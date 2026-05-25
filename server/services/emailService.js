const nodemailer = require('nodemailer');

const logger = require('../utils/logger');

const hasMailConfig = () =>
  Boolean(
    process.env.SMTP_HOST &&
      process.env.SMTP_PORT &&
      process.env.SMTP_USER &&
      process.env.SMTP_PASS
  );

const getTransporter = () => {
  if (!hasMailConfig()) {
    return null;
  }

  return nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: Number(process.env.SMTP_PORT),
    secure: Number(process.env.SMTP_PORT) === 465,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS
    }
  });
};

const sendMail = async ({ to, subject, text, html }) => {
  const transporter = getTransporter();

  if (!transporter) {
    logger.warn({
      message: 'SMTP is not configured; email delivery skipped',
      to,
      subject
    });

    return {
      delivered: false,
      reason: 'SMTP is not configured'
    };
  }

  const info = await transporter.sendMail({
    from: process.env.MAIL_FROM || process.env.SMTP_USER,
    to,
    subject,
    text,
    html
  });

  return {
    delivered: true,
    messageId: info.messageId
  };
};

const sendRegistrationEmail = ({ email, name }) =>
  sendMail({
    to: email,
    subject: 'Welcome to EDMS',
    text: `Hello ${name}, your EDMS account has been created successfully.`,
    html: `<p>Hello ${name},</p><p>Your EDMS account has been created successfully.</p>`
  });

const sendPasswordResetEmail = ({ email, name, resetToken }) => {
  const resetUrl = `${process.env.CLIENT_APP_URL || 'http://localhost:3000'}/reset-password?token=${resetToken}`;

  return sendMail({
    to: email,
    subject: 'Reset your EDMS password',
    text: `Hello ${name}, use this link to reset your password: ${resetUrl}`,
    html: `<p>Hello ${name},</p><p>Reset your password using this link:</p><p><a href="${resetUrl}">${resetUrl}</a></p>`
  });
};

const sendContactHrEmail = ({ name, email, employeeId, subject, message }) =>
  sendMail({
    to: process.env.HR_NOTIFICATION_EMAIL || process.env.SMTP_USER,
    subject: `[Contact HR] ${subject}`,
    text: `Name: ${name}\nEmail: ${email}\nEmployee ID: ${employeeId}\nTimestamp: ${new Date().toISOString()}\n\n${message}`,
    html: `<p><strong>Name:</strong> ${name}</p><p><strong>Email:</strong> ${email}</p><p><strong>Employee ID:</strong> ${employeeId}</p><p><strong>Timestamp:</strong> ${new Date().toISOString()}</p><p>${message}</p>`
  });

module.exports = {
  sendRegistrationEmail,
  sendPasswordResetEmail,
  sendContactHrEmail
};
