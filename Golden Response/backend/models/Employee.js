const mongoose = require('mongoose');

const EmployeeSchema = new mongoose.Schema(
  {
    user: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'User',
      index: true
    },
    firstName: { type: String, required: true, trim: true },
    lastName: { type: String, required: true, trim: true },
    email: {
      type: String,
      required: true,
      lowercase: true,
      trim: true,
      unique: true,
      index: true
    },
    phone: { type: String, trim: true },
    employeeId: { type: String, required: true, unique: true, trim: true, index: true },
    department: { type: String, trim: true, index: true },
    designation: { type: String, trim: true },
    roleTitle: { type: String, trim: true },
    status: {
      type: String,
      enum: ['active', 'inactive', 'terminated'],
      default: 'active',
      index: true
    },
    salary: { type: Number, default: 0, min: 0, index: true },
    joiningDate: { type: Date, index: true },
    emergencyContact: {
      name: String,
      relation: String,
      phone: String
    },
    documents: [
      {
        filename: String,
        originalname: String,
        mimeType: String,
        size: Number,
        path: String,
        uploadedAt: { type: Date, default: Date.now }
      }
    ],
    profileImage: { type: String },
    attendance: [
      {
        date: { type: Date, required: true },
        status: { type: String, enum: ['present', 'absent', 'leave'], required: true },
        note: { type: String, trim: true }
      }
    ]
  },
  {
    timestamps: true
  }
);

EmployeeSchema.index({ firstName: 'text', lastName: 'text', email: 'text', department: 'text' });

module.exports = mongoose.model('Employee', EmployeeSchema);
