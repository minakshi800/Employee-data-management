export const mockCurrentUser = {
  _id: 'user-1',
  name: 'Avery Carter',
  email: 'avery.carter@northpass.co',
  role: 'admin',
  employee: {
    _id: 'emp-1',
    employeeId: 'EDM-1024',
    department: 'Operations'
  }
};

export const mockEmployees = [
  {
    _id: 'emp-1',
    firstName: 'Avery',
    lastName: 'Carter',
    email: 'avery.carter@northpass.co',
    phone: '+1 555 0192',
    employeeId: 'EDM-1024',
    department: 'Operations',
    designation: 'Director of Operations',
    roleTitle: 'Leadership',
    status: 'active',
    salary: 142000,
    joiningDate: '2022-02-18T00:00:00.000Z',
    emergencyContact: {
      name: 'Jordan Carter',
      relation: 'Spouse',
      phone: '+1 555 0131'
    },
    attendance: [
      { date: '2026-05-20T00:00:00.000Z', status: 'present' },
      { date: '2026-05-21T00:00:00.000Z', status: 'present' },
      { date: '2026-05-22T00:00:00.000Z', status: 'leave' }
    ],
    documents: [{ originalname: 'executive-contract.pdf', mimeType: 'application/pdf' }],
    profileImage: '',
    updatedAt: '2026-05-24T09:00:00.000Z',
    createdAt: '2022-02-18T00:00:00.000Z'
  },
  {
    _id: 'emp-2',
    firstName: 'Mina',
    lastName: 'Lopez',
    email: 'mina.lopez@northpass.co',
    phone: '+1 555 0107',
    employeeId: 'EDM-1042',
    department: 'People',
    designation: 'HR Business Partner',
    roleTitle: 'HR',
    status: 'active',
    salary: 92000,
    joiningDate: '2023-04-12T00:00:00.000Z',
    emergencyContact: {
      name: 'Lucas Lopez',
      relation: 'Brother',
      phone: '+1 555 0146'
    },
    attendance: [
      { date: '2026-05-20T00:00:00.000Z', status: 'present' },
      { date: '2026-05-21T00:00:00.000Z', status: 'present' },
      { date: '2026-05-22T00:00:00.000Z', status: 'present' }
    ],
    documents: [{ originalname: 'benefits-guide.pdf', mimeType: 'application/pdf' }],
    profileImage: '',
    updatedAt: '2026-05-24T11:12:00.000Z',
    createdAt: '2023-04-12T00:00:00.000Z'
  },
  {
    _id: 'emp-3',
    firstName: 'Kei',
    lastName: 'Tanaka',
    email: 'kei.tanaka@northpass.co',
    phone: '+1 555 0128',
    employeeId: 'EDM-1061',
    department: 'Engineering',
    designation: 'Platform Engineer',
    roleTitle: 'IC',
    status: 'active',
    salary: 128000,
    joiningDate: '2024-01-08T00:00:00.000Z',
    emergencyContact: {
      name: 'Aiko Tanaka',
      relation: 'Parent',
      phone: '+1 555 0184'
    },
    attendance: [
      { date: '2026-05-20T00:00:00.000Z', status: 'present' },
      { date: '2026-05-21T00:00:00.000Z', status: 'absent' },
      { date: '2026-05-22T00:00:00.000Z', status: 'present' }
    ],
    documents: [],
    profileImage: '',
    updatedAt: '2026-05-23T17:43:00.000Z',
    createdAt: '2024-01-08T00:00:00.000Z'
  },
  {
    _id: 'emp-4',
    firstName: 'Sana',
    lastName: 'Rahman',
    email: 'sana.rahman@northpass.co',
    phone: '+1 555 0176',
    employeeId: 'EDM-1084',
    department: 'Finance',
    designation: 'Senior Analyst',
    roleTitle: 'IC',
    status: 'active',
    salary: 104000,
    joiningDate: '2023-09-21T00:00:00.000Z',
    emergencyContact: {
      name: 'Mariam Rahman',
      relation: 'Parent',
      phone: '+1 555 0177'
    },
    attendance: [
      { date: '2026-05-20T00:00:00.000Z', status: 'present' },
      { date: '2026-05-21T00:00:00.000Z', status: 'present' },
      { date: '2026-05-22T00:00:00.000Z', status: 'present' }
    ],
    documents: [{ originalname: 'nda.pdf', mimeType: 'application/pdf' }],
    profileImage: '',
    updatedAt: '2026-05-24T08:00:00.000Z',
    createdAt: '2023-09-21T00:00:00.000Z'
  },
  {
    _id: 'emp-5',
    firstName: 'Theo',
    lastName: 'Mercer',
    email: 'theo.mercer@northpass.co',
    phone: '+1 555 0160',
    employeeId: 'EDM-1102',
    department: 'Design',
    designation: 'Product Designer',
    roleTitle: 'IC',
    status: 'inactive',
    salary: 96000,
    joiningDate: '2024-05-30T00:00:00.000Z',
    emergencyContact: {
      name: 'Iris Mercer',
      relation: 'Partner',
      phone: '+1 555 0164'
    },
    attendance: [
      { date: '2026-05-20T00:00:00.000Z', status: 'leave' },
      { date: '2026-05-21T00:00:00.000Z', status: 'leave' }
    ],
    documents: [],
    profileImage: '',
    updatedAt: '2026-05-22T13:28:00.000Z',
    createdAt: '2024-05-30T00:00:00.000Z'
  },
  {
    _id: 'emp-6',
    firstName: 'Noah',
    lastName: 'Patel',
    email: 'noah.patel@northpass.co',
    phone: '+1 555 0151',
    employeeId: 'EDM-1118',
    department: 'Engineering',
    designation: 'QA Automation Engineer',
    roleTitle: 'IC',
    status: 'active',
    salary: 89000,
    joiningDate: '2025-01-15T00:00:00.000Z',
    emergencyContact: {
      name: 'Riya Patel',
      relation: 'Sister',
      phone: '+1 555 0158'
    },
    attendance: [
      { date: '2026-05-20T00:00:00.000Z', status: 'present' },
      { date: '2026-05-21T00:00:00.000Z', status: 'present' },
      { date: '2026-05-22T00:00:00.000Z', status: 'present' }
    ],
    documents: [{ originalname: 'qa-certification.pdf', mimeType: 'application/pdf' }],
    profileImage: '',
    updatedAt: '2026-05-25T08:45:00.000Z',
    createdAt: '2025-01-15T00:00:00.000Z'
  }
];

