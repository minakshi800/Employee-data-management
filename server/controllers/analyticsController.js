const Employee = require('../models/Employee');
const asyncHandler = require('../utils/asyncHandler');
const { sendSuccess } = require('../utils/http');

const getOverview = asyncHandler(async (_req, res) => {
  const [totalEmployees, departmentDistribution, salarySummary, monthlyHiring, attendanceSummary, recentActivity] =
    await Promise.all([
      Employee.countDocuments(),
      Employee.aggregate([
        { $group: { _id: '$department', count: { $sum: 1 } } },
        { $project: { _id: 0, department: '$_id', count: 1 } },
        { $sort: { count: -1 } }
      ]),
      Employee.aggregate([
        {
          $group: {
            _id: null,
            averageSalary: { $avg: '$salary' },
            totalSalary: { $sum: '$salary' },
            maxSalary: { $max: '$salary' },
            minSalary: { $min: '$salary' }
          }
        },
        { $project: { _id: 0 } }
      ]),
      Employee.aggregate([
        {
          $match: {
            joiningDate: {
              $gte: new Date(new Date().setMonth(new Date().getMonth() - 11))
            }
          }
        },
        {
          $group: {
            _id: {
              year: { $year: '$joiningDate' },
              month: { $month: '$joiningDate' }
            },
            hires: { $sum: 1 }
          }
        },
        { $sort: { '_id.year': 1, '_id.month': 1 } }
      ]),
      Employee.aggregate([
        { $unwind: { path: '$attendance', preserveNullAndEmptyArrays: true } },
        {
          $group: {
            _id: '$attendance.status',
            count: { $sum: 1 }
          }
        },
        { $project: { _id: 0, status: '$_id', count: 1 } }
      ]),
      Employee.find()
        .sort({ updatedAt: -1 })
        .limit(5)
        .select('firstName lastName employeeId department updatedAt createdAt')
    ]);

  return sendSuccess(res, 'Analytics overview fetched successfully', {
    totalEmployees,
    departmentDistribution,
    salarySummary: salarySummary[0] || {
      averageSalary: 0,
      totalSalary: 0,
      maxSalary: 0,
      minSalary: 0
    },
    monthlyHiring,
    attendanceSummary,
    recentActivity
  });
});

module.exports = {
  getOverview
};
