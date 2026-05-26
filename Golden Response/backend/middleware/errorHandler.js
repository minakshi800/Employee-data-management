const multer = require('multer');

const AppError = require('../utils/AppError');
const logger = require('../utils/logger');

const notFoundHandler = (req, _res, next) => {
  next(new AppError(404, `Route not found: ${req.method} ${req.originalUrl}`));
};

const errorHandler = (err, req, res, _next) => {
  if (err instanceof multer.MulterError) {
    return res.status(400).json({
      success: false,
      message: err.message
    });
  }

  if (err && err.code === 11000) {
    return res.status(409).json({
      success: false,
      message: 'A unique field already exists',
      details: err.keyValue
    });
  }

  const statusCode = err.statusCode || 500;
  const message = err.message || 'Internal server error';

  logger.error({
    message,
    statusCode,
    stack: err.stack,
    method: req.method,
    path: req.originalUrl
  });

  return res.status(statusCode).json({
    success: false,
    message,
    details: err.details || undefined
  });
};

module.exports = {
  notFoundHandler,
  errorHandler
};
