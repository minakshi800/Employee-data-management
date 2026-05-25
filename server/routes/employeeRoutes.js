const express = require('express');
const { body, query } = require('express-validator');

const {
  listEmployees,
  getEmployee,
  createEmployee,
  updateEmployee,
  deleteEmployee,
  recordAttendance
} = require('../controllers/employeeController');
const { authenticate, authorize } = require('../middleware/auth');
const validateRequest = require('../middleware/validateRequest');
const { employeeUpload } = require('../middleware/upload');

const router = express.Router();

router.use(authenticate);

router.get(
  '/',
  authorize('admin', 'hr'),
  [
    query('page').optional().isInt({ min: 1 }).withMessage('page must be a positive integer'),
    query('limit').optional().isInt({ min: 1, max: 100 }).withMessage('limit must be between 1 and 100')
  ],
  validateRequest,
  listEmployees
);

router.get('/:id', getEmployee);

router.post(
  '/',
  authorize('admin', 'hr'),
  employeeUpload,
  [
    body('firstName').trim().notEmpty().withMessage('firstName is required'),
    body('lastName').trim().notEmpty().withMessage('lastName is required'),
    body('email').trim().isEmail().withMessage('Valid email is required'),
    body('employeeId').trim().notEmpty().withMessage('employeeId is required'),
    body('salary').optional().isFloat({ min: 0 }).withMessage('salary must be zero or greater'),
    body('status')
      .optional()
      .isIn(['active', 'inactive', 'terminated'])
      .withMessage('Invalid status')
  ],
  validateRequest,
  createEmployee
);

router.put(
  '/:id',
  authorize('admin', 'hr'),
  employeeUpload,
  [
    body('email').optional().trim().isEmail().withMessage('email must be valid'),
    body('salary').optional().isFloat({ min: 0 }).withMessage('salary must be zero or greater'),
    body('status')
      .optional()
      .isIn(['active', 'inactive', 'terminated'])
      .withMessage('Invalid status')
  ],
  validateRequest,
  updateEmployee
);

router.delete('/:id', authorize('admin'), deleteEmployee);

router.post(
  '/:id/attendance',
  authorize('admin', 'hr'),
  [
    body('status')
      .isIn(['present', 'absent', 'leave'])
      .withMessage('status must be present, absent, or leave'),
    body('date').optional().isISO8601().withMessage('date must be a valid ISO date')
  ],
  validateRequest,
  recordAttendance
);

module.exports = router;
