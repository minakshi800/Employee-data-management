const crypto = require('crypto');
const bcrypt = require('bcryptjs');

const User = require('../models/User');
const Employee = require('../models/Employee');
const asyncHandler = require('../utils/asyncHandler');
const AppError = require('../utils/AppError');
const { sendSuccess } = require('../utils/http');
const { signAccessToken, signRefreshToken, hashToken } = require('../utils/tokens');
const { sendRegistrationEmail, sendPasswordResetEmail } = require('../services/emailService');
const logger = require('../utils/logger');

const sanitizeUser = (user) => ({
  id: user._id,
  name: user.name,
  email: user.email,
  role: user.role,
  employee: user.employee,
  lastLoginAt: user.lastLoginAt,
  createdAt: user.createdAt,
  updatedAt: user.updatedAt
});

const setRefreshCookie = (res, refreshToken) => {
  res.cookie('refreshToken', refreshToken, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'strict',
    maxAge: 7 * 24 * 60 * 60 * 1000
  });
};

const clearAuthCookies = (res) => {
  res.clearCookie('refreshToken');
  res.clearCookie('accessToken');
};

const issueTokens = async (user, res) => {
  const accessToken = signAccessToken(user);
  const refreshToken = signRefreshToken(user);

  user.refreshTokenHash = hashToken(refreshToken);
  user.lastLoginAt = new Date();
  await user.save();

  setRefreshCookie(res, refreshToken);

  return {
    accessToken,
    refreshToken
  };
};

const resolveRegistrationRole = (requestedRole, bootstrapKey) => {
  const validRole = ['admin', 'hr', 'employee'].includes(requestedRole)
    ? requestedRole
    : 'employee';

  if (validRole === 'employee') {
    return 'employee';
  }

  if (
    process.env.ADMIN_BOOTSTRAP_KEY &&
    bootstrapKey &&
    bootstrapKey === process.env.ADMIN_BOOTSTRAP_KEY
  ) {
    return validRole;
  }

  return 'employee';
};

const register = asyncHandler(async (req, res) => {
  const { name, email, password, role = 'employee', employeeId, bootstrapKey } = req.body;

  const existingUser = await User.findOne({ email: email.toLowerCase() });
  if (existingUser) {
    throw new AppError(409, 'An account with this email already exists');
  }

  let linkedEmployee = null;
  if (employeeId) {
    linkedEmployee = await Employee.findOne({ employeeId });

    if (!linkedEmployee) {
      throw new AppError(404, 'Employee record not found for the supplied employee ID');
    }

    if (linkedEmployee.user) {
      throw new AppError(409, 'This employee record is already linked to a user account');
    }
  }

  const passwordHash = await bcrypt.hash(password, 12);
  const resolvedRole = resolveRegistrationRole(role, bootstrapKey);
  const user = await User.create({
    name,
    email: email.toLowerCase(),
    passwordHash,
    role: resolvedRole,
    employee: linkedEmployee ? linkedEmployee._id : undefined
  });

  if (linkedEmployee) {
    linkedEmployee.user = user._id;
    await linkedEmployee.save();
  }

  const tokens = await issueTokens(user, res);
  const emailResult = await sendRegistrationEmail({ email: user.email, name: user.name });

  return sendSuccess(
    res,
    'User registered successfully',
    {
      user: sanitizeUser(user),
      tokens,
      emailNotification: emailResult
    },
    201
  );
});

const login = asyncHandler(async (req, res) => {
  const { email, password } = req.body;

  const user = await User.findOne({ email: email.toLowerCase() });
  if (!user) {
    logger.warn({ message: 'Failed login attempt', email });
    throw new AppError(401, 'Invalid email or password');
  }

  const isPasswordValid = await bcrypt.compare(password, user.passwordHash);
  if (!isPasswordValid) {
    logger.warn({ message: 'Failed login attempt', email });
    throw new AppError(401, 'Invalid email or password');
  }

  const tokens = await issueTokens(user, res);
  const populatedUser = await User.findById(user._id)
    .select('-passwordHash -refreshTokenHash -resetPasswordTokenHash')
    .populate('employee');

  return sendSuccess(res, 'Login successful', {
    user: populatedUser,
    tokens
  });
});

const refresh = asyncHandler(async (req, res) => {
  const providedToken = req.cookies.refreshToken || req.body.refreshToken;
  if (!providedToken) {
    throw new AppError(401, 'Refresh token is required');
  }

  const decoded = require('jsonwebtoken').verify(providedToken, process.env.JWT_REFRESH_SECRET);
  const user = await User.findById(decoded.sub);

  if (!user || user.refreshTokenHash !== hashToken(providedToken)) {
    throw new AppError(401, 'Refresh token is invalid or expired');
  }

  const tokens = await issueTokens(user, res);

  return sendSuccess(res, 'Token refreshed successfully', {
    accessToken: tokens.accessToken,
    refreshToken: tokens.refreshToken
  });
});

const logout = asyncHandler(async (req, res) => {
  const providedToken = req.cookies.refreshToken || req.body.refreshToken;

  if (providedToken) {
    try {
      const decoded = require('jsonwebtoken').verify(
        providedToken,
        process.env.JWT_REFRESH_SECRET
      );
      const user = await User.findById(decoded.sub);

      if (user) {
        user.refreshTokenHash = undefined;
        await user.save();
      }
    } catch (_error) {
      logger.warn({ message: 'Logout requested with an invalid refresh token' });
    }
  }

  clearAuthCookies(res);

  return sendSuccess(res, 'Logged out successfully');
});

const me = asyncHandler(async (req, res) => {
  const user = await User.findById(req.user._id)
    .select('-passwordHash -refreshTokenHash -resetPasswordTokenHash')
    .populate('employee');

  return sendSuccess(res, 'Current user fetched successfully', { user });
});

const forgotPassword = asyncHandler(async (req, res) => {
  const { email } = req.body;
  const user = await User.findOne({ email: email.toLowerCase() });

  if (!user) {
    return sendSuccess(res, 'If the account exists, a reset email has been queued');
  }

  const resetToken = crypto.randomBytes(32).toString('hex');
  user.resetPasswordTokenHash = hashToken(resetToken);
  user.resetPasswordExpiresAt = new Date(Date.now() + 1000 * 60 * 30);
  await user.save();

  const emailResult = await sendPasswordResetEmail({
    email: user.email,
    name: user.name,
    resetToken
  });

  return sendSuccess(res, 'Password reset instructions have been sent', {
    emailNotification: emailResult
  });
});

const resetPassword = asyncHandler(async (req, res) => {
  const { token, newPassword } = req.body;
  const hashedToken = hashToken(token);

  const user = await User.findOne({
    resetPasswordTokenHash: hashedToken,
    resetPasswordExpiresAt: { $gt: new Date() }
  });

  if (!user) {
    throw new AppError(400, 'Password reset token is invalid or expired');
  }

  user.passwordHash = await bcrypt.hash(newPassword, 12);
  user.resetPasswordTokenHash = undefined;
  user.resetPasswordExpiresAt = undefined;
  user.refreshTokenHash = undefined;
  await user.save();

  clearAuthCookies(res);

  return sendSuccess(res, 'Password has been reset successfully');
});

module.exports = {
  register,
  login,
  refresh,
  logout,
  me,
  forgotPassword,
  resetPassword
};
