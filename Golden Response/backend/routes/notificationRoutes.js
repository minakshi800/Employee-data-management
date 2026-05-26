const express = require('express');
const { body } = require('express-validator');

const { contactHr } = require('../controllers/notificationController');
const { authenticate } = require('../middleware/auth');
const validateRequest = require('../middleware/validateRequest');

const router = express.Router();

router.post(
  '/contact-hr',
  authenticate,
  [
    body('name').trim().notEmpty().withMessage('Name is required'),
    body('email').trim().isEmail().withMessage('Valid email is required'),
    body('employeeId').trim().notEmpty().withMessage('Employee ID is required'),
    body('subject').trim().notEmpty().withMessage('Subject is required'),
    body('message')
      .trim()
      .isLength({ min: 10, max: 2000 })
      .withMessage('Message must be between 10 and 2000 characters')
  ],
  validateRequest,
  contactHr
);

module.exports = router;
