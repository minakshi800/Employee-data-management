const crypto = require('crypto');
const jwt = require('jsonwebtoken');

const getJwtConfig = () => ({
  accessSecret: process.env.JWT_SECRET,
  refreshSecret: process.env.JWT_REFRESH_SECRET,
  accessExpiresIn: process.env.ACCESS_TOKEN_EXP || '15m',
  refreshExpiresIn: process.env.REFRESH_TOKEN_EXP || '7d'
});

const buildAuthPayload = (user) => ({
  sub: user._id.toString(),
  email: user.email,
  role: user.role
});

const signAccessToken = (user) => {
  const { accessSecret, accessExpiresIn } = getJwtConfig();
  return jwt.sign(buildAuthPayload(user), accessSecret, {
    expiresIn: accessExpiresIn
  });
};

const signRefreshToken = (user) => {
  const { refreshSecret, refreshExpiresIn } = getJwtConfig();
  return jwt.sign(buildAuthPayload(user), refreshSecret, {
    expiresIn: refreshExpiresIn
  });
};

const hashToken = (token) => crypto.createHash('sha256').update(token).digest('hex');

module.exports = {
  signAccessToken,
  signRefreshToken,
  hashToken
};
