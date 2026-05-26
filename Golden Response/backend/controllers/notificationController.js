const asyncHandler = require('../utils/asyncHandler');
const { sendSuccess } = require('../utils/http');
const { sendContactHrEmail } = require('../services/emailService');

const contactHr = asyncHandler(async (req, res) => {
  const emailResult = await sendContactHrEmail({
    name: req.body.name,
    email: req.body.email,
    employeeId: req.body.employeeId,
    subject: req.body.subject,
    message: req.body.message
  });

  return sendSuccess(
    res,
    'HR contact request submitted successfully',
    {
      emailNotification: emailResult
    },
    202
  );
});

module.exports = {
  contactHr
};
