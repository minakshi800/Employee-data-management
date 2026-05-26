const express = require('express');

const { getOverview } = require('../controllers/analyticsController');
const { authenticate, authorize } = require('../middleware/auth');

const router = express.Router();

router.get('/overview', authenticate, authorize('admin', 'hr'), getOverview);

module.exports = router;
