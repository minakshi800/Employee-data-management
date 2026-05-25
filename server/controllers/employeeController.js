const path = require('path');

const Employee = require('../models/Employee');
const asyncHandler = require('../utils/asyncHandler');
const AppError = require('../utils/AppError');
const { sendSuccess } = require('../utils/http');
const logger = require('../utils/logger');

const parseJsonField = (value, fallback = {}) => {
  if (!value) {
    return fallback;
  }

  if (typeof value === 'object') {
    return value;
  }

  try {
    return JSON.parse(value);
  } catch (_error) {
    return fallback;
  }
};

const normalizeFiles = (files = {}) => {
  const profileImageFile = files.profileImage ? files.profileImage[0] : null;
  const documentFiles = files.documents || [];

  return {
    profileImage: profileImageFile
      ? path.relative(path.join(__dirname, '..'), profileImageFile.path).replace(/\\/g, '/')
      : undefined,
    documents: documentFiles.map((file) => ({
      filename: file.filename,
      originalname: file.originalname,
      mimeType: file.mimetype,
      size: file.size,
      path: path.relative(path.join(__dirname, '..'), file.path).replace(/\\/g, '/')
    }))
  };
};

const buildEmployeePayload = (body, files) => {
  const uploads = normalizeFiles(files);
  const hasEmergencyContact =
    body.emergencyContact ||
    body.emergencyContactName ||
    body.emergencyContactRelation ||
    body.emergencyContactPhone;
  const payload = {
    firstName: body.firstName,
    lastName: body.lastName,
    email: body.email?.toLowerCase(),
    phone: body.phone,
    employeeId: body.employeeId,
    department: body.department,
    designation: body.designation,
    roleTitle: body.roleTitle,
    status: body.status,
    salary: body.salary !== undefined ? Number(body.salary) : undefined,
    joiningDate: body.joiningDate || undefined,
    emergencyContact: hasEmergencyContact
      ? parseJsonField(body.emergencyContact, {
          name: body.emergencyContactName,
          relation: body.emergencyContactRelation,
          phone: body.emergencyContactPhone
        })
      : undefined
  };

  if (uploads.profileImage) {
    payload.profileImage = uploads.profileImage;
  }

  if (uploads.documents.length) {
    payload.documents = uploads.documents;
  }

  return payload;
};

const findEmployeeOrThrow = async (employeeId) => {
  const employee = await Employee.findById(employeeId).populate('user', 'name email role');
  if (!employee) {
    throw new AppError(404, 'Employee not found');
  }

  return employee;
};

const ensureEmployeeScope = (req, employee) => {
  if (req.user.role === 'employee') {
    if (!employee.user || employee.user._id.toString() !== req.user._id.toString()) {
      throw new AppError(403, 'Employees can only access their own profile');
    }
  }
};

const listEmployees = asyncHandler(async (req, res) => {
  const page = Math.max(Number(req.query.page) || 1, 1);
  const limit = Math.min(Math.max(Number(req.query.limit) || 10, 1), 100);
  const skip = (page - 1) * limit;
  const sortBy = req.query.sortBy || 'createdAt';
  const sortOrder = req.query.sortOrder === 'asc' ? 1 : -1;

  const filters = {};

  if (req.query.department) {
    filters.department = req.query.department;
  }

  if (req.query.designation) {
    filters.designation = req.query.designation;
  }

  if (req.query.status) {
    filters.status = req.query.status;
  }

  if (req.query.minSalary || req.query.maxSalary) {
    filters.salary = {};
    if (req.query.minSalary) {
      filters.salary.$gte = Number(req.query.minSalary);
    }
    if (req.query.maxSalary) {
      filters.salary.$lte = Number(req.query.maxSalary);
    }
  }

  if (req.query.joinedFrom || req.query.joinedTo) {
    filters.joiningDate = {};
    if (req.query.joinedFrom) {
      filters.joiningDate.$gte = new Date(req.query.joinedFrom);
    }
    if (req.query.joinedTo) {
      filters.joiningDate.$lte = new Date(req.query.joinedTo);
    }
  }

  if (req.query.search) {
    const searchRegex = new RegExp(req.query.search.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i');
    filters.$or = [
      { firstName: searchRegex },
      { lastName: searchRegex },
      { email: searchRegex },
      { employeeId: searchRegex },
      { department: searchRegex }
    ];
  }

  const allowedSortFields = new Set([
    'firstName',
    'department',
    'salary',
    'joiningDate',
    'createdAt',
    'updatedAt'
  ]);
  const sortField = allowedSortFields.has(sortBy) ? sortBy : 'createdAt';

  const [items, total] = await Promise.all([
    Employee.find(filters)
      .populate('user', 'name email role')
      .sort({ [sortField]: sortOrder })
      .skip(skip)
      .limit(limit),
    Employee.countDocuments(filters)
  ]);

  return sendSuccess(res, 'Employees fetched successfully', {
    items,
    pagination: {
      page,
      limit,
      total,
      totalPages: Math.ceil(total / limit)
    }
  });
});

const getEmployee = asyncHandler(async (req, res) => {
  const employee = await findEmployeeOrThrow(req.params.id);
  ensureEmployeeScope(req, employee);

  return sendSuccess(res, 'Employee fetched successfully', { employee });
});

const createEmployee = asyncHandler(async (req, res) => {
  const payload = buildEmployeePayload(req.body, req.files);

  const duplicate = await Employee.findOne({
    $or: [{ email: payload.email }, { employeeId: payload.employeeId }]
  });
  if (duplicate) {
    throw new AppError(409, 'Employee email or employee ID already exists');
  }

  const employee = await Employee.create(payload);
  logger.info({
    message: 'Employee created',
    actor: req.user.email,
    employeeId: employee.employeeId
  });

  return sendSuccess(res, 'Employee created successfully', { employee }, 201);
});

const updateEmployee = asyncHandler(async (req, res) => {
  const employee = await findEmployeeOrThrow(req.params.id);
  const payload = buildEmployeePayload(req.body, req.files);

  Object.entries(payload).forEach(([key, value]) => {
    if (value === undefined) {
      return;
    }

    if (key === 'documents' && Array.isArray(value) && value.length) {
      employee.documents.push(...value);
      return;
    }

    employee[key] = value;
  });

  await employee.save();
  logger.info({
    message: 'Employee updated',
    actor: req.user.email,
    employeeId: employee.employeeId
  });

  return sendSuccess(res, 'Employee updated successfully', { employee });
});

const deleteEmployee = asyncHandler(async (req, res) => {
  const employee = await findEmployeeOrThrow(req.params.id);
  await employee.deleteOne();

  logger.info({
    message: 'Employee deleted',
    actor: req.user.email,
    employeeId: employee.employeeId
  });

  return sendSuccess(res, 'Employee deleted successfully');
});

const recordAttendance = asyncHandler(async (req, res) => {
  const employee = await findEmployeeOrThrow(req.params.id);
  employee.attendance.push({
    date: req.body.date || new Date(),
    status: req.body.status,
    note: req.body.note
  });
  await employee.save();

  return sendSuccess(res, 'Attendance recorded successfully', { employee });
});

module.exports = {
  listEmployees,
  getEmployee,
  createEmployee,
  updateEmployee,
  deleteEmployee,
  recordAttendance
};
