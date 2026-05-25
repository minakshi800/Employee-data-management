const express = require('express');
const rateLimit = require('express-rate-limit');
const { body } = require('express-validator');

const {
  register,
  login,
  refresh,
  logout,
  me,
  forgotPassword,
  resetPassword
} = require('../controllers/authController');
const validateRequest = require('../middleware/validateRequest');
const { authenticate, authorize } = require('../middleware/auth');

const router = express.Router();

const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 20,
  standardHeaders: true,
  legacyHeaders: false
});

router.post(
  '/register',
  authLimiter,
  [
    body('name').trim().notEmpty().withMessage('Name is required'),
    body('email').trim().isEmail().withMessage('Valid email is required'),
    body('password')
      .isLength({ min: 8 })
      .withMessage('Password must be at least 8 characters long'),
    body('role')
      .optional()
      .isIn(['admin', 'hr', 'employee'])
      .withMessage('Role must be admin, hr, or employee'),
    body('bootstrapKey')
      .optional()
      .isString()
      .withMessage('bootstrapKey must be a string'),
    body('employeeId').optional().trim().notEmpty().withMessage('employeeId cannot be empty')
  ],
  validateRequest,
  register
);

router.post(
  '/login',
  authLimiter,
  [
    body('email').trim().isEmail().withMessage('Valid email is required'),
    body('password').notEmpty().withMessage('Password is required')
  ],
  validateRequest,
  login
);

router.post('/refresh', refresh);
router.post('/logout', logout);
router.get('/me', authenticate, me);

router.post(
  '/forgot-password',
  authLimiter,
  [body('email').trim().isEmail().withMessage('Valid email is required')],
  validateRequest,
  forgotPassword
);

router.post(
  '/reset-password',
  authLimiter,
  [
    body('token').trim().notEmpty().withMessage('Reset token is required'),
    body('newPassword')
      .isLength({ min: 8 })
      .withMessage('New password must be at least 8 characters long')
  ],
  validateRequest,
  resetPassword
);

router.get('/users/roles', authenticate, authorize('admin'), (_req, res) => {
  res.json({
    success: true,
    message: 'Roles fetched successfully',
    data: {
      roles: ['admin', 'hr', 'employee']
    }
  });
});

module.exports = router;