export const mockAnalytics = {
  totalEmployees: 186,
  departmentDistribution: [
    { department: 'Engineering', count: 54 },
    { department: 'Operations', count: 31 },
    { department: 'People', count: 22 },
    { department: 'Finance', count: 18 },
    { department: 'Design', count: 16 }
  ],
  salarySummary: {
    averageSalary: 108400,
    totalSalary: 20162400,
    maxSalary: 231000,
    minSalary: 56000
  },
  monthlyHiring: [
    { _id: { year: 2025, month: 6 }, hires: 8 },
    { _id: { year: 2025, month: 7 }, hires: 6 },
    { _id: { year: 2025, month: 8 }, hires: 10 },
    { _id: { year: 2025, month: 9 }, hires: 5 },
    { _id: { year: 2025, month: 10 }, hires: 12 },
    { _id: { year: 2025, month: 11 }, hires: 7 },
    { _id: { year: 2025, month: 12 }, hires: 9 },
    { _id: { year: 2026, month: 1 }, hires: 11 },
    { _id: { year: 2026, month: 2 }, hires: 6 },
    { _id: { year: 2026, month: 3 }, hires: 14 },
    { _id: { year: 2026, month: 4 }, hires: 9 },
    { _id: { year: 2026, month: 5 }, hires: 13 }
  ],
  attendanceSummary: [
    { status: 'present', count: 422 },
    { status: 'leave', count: 28 },
    { status: 'absent', count: 14 }
  ],
  recentActivity: mockEmployees.slice(0, 5).map((employee) => ({
    _id: employee._id,
    firstName: employee.firstName,
    lastName: employee.lastName,
    employeeId: employee.employeeId,
    department: employee.department,
    updatedAt: employee.updatedAt
  }))
};
