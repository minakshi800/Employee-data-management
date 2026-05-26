const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema(
  {
    name: { type: String, required: true, trim: true },
    email: { type: String, required: true, unique: true, lowercase: true, trim: true },
    passwordHash: { type: String, required: true },
    role: { type: String, enum: ['admin', 'hr', 'employee'], default: 'employee' },
    employee: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Employee',
      index: true
    },
    refreshTokenHash: { type: String },
    resetPasswordTokenHash: { type: String },
    resetPasswordExpiresAt: { type: Date },
    lastLoginAt: { type: Date }
  },
  {
    timestamps: true
  }
);

module.exports = mongoose.model('User', UserSchema);
