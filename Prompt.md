AI-Powered Employee Data Management System
Context and Role
As a Full-Stack Software Engineer specializing in enterprise web applications, you are responsible for designing and developing a modern AI-powered Employee Data Management System that provides secure employee record handling, analytics, role-based access, real-time data visualization, and smooth interactive user experiences.

The system must include a modern frontend with animated UI interactions and a scalable backend architecture with secure authentication and intelligent employee management workflows. This platform should support HR teams, managers, and administrators in managing employee information efficiently while ensuring security, scalability, and excellent user experience.

Objective
Develop a complete production-ready Employee Data Management System that:

Manages employee records securely
Provides animated dashboards and smooth interactions
Supports authentication and role-based access
Includes employee analytics and reporting
Allows CRUD operations for employee data
Includes search, filtering, and sorting
Sends email notifications for important actions
Stores employee data securely in a database
Provides responsive and accessible UI
Core Features
Employee Management
The system must allow:

Add employee records
Edit employee information
Delete employee records
View employee details
Upload employee profile images/documents
Track department and designation
Manage salary and joining date
Store emergency contact details
Dashboard Requirements
Animated Dashboard UI
Implement modern UI animations using Framer Motion:

Smooth page transitions
Animated cards and charts
Staggered dashboard loading animations
Hover effects on employee cards
Animated sidebar navigation
Scroll-triggered section animations
Real-time counters and stat widgets
Animation Constraints
Animations must:

Be GPU optimized
Use transform and opacity properties
Avoid unnecessary re-renders
Maintain high FPS performance
Layout Requirements
Admin Dashboard
Includes:

Employee overview cards
Total employees
Department statistics
Salary analytics
Attendance summary
Recent activity logs
Check activity
New data
Employee Table
Features:

Pagination
Search functionality
Advanced filtering
Sorting by:
Name
Department
Salary
Joining date
Employee Profile Page
Contains:

Personal details
Contact information
Department
Role
Attendance records
Salary information
Uploaded documents
Analytics Section
Display:

Employee growth charts
Department distribution graphs
Salary trend analytics
Monthly hiring reports
Use animated charts and visualizations.

Authentication and Security Requirements
Authentication System
Implement secure authentication using:

JWT authentication
Secure password hashing
Session management
Refresh tokens
Role-Based Access Control
Roles
Admin
HR Manager
Employee
Permissions
Admin can manage all employees
HR can update employee records
Employees can view only their profile
Contact and Notification System
Contact Modal
Include a "Contact HR" button that:

Opens animated modal using Framer Motion
Allows employees to send queries
Form Fields
Name
Email
Employee ID
Subject
Message
Validation Requirements
Implement:

Client-side validation
Server-side validation
Proper error messages
Email format validation
Required field validation
Prevent submission if data is invalid
Backend Requirements
Implement RESTful API endpoints for:

Authentication
Employee CRUD operations
File uploads
Analytics
Notifications
Database Requirements
Use MongoDB or PostgreSQL to store:

Employee records
User accounts
Attendance data
Salary data
Notifications
Logs
Database must support:
Indexing
Optimized queries
Scalability
Data consistency
Email Notification System
Trigger emails for:

Employee registration
Password reset
HR notifications
Contact form submissions
Email must include:
Employee name
Email
Subject
Timestamp
Message details
Use:
Nodemailer
SMTP service or transactional email API
Store credentials securely using environment variables.

Security Requirements
Sanitize all inputs to prevent:

XSS attacks
SQL injection
NoSQL injection
CSRF vulnerabilities
Implement:
Rate limiting
Helmet.js security headers
API request validation
Secure CORS configuration
API Response Requirements
Success Response
Success status
Message
Requested data
Error Response
Error status
Error message
Validation details
UI/UX Requirements
The UI must be:

Fully responsive
Mobile-friendly
Accessible (ARIA labels)
SEO optimized
Fast-loading
Clean and modern
Include:
Dark/light mode
Smooth transitions
Skeleton loaders
Toast notifications
Confirmation dialogs
Performance Optimization
Optimize for:

High traffic scalability
Lazy loading
Code splitting
Reduced bundle size
Efficient database queries
Cached API responses
Ensure the animations do not degrade performance.

File Uploading Requirements
Allow secure upload of:

Employee profile images
Resume PDFs
ID documents
Implement:
File type validation
File size limits
Secure cloud/local storage
Logging and Monitoring
Log:

Authentication activity
Failed login attempts
Employee updates
API failures
Server errors
Use structured logging and monitoring tools.

Documentation Requirements
Provide documentation for:

Folder structure
API routes
Database schema
Environment variables
Authentication flow
Deployment process
Setup instructions
Technology Stack
Frontend
Use:

React or Next.js
Framer Motion
Tailwind CSS
Redux or Context API
Axios
Backend
Use:

Node.js
Express.js
JWT Authentication
bcrypt
Nodemailer
dotenv
Database
Use one of:

MongoDB
PostgreSQL
Optional Enhancements
Include:

Redis caching
Docker containerization
CI/CD pipeline
AWS deployment
Real-time notifications using Socket.io
Expected Output
The final system must provide:

Smooth animated enterprise dashboard
Secure employee management
Responsive modern UI
Role-based authentication
Functional employee CRUD system
Analytics and reporting
Secure contact and notification system
Email notification integration
Production-ready scalable architecture
Proper error handling and logging
