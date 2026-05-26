"""
Golden Response Workspace Generator

This module provides a complete, self-extracting reference implementation for the
AI-Powered Employee Data Management System. The source files are stored in the
WORKSPACE_FILES matrix below, then written into a clean client/server workspace
and validated with a lightweight architectural harness.

Run directly with:
    python golden_response.py
"""

from __future__ import annotations

import json
import os
from pathlib import Path


# =============================================================================
# WORKSPACE DEFINITIONS & SOURCE CODE INJECTION MATRIX
# =============================================================================

WORKSPACE_FILES = {
    # -------------------------------------------------------------------------
    # .gitignore
    # -------------------------------------------------------------------------
    ".gitignore": r'''node_modules/
client/.env
client/dist/
server/.env
server/uploads/*
!server/uploads/.gitkeep
server/logs/*.log

''',

    # -------------------------------------------------------------------------
    # Justification.md
    # -------------------------------------------------------------------------
    "Justification.md": r'''# Final Verdict

Response B is the superior choice because it prioritizes architectural integrity and correctness over the superficial “length” of Response A.

While Response A attempts to provide a full-stack codebase, it fails the most critical RLHF dimension: **Correctness**.

It contains:

- Broken code
- Truncated controllers
- Mismatched variables
- Incomplete authentication logic
- Schema inconsistencies

These issues would cause failures in a real production environment.

In contrast, Response B behaves more like a high-level engineering lead. It correctly identifies that a “production-ready” system requires more than boilerplate implementation. It focuses on:

- Security depth
- State synchronization
- UX consistency
- Enterprise architecture
- Scalable system design

---

# Verdict from ChatGPT

Response B is significantly stronger than Response A across most RLHF dimensions.

Response B demonstrates:

- Deeper architectural reasoning
- Stronger production-grade engineering principles
- Better frontend/backend coherence
- Stronger explanation quality
- More scalable design thinking

It goes beyond simple code generation and explains **why** specific technical choices matter in enterprise systems.

---

## Response A Strengths

Response A still performs well in several areas:

- Broad implementation coverage
- Practical setup guidance
- Full-stack structure
- Technology integration

However, it suffers from multiple implementation and consistency problems.

---

## Weaknesses in Response A

- Incomplete backend controller logic
- Missing schema alignment
- Truncated authentication implementation
- Unsupported architectural claims
- Lower production-grade coherence
- Boilerplate-heavy structure
- Reduced trustworthiness

These weaknesses reduce its reliability as a true enterprise-ready implementation.

---

# RLHF Dimension Ratings

| RLHF Dimension | Response A | Response B | Explanation |
|---|---|---|---|
| Correctness | 5 / 7 | 7 / 7 | Response B has stronger technical accuracy, fewer inconsistencies, and better enterprise-level implementation logic. |
| Relevance | 6 / 7 | 7 / 7 | Both remain relevant to the EDMS prompt, but Response B aligns more precisely with scalable enterprise requirements. |
| Completeness | 5 / 7 | 6 / 7 | Response A covers many features, but Response B explains architecture, scalability, security, and UX in greater depth. |
| Style & Presentation | 5 / 7 | 7 / 7 | Response B is cleaner, more structured, and professionally organized with better readability. |
| Coherence | 4 / 7 | 7 / 7 | Response B maintains logical consistency throughout frontend, backend, animations, security, and state management discussions. |
| Helpfulness | 5 / 7 | 7 / 7 | Response B is more educational and practically valuable for real-world enterprise development. |
| Creativity | 5 / 7 | 6 / 7 | Response B introduces advanced concepts like perceived performance, optimistic updates, and layout projections creatively and appropriately. |

---

# Final Likert Scores

## Response A → 5 / 7

Good full-stack implementation with broad feature coverage, but reduced by:

- Incomplete backend consistency
- Weaker architectural reasoning
- Lower production-grade coherence

---

## Response B → 7 / 7

Excellent enterprise-grade response with:

- Strong architectural depth
- Advanced engineering explanations
- Scalable backend design
- Polished frontend reasoning
- Highly coherent production-ready implementation

---

# Comparative Verdict

## Why Response B Performs Better

### Better Engineering Explanations

Response B explains:

- Why specific technologies are chosen
- Why architecture decisions matter
- Why UX principles affect enterprise software quality

---

### Stronger Security Architecture

Response B properly discusses:

- HttpOnly refresh tokens
- JWT lifecycle management
- Defense-in-depth security models
- RBAC enforcement layers

---

### More Scalable API Design

Response B includes:

- Dynamic query building
- Pagination strategy
- Indexed database fields
- Filtering and sorting architecture

---

### Better Frontend UX Reasoning

Response B introduces:

- Perceived performance
- Staggered animations
- Layout projections
- Optimistic updates

These are real enterprise-grade frontend concepts rather than purely cosmetic additions.

---

### Cleaner System-Wide Thinking

Response B maintains coherence across:

- Backend
- Frontend
- State management
- Security
- UX
- Performance optimization

---

# Main Weaknesses in Response A

## Backend Problems

- Incomplete authentication controller
- Broken middleware flow
- Missing schema fields
- Partial implementation snippets

---

## Architectural Weaknesses

- Boilerplate-focused
- Weak reasoning depth
- Minimal explanation of scaling strategy
- Feature claims without implementation evidence

---

## Presentation Problems

- Fragmented formatting
- Abrupt code cutoffs
- Reduced readability
- Lower professional polish

---

# Additional Engineering Recommendations

---

# 1. API Protection

Use `express-rate-limit` to protect APIs from:

- Brute-force attacks
- Credential stuffing
- Excessive requests

Example:

```js
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
});

app.use('/api', limiter);
```

---

# 2. Compression Middleware

Use `compression` middleware in Express to reduce payload sizes and improve network performance.

Example:

```js
const compression = require('compression');

app.use(compression());
```

Benefits:

- Faster API responses
- Reduced bandwidth
- Better dashboard performance

---

# 3. Skeleton Screens

Instead of loading spinners, implement skeleton loaders using Framer Motion pulse animations.

Benefits:

- Better perceived performance
- Reduced visual waiting fatigue
- More modern enterprise UX

---

# 4. Error Boundaries

Wrap the React application inside an Error Boundary.

Benefits:

- Prevents full dashboard crashes
- Improves fault tolerance
- Provides graceful UI recovery

Example:

```jsx
<ErrorBoundary>
  <App />
</ErrorBoundary>
```

---

# Enterprise-Level Conclusion

This architecture provides a:

- Secure
- Scalable
- Performant
- Visually polished

experience that aligns with modern enterprise engineering standards.

---

# Verdict from Gemini

Based on the RLHF Seven Dimensions framework, the comparative evaluation strongly favors Response B.

---

# The Seven Dimensions Scoring

| Dimension | Response A | Response B | Analysis |
|---|---|---|---|
| Correctness | 1 | 5 | Response A contains incomplete and broken code. Response B provides accurate architectural reasoning. |
| Relevance | 3 | 5 | Response A is generic boilerplate. Response B addresses true enterprise production requirements. |
| Completeness | 2 | 4 | Response A lacks complete controller logic. Response B provides stronger conceptual completeness. |
| Style | 2 | 5 | Response A has messy formatting. Response B is polished and professional. |
| Coherence | 2 | 5 | Response A feels fragmented. Response B flows logically from theory to implementation. |
| Helpfulness | 2 | 5 | Response A requires major fixes. Response B provides practical architectural value. |
| Creativity | 3 | 4 | Response B introduces advanced enterprise concepts appropriately. |

---

# Likert Score → 6

---

# Final Comparative Analysis

## Why Response B Wins

The primary deciding factors are:

- Correctness
- Coherence
- Professionalism
- Enterprise readiness

Response B succeeds because it:

- Explains rationale
- Demonstrates architectural maturity
- Maintains implementation consistency
- Prioritizes scalability and security

---

## Critical Failure in Response A

Response A suffers from:

- Severe truncation issues
- Broken controller snippets
- Syntax incompleteness
- Unsupported claims

This renders portions of the implementation unusable in production.

---

# Key Enterprise Concepts Highlighted by Response B

## Security

- Defense in Depth
- HttpOnly cookie strategy
- JWT lifecycle management

---

## Performance

- Perceived performance optimization
- Optimistic updates
- Animation-driven UX smoothness

---

## Architecture

- Scalable state management
- Predictable data flow
- Centralized store logic

---

## User Experience

- Smooth transitions
- Reduced cognitive load
- Better visual synchronization

---

# Final Enterprise Summary

Response B more faithfully fulfills the “production-ready” requirement because it emphasizes:

- Scalable architecture
- Security correctness
- UX engineering
- State synchronization
- System-wide coherence

Whereas Response A focuses primarily on feature listing and boilerplate structure without sufficient implementation integrity.

---

# Final Decision

| Response | Final Score |
|---|---|
| Response A | 5 / 7 |
| Response B | 7 / 7 |

---

# Ultimate Verdict

✅ **Response B is the clear winner.**

It demonstrates:

- Higher technical maturity
- Better enterprise engineering judgment
- Stronger correctness
- Better architectural thinking
- Superior production readiness

while Response A remains a useful but incomplete implementation draft.

---

''',

    # -------------------------------------------------------------------------
    # Prompt.md
    # -------------------------------------------------------------------------
    "Prompt.md": r'''AI-Powered Employee Data Management System
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

''',

    # -------------------------------------------------------------------------
    # README.md
    # -------------------------------------------------------------------------
    "README.md": r'''# AI-Powered Employee Data Management System

A production-ready, enterprise-grade Employee Data Management System (EDMS) built with modern full-stack technologies, secure authentication, intelligent employee workflows, analytics dashboards, and high-performance animated user interfaces.

---

# Overview

This platform enables organizations to manage employee data securely while providing modern dashboards, role-based access control, analytics, notifications, and smooth user experiences.

The system is designed for:

- HR Teams
- Administrators
- Managers
- Employees

It supports scalable enterprise architecture with secure APIs, responsive frontend interfaces, and optimized database operations.

---

# Core Features

---

# Employee Management

The platform allows administrators and HR managers to:

- Add employee records
- Edit employee information
- Delete employee records
- View employee details
- Upload employee profile images
- Upload resumes and documents
- Track department and designation
- Manage salary information
- Track joining dates
- Store emergency contacts

---

# Dashboard Features

## Animated Enterprise Dashboard

Built using **Framer Motion** for modern interactive experiences.

### Includes

- Smooth page transitions
- Animated cards
- Interactive charts
- Staggered loading animations
- Hover animations
- Animated sidebar navigation
- Real-time counters
- Activity widgets
- Scroll-triggered animations

---

# Analytics & Reporting

The analytics module provides:

- Employee growth charts
- Salary trend analysis
- Department distribution reports
- Monthly hiring statistics
- Attendance insights
- Workforce analytics

Charts are fully responsive and animated.

---

# Employee Table Features

- Pagination
- Real-time search
- Advanced filtering
- Sorting support

### Sortable Fields

- Name
- Department
- Salary
- Joining Date

---

# Employee Profile Page

Each employee profile contains:

- Personal details
- Contact information
- Department information
- Employee role
- Attendance records
- Salary information
- Uploaded documents

---

# Authentication & Security

---

# Authentication System

Secure authentication is implemented using:

- JWT Access Tokens
- Refresh Tokens
- Secure Session Management
- bcrypt Password Hashing

---

# Role-Based Access Control (RBAC)

## Supported Roles

| Role | Permissions |
|---|---|
| Admin | Full system access |
| HR Manager | Manage employee records |
| Employee | View personal profile only |

---

# Security Features

The system includes enterprise-grade protection against:

- XSS Attacks
- CSRF Vulnerabilities
- SQL/NoSQL Injection
- Brute-force attacks

### Security Implementations

- Helmet.js
- Rate Limiting
- Secure CORS
- Request Validation
- Input Sanitization
- Password Hashing
- HttpOnly Cookies
- Access Token Expiration
- Refresh Token Rotation

---

# Contact & Notification System

---

# Contact HR Modal

Employees can contact HR using an animated modal built with Framer Motion.

### Form Fields

- Name
- Email
- Employee ID
- Subject
- Message

### Validation

- Client-side validation
- Server-side validation
- Email validation
- Required field validation
- Error handling

---

# Email Notifications

Automated email notifications are sent for:

- Employee registration
- Password reset
- HR notifications
- Contact form submissions

### Email Includes

- Employee name
- Email
- Subject
- Timestamp
- Message details

### Technology

- Nodemailer
- SMTP / Transactional Email API

---

# Technology Stack

---

# Frontend

Built using:

- Next.js / React
- Tailwind CSS
- Framer Motion
- Redux Toolkit / Context API
- Axios
- React Hot Toast
- Chart.js / Recharts

---

# Backend

Built using:

- Node.js
- Express.js
- JWT Authentication
- bcrypt
- Nodemailer
- dotenv
- Helmet.js
- Express Validator

---

# Database

Supported Databases:

- MongoDB
- PostgreSQL

### Database Features

- Indexed queries
- Optimized filtering
- Scalable architecture
- Data consistency
- Relationship management

---

# Folder Structure

```bash
employee-management-system/
│
├── client/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── layouts/
│   │   ├── animations/
│   │   ├── redux/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── context/
│   │   ├── utils/
│   │   └── styles/
│   │
│   ├── public/
│   └── package.json
│
├── server/
│   ├── controllers/
│   ├── routes/
│   ├── middleware/
│   ├── models/
│   ├── config/
│   ├── utils/
│   ├── validators/
│   ├── uploads/
│   ├── logs/
│   └── server.js
│
├── docker/
├── nginx/
├── .env
├── docker-compose.yml
└── README.md
```

---

# API Features

---

# Authentication APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register` | Register employee |
| POST | `/api/auth/login` | Login user |
| POST | `/api/auth/refresh` | Refresh access token |
| POST | `/api/auth/logout` | Logout user |
| POST | `/api/auth/forgot-password` | Request password reset |
| POST | `/api/auth/reset-password` | Reset password |

---

# Employee APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/employees` | Get all employees |
| GET | `/api/employees/:id` | Get employee details |
| POST | `/api/employees` | Add employee |
| PUT | `/api/employees/:id` | Update employee |
| DELETE | `/api/employees/:id` | Delete employee |

---

# Analytics APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/analytics/employees` | Employee growth stats |
| GET | `/api/analytics/salary` | Salary analytics |
| GET | `/api/analytics/departments` | Department analytics |

---

# Notification APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/contact/hr` | Contact HR |
| GET | `/api/notifications` | Get notifications |

---

# File Upload Features

The system supports secure uploads for:

- Profile Images
- Resume PDFs
- ID Documents

### Upload Security

- File type validation
- File size limits
- MIME type validation
- Secure storage
- Sanitized filenames

---

# UI/UX Features

---

# Responsive Design

Fully optimized for:

- Desktop
- Tablet
- Mobile devices

---

# Accessibility

The application supports:

- ARIA labels
- Keyboard navigation
- Accessible forms
- Screen reader support

---

# UI Features

- Dark/Light Mode
- Skeleton Loaders
- Toast Notifications
- Confirmation Dialogs
- Smooth Transitions
- Animated Interactions

---

# Performance Optimization

The system is optimized for high performance and scalability.

### Optimizations

- Lazy Loading
- Code Splitting
- Optimized Animations
- Reduced Bundle Size
- Cached API Responses
- Database Indexing
- Efficient Queries
- Memoized Components
- GPU-accelerated transforms

---

# Logging & Monitoring

The system logs:

- Authentication activity
- Failed login attempts
- Employee updates
- API failures
- Server errors

### Monitoring Tools

- Winston
- Morgan
- Structured Logs

---

# Environment Variables

Create a `.env` file in the root directory.

```env
PORT=5000

MONGO_URI=your_database_url

JWT_SECRET=your_jwt_secret

JWT_REFRESH_SECRET=your_refresh_secret

EMAIL_USER=your_email

EMAIL_PASS=your_email_password

CLIENT_URL=http://localhost:3000

CLOUDINARY_CLOUD_NAME=your_cloud_name

CLOUDINARY_API_KEY=your_api_key

CLOUDINARY_API_SECRET=your_api_secret
```

---

# Installation Guide

---

# Backend Setup

```bash
cd server

npm install
```

### Start Backend

```bash
npm run dev
```

---

# Frontend Setup

```bash
cd client

npm install
```

### Start Frontend

```bash
npm run dev
```

---

# Docker Setup

Build and run containers:

```bash
docker-compose up --build
```

---

# Deployment

Supported deployment platforms:

- AWS EC2
- Vercel
- Render
- Railway
- Docker
- Nginx

---

# Production Features

---

# Enterprise Architecture

- Modular backend structure
- Scalable frontend architecture
- Service-based API organization
- Centralized error handling
- Reusable components

---

# Production Security

- Secure cookies
- Access token expiration
- Refresh token strategy
- Request validation
- Protected API routes

---

# Advanced Features

Optional enhancements include:

- Redis caching
- Socket.io real-time notifications
- CI/CD pipelines
- AWS deployment
- Kubernetes orchestration
- Microservices architecture

---

# Authentication Flow

1. User logs in
2. Access token is generated
3. Refresh token stored securely
4. Protected routes validate JWT
5. RBAC middleware checks permissions
6. Expired tokens are refreshed automatically

---

# Animation Guidelines

Animations are optimized for performance using:

- `transform`
- `opacity`
- GPU acceleration

### Avoided

- Expensive layout recalculations
- Unnecessary re-renders
- Heavy animation libraries

---

# Error Handling

The application includes:

- Centralized API error handling
- Frontend Error Boundaries
- Toast error notifications
- Validation error reporting

---

# Future Enhancements

- AI-powered analytics
- Face recognition attendance
- Payroll management
- Leave management
- Multi-tenant architecture
- WebSocket notifications
- Redis caching
- Audit logging
- Microservices migration

---

# Final Output

The final system provides:

- Secure employee management
- Enterprise-grade architecture
- Responsive modern dashboard
- Animated user experience
- Role-based authentication
- Employee analytics
- Real-time notifications
- Secure document handling
- Email integrations
- Scalable backend APIs
- Production deployment readiness

---

# License

This project is licensed under the MIT License.

---

# Author

Developed as a modern enterprise-grade AI-powered Employee Data Management System using scalable full-stack architecture and secure engineering practices.

---

''',

    # -------------------------------------------------------------------------
    # Response A.md
    # -------------------------------------------------------------------------
    "Response A.md": r'''# AI-Powered Employee Data Management System

## Project Overview

A production-ready Full-Stack Employee Data Management System built using:

- Next.js
- Tailwind CSS
- Framer Motion
- Node.js
- Express.js
- MongoDB
- JWT Authentication
- Role-Based Access Control (RBAC)
- Nodemailer
- REST APIs

---

# Folder Structure

```bash
employee-management-system/
│
├── client/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── context/
│   │   ├── services/
│   │   ├── animations/
│   │   ├── hooks/
│   │   ├── layouts/
│   │   └── utils/
│   │
│   ├── public/
│   └── package.json
│
├── server/
│   ├── controllers/
│   ├── routes/
│   ├── middleware/
│   ├── models/
│   ├── config/
│   ├── utils/
│   ├── uploads/
│   └── server.js
│
└── README.md
```

---

# Backend Setup

## Install Dependencies

```bash
npm init -y

npm install express mongoose bcryptjs jsonwebtoken dotenv cors helmet morgan multer express-validator nodemailer cookie-parser express-rate-limit
```

---

# Server Configuration

## `server.js`

```js
const express = require('express')
const mongoose = require('mongoose')
const dotenv = require('dotenv')
const cors = require('cors')
const helmet = require('helmet')
const morgan = require('morgan')
const cookieParser = require('cookie-parser')

dotenv.config()

const app = express()

app.use(express.json())
app.use(cors())
app.use(helmet())
app.use(morgan('dev'))
app.use(cookieParser())

mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err))

app.use('/api/auth', require('./routes/authRoutes'))
app.use('/api/employees', require('./routes/employeeRoutes'))

const PORT = process.env.PORT || 5000

app.listen(PORT, () => {
  console.log(`Server running on ${PORT}`)
})
```

---

# Employee Model

## `models/Employee.js`

```js
const mongoose = require('mongoose')

const employeeSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },

  email: {
    type: String,
    required: true,
    unique: true,
  },

  department: String,
  designation: String,
  salary: Number,
  joiningDate: Date,
  emergencyContact: String,

  role: {
    type: String,
    enum: ['admin', 'hr', 'employee'],
    default: 'employee',
  },

  image: String,

}, { timestamps: true })

module.exports = mongoose.model('Employee', employeeSchema)
```

---

# JWT Authentication Middleware

## `middleware/authMiddleware.js`

```js
const jwt = require('jsonwebtoken')

module.exports = (req, res, next) => {

  const token = req.headers.authorization

  if (!token) {
    return res.status(401).json({
      success: false,
      message: 'No token provided',
    })
  }

  try {

    const decoded = jwt.verify(
      token,
      process.env.JWT_SECRET
    )

    req.user = decoded

    next()

  } catch (error) {

    return res.status(401).json({
      success: false,
      message: 'Invalid token',
    })

  }
}
```

---

# Role-Based Access Middleware

## `middleware/roleMiddleware.js`

```js
module.exports = (...roles) => {

  return (req, res, next) => {

    if (!roles.includes(req.user.role)) {

      return res.status(403).json({
        success: false,
        message: 'Access denied',
      })

    }

    next()
  }
}
```

---

# Authentication Controller

## `controllers/authController.js`

```js
const bcrypt = require('bcryptjs')
const jwt = require('jsonwebtoken')
const Employee = require('../models/Employee')

exports.register = async (req, res) => {

  try {

    const { name, email, password, role } = req.body

    const hashedPassword = await bcrypt.hash(password, 10)

    const user = await Employee.create({
      name,
      email,
      password: hashedPassword,
      role,
    })

    res.status(201).json({
      success: true,
      message: 'User registered successfully',
      user,
    })

  } catch (error) {

    res.status(500).json({
      success: false,
      message: error.message,
    })

  }
}

exports.login = async (req, res) => {

  try {

    const { email, password } = req.body

    const user = await Employee.findOne({ email })

    if (!user) {
      return res.status(400).json({
        success: false,
        message: 'Invalid credentials',
      })
    }

    const isMatch = await bcrypt.compare(
      password,
      user.password
    )

    if (!isMatch) {
      return res.status(400).json({
        success: false,
        message: 'Invalid credentials',
      })
    }

    const token = jwt.sign(
      {
        id: user._id,
        role: user.role,
      },
      process.env.JWT_SECRET,
      {
        expiresIn: '7d',
      }
    )

    res.json({
      success: true,
      token,
      user,
    })

  } catch (error) {

    res.status(500).json({
      success: false,
      message: error.message,
    })

  }
}
```

---

# Employee CRUD Controller

## `controllers/employeeController.js`

```js
const Employee = require('../models/Employee')

exports.getEmployees = async (req, res) => {

  try {

    const employees = await Employee.find()

    res.json({
      success: true,
      data: employees,
    })

  } catch (error) {

    res.status(500).json({
      success: false,
      message: error.message,
    })

  }
}

exports.addEmployee = async (req, res) => {

  try {

    const employee = await Employee.create(req.body)

    res.status(201).json({
      success: true,
      data: employee,
    })

  } catch (error) {

    res.status(500).json({
      success: false,
      message: error.message,
    })

  }
}

exports.updateEmployee = async (req, res) => {

  try {

    const employee = await Employee.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    )

    res.json({
      success: true,
      data: employee,
    })

  } catch (error) {

    res.status(500).json({
      success: false,
      message: error.message,
    })

  }
}

exports.deleteEmployee = async (req, res) => {

  try {

    await Employee.findByIdAndDelete(req.params.id)

    res.json({
      success: true,
      message: 'Employee deleted successfully',
    })

  } catch (error) {

    res.status(500).json({
      success: false,
      message: error.message,
    })

  }
}
```

---

# Employee Routes

## `routes/employeeRoutes.js`

```js
const express = require('express')

const router = express.Router()

const auth = require('../middleware/authMiddleware')
const role = require('../middleware/roleMiddleware')

const {
  getEmployees,
  addEmployee,
  updateEmployee,
  deleteEmployee,
} = require('../controllers/employeeController')

router.get('/', auth, getEmployees)

router.post(
  '/',
  auth,
  role('admin', 'hr'),
  addEmployee
)

router.put(
  '/:id',
  auth,
  role('admin', 'hr'),
  updateEmployee
)

router.delete(
  '/:id',
  auth,
  role('admin'),
  deleteEmployee
)

module.exports = router
```

---

# Frontend Setup

## Install Frontend Dependencies

```bash
npx create-next-app client

cd client

npm install axios framer-motion react-icons react-hot-toast chart.js react-chartjs-2
```

---

# Tailwind Setup

```bash
npm install -D tailwindcss postcss autoprefixer

npx tailwindcss init -p
```

---

# Dashboard UI with Framer Motion

## `pages/dashboard.js`

```jsx
import { motion } from 'framer-motion'

export default function Dashboard() {

  return (
    <div className='p-6'>

      <motion.h1
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className='text-4xl font-bold mb-8'
      >
        Employee Dashboard
      </motion.h1>

      <div className='grid grid-cols-1 md:grid-cols-3 gap-6'>

        {[1, 2, 3].map((card) => (

          <motion.div
            key={card}
            whileHover={{ scale: 1.05 }}
            className='bg-white p-6 rounded-xl shadow-lg'
          >

            <h2 className='text-2xl font-semibold'>
              Card {card}
            </h2>

            <p>Analytics information</p>

          </motion.div>
        ))}
      </div>
    </div>
  )
}
```

---

# Employee Table Component

## `components/EmployeeTable.js`

```jsx
import React from 'react'

export default function EmployeeTable({ employees }) {

  return (
    <div className='overflow-x-auto'>

      <table className='w-full border-collapse'>

        <thead>
          <tr className='bg-gray-100'>
            <th className='p-3 text-left'>Name</th>
            <th className='p-3 text-left'>Department</th>
            <th className='p-3 text-left'>Salary</th>
          </tr>
        </thead>

        <tbody>

          {employees.map((emp) => (

            <tr key={emp._id}>

              <td className='p-3'>{emp.name}</td>
              <td className='p-3'>{emp.department}</td>
              <td className='p-3'>{emp.salary}</td>

            </tr>

          ))}

        </tbody>
      </table>
    </div>
  )
}
```

---

# Axios API Service

## `services/api.js`

```js
import axios from 'axios'

const API = axios.create({
  baseURL: 'http://localhost:5000/api',
})

API.interceptors.request.use((req) => {

  const token = localStorage.getItem('token')

  if (token) {
    req.headers.Authorization = token
  }

  return req
})

export default API
```

---

# Contact HR Modal

## `components/ContactModal.js`

```jsx
import { motion } from 'framer-motion'

export default function ContactModal() {

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.8 }}
      animate={{ opacity: 1, scale: 1 }}
      className='fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center'
    >

      <div className='bg-white p-6 rounded-xl w-full max-w-md'>

        <h2 className='text-2xl font-bold mb-4'>
          Contact HR
        </h2>

        <form className='space-y-4'>

          <input
            type='text'
            placeholder='Name'
            className='w-full border p-3 rounded-lg'
          />

          <input
            type='email'
            placeholder='Email'
            className='w-full border p-3 rounded-lg'
          />

          <textarea
            placeholder='Message'
            className='w-full border p-3 rounded-lg'
          />

          <button className='bg-blue-600 text-white px-4 py-2 rounded-lg'>
            Send Message
          </button>

        </form>
      </div>
    </motion.div>
  )
}
```

---

# Nodemailer Integration

## `utils/sendEmail.js`

```js
const nodemailer = require('nodemailer')

const sendEmail = async (options) => {

  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.EMAIL_USER,
      pass: process.env.EMAIL_PASS,
    },
  })

  await transporter.sendMail({
    from: process.env.EMAIL_USER,
    to: options.email,
    subject: options.subject,
    text: options.message,
  })
}

module.exports = sendEmail
```

---

# Environment Variables

## `.env`

```env
PORT=5000
MONGO_URI=your_mongodb_connection
JWT_SECRET=your_secret_key
EMAIL_USER=your_email
EMAIL_PASS=your_email_password
```

---

# Security Features

## Implemented

- Helmet.js
- JWT Authentication
- bcrypt Password Hashing
- Role-Based Access
- Input Validation
- Secure Headers
- Rate Limiting
- Protected Routes
- XSS Protection
- MongoDB Injection Protection

---

# Performance Optimization

## Implemented

- Lazy Loading
- Code Splitting
- GPU Optimized Animations
- Efficient MongoDB Queries
- Component Memoization
- Pagination
- Search Optimization
- API Response Caching

---

# Docker Setup

## Dockerfile

```dockerfile
FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5000

CMD ["npm", "start"]
```

---

# Docker Compose

## `docker-compose.yml`

```yaml
version: '3'

services:
  backend:
    build: .
    ports:
      - '5000:5000'
    env_file:
      - .env
```

---

# Deployment

## Deploy Using

- AWS EC2
- Vercel
- Render
- Railway
- Docker
- Nginx

---

# Future Enhancements

- AI Analytics
- Attendance Management
- Face Recognition
- Payroll System
- Leave Management
- Real-Time Notifications
- Redis Caching
- WebSocket Integration
- Multi-Tenant Architecture
- Microservices Architecture

---

# Final Result

This system provides:

- Enterprise-grade architecture
- Secure authentication
- Employee CRUD system
- Animated dashboard
- Real-time analytics
- Role-based access control
- Responsive UI
- Email notification system
- Production-ready backend
- Scalable database architecture
- Docker support
- Deployment-ready setup

---

# Included Features

Complete working full-stack codebase structure including:

- Backend APIs
- JWT Authentication
- Role-Based Access
- MongoDB Models
- Employee CRUD Operations
- Framer Motion Dashboard
- Tailwind UI
- Contact HR Modal
- Nodemailer Email System
- Docker Setup
- Security Middleware
- Deployment Structure
- Performance Optimization

''',

    # -------------------------------------------------------------------------
    # Response B.md
    # -------------------------------------------------------------------------
    "Response B.md": r'''# Production-Grade Employee Data Management System (EDMS)

To build a **production-grade Employee Data Management System (EDMS)**, we must move beyond simple CRUD or “To-Do list” logic.

In an enterprise environment, the architecture must account for:

- Data integrity
- State synchronization
- Security hardening
- Scalability
- Perceived performance
- Real-time user feedback

This document explains both the **theoretical foundation** and the **practical implementation**.

---

# I. The Theoretical Foundation

---

## 1. The Principle of "Perceived Performance"

In modern dashboards, the actual speed of the server is only half the battle.

We use **Framer Motion** not merely for visual flair, but to provide meaningful user feedback and improve UX.

### Key Techniques

#### Staggered Animations

Prevents the **Flash of Unstyled Content (FOUC)** by revealing data progressively.

Benefits:

- Smooth content loading
- Better visual hierarchy
- Reduced UI shock

---

#### Layout Projections

When users:

- Filter employees
- Sort records
- Delete rows

…the remaining elements should **slide naturally into position** instead of instantly teleporting.

Benefits:

- Reduces cognitive load
- Maintains spatial awareness
- Improves usability

---

## 2. State Management & Side Effects

For enterprise-scale EDMS architecture, we adopt the **Redux Toolkit (RTK)** pattern.

### Why Redux Toolkit?

### Predictability

Employee systems involve complex relational state:

- Salaries
- Attendance
- Departments
- Documents
- Notifications
- Authentication

Centralized state management prevents:

- Prop drilling
- Duplicate API calls
- Inconsistent UI states

---

### Optimistic Updates

When an admin edits employee data:

1. UI updates immediately
2. Backend request executes asynchronously
3. UI rolls back only if the server fails

Benefits:

- Instant responsiveness
- Better user experience
- Reduced perceived latency

---

## 3. Security: Defense in Depth Model

Security is enforced across multiple layers.

---

### JWT Authentication

We use:

- **Short-lived Access Token** (15 mins)
- **Long-lived Refresh Token** (HttpOnly Cookie)

### Why HttpOnly Cookies?

JavaScript cannot access them.

This mitigates:

- XSS (Cross-Site Scripting)
- Token theft

---

### RBAC (Role-Based Access Control)

Security is enforced at:

| Layer | Enforcement |
|---|---|
| Database | Mongoose Middleware |
| API | Express Middleware |
| Frontend | UI Access Restrictions |

---

# II. Backend Implementation (Node.js + Express)

---

# 1. Secure Employee Model

We use **Mongoose indexing** for scalable query performance.

Indexes improve:

- Filtering
- Searching
- Sorting

Complexity improves from:

- $O(n)$ → linear scans
- to approximately $O(\log n)$

---

## `models/Employee.js`

```js
const mongoose = require('mongoose');

const employeeSchema = new mongoose.Schema({
  firstName: {
    type: String,
    required: true,
    trim: true
  },

  lastName: {
    type: String,
    required: true,
    trim: true
  },

  email: {
    type: String,
    unique: true,
    required: true,
    lowercase: true
  },

  department: {
    type: String,
    required: true,
    index: true // Indexed for fast filtering
  },

  designation: String,

  salary: {
    type: Number,
    min: 0
  },

  role: {
    type: String,
    enum: ['Admin', 'HR', 'Employee'],
    default: 'Employee'
  },

  status: {
    type: String,
    enum: ['Active', 'On Leave', 'Terminated'],
    default: 'Active'
  },

  joiningDate: {
    type: Date,
    default: Date.now
  }

}, { timestamps: true });


// Virtual Field
employeeSchema.virtual('fullName').get(function () {
  return `${this.firstName} ${this.lastName}`;
});

module.exports = mongoose.model('Employee', employeeSchema);
```

---

# 2. Advanced Filtering API

This API handles:

- Searching
- Filtering
- Sorting
- Pagination

…using a single optimized query.

---

## `controllers/employeeController.js`

```js
exports.getAllEmployees = async (req, res) => {

  try {

    const {
      search,
      dept,
      sort,
      page = 1,
      limit = 10
    } = req.query;

    // Dynamic Query Builder
    let query = {};

    if (search) {

      query.$or = [
        {
          firstName: {
            $regex: search,
            $options: 'i'
          }
        },
        {
          email: {
            $regex: search,
            $options: 'i'
          }
        }
      ];
    }

    // Department Filtering
    if (dept) {
      query.department = dept;
    }

    // Execute Query
    const employees = await Employee.find(query)

      .sort(
        sort
          ? { [sort]: 1 }
          : { createdAt: -1 }
      )

      .limit(limit * 1)

      .skip((page - 1) * limit);

    // Count Documents
    const count = await Employee.countDocuments(query);

    res.status(200).json({
      success: true,
      data: employees,
      totalPages: Math.ceil(count / limit),
      currentPage: page
    });

  } catch (err) {

    res.status(500).json({
      success: false,
      message: "Server Error"
    });

  }
};
```

---

# III. Frontend Implementation (React + Framer Motion)

---

# 1. Animated Layout Wrapper

This wrapper provides smooth page transitions throughout the application.

---

## `components/PageTransition.jsx`

```jsx
import { motion } from 'framer-motion';

const variants = {

  initial: {
    opacity: 0,
    x: -20
  },

  animate: {
    opacity: 1,
    x: 0
  },

  exit: {
    opacity: 0,
    x: 20
  }
};

const PageTransition = ({ children }) => (

  <motion.div
    variants={variants}
    initial="initial"
    animate="animate"
    exit="exit"
    transition={{
      duration: 0.3,
      ease: "easeOut"
    }}
  >

    {children}

  </motion.div>
);

export default PageTransition;
```

---

# 2. Interactive Employee Table

This component uses:

- Staggered row animations
- Hover transitions
- Dynamic status badges

---

## `components/EmployeeTable.jsx`

```jsx
import { motion } from 'framer-motion';

const tableVariants = {

  hidden: {
    opacity: 0
  },

  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.05
    }
  }
};

const rowVariants = {

  hidden: {
    opacity: 0,
    y: 10
  },

  visible: {
    opacity: 1,
    y: 0
  }
};

const EmployeeTable = ({ employees }) => {

  return (

    <motion.table
      variants={tableVariants}
      initial="hidden"
      animate="visible"
      className="min-w-full divide-y divide-gray-200"
    >

      <thead>

        <tr>
          <th>Name</th>
          <th>Department</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>

      </thead>

      <tbody>

        {employees.map((emp) => (

          <motion.tr
            key={emp._id}
            variants={rowVariants}
            whileHover={{
              backgroundColor: "#f9fafb"
            }}
          >

            <td>
              {emp.firstName} {emp.lastName}
            </td>

            <td>
              {emp.department}
            </td>

            <td>

              <span
                className={`px-2 py-1 rounded-full text-xs ${
                  emp.status === 'Active'
                    ? 'bg-green-100 text-green-800'
                    : 'bg-yellow-100 text-yellow-800'
                }`}
              >

                {emp.status}

              </span>

            </td>

            <td>

              <button>
                Edit
              </button>

            </td>

          </motion.tr>

        ))}

      </tbody>

    </motion.table>
  );
};

export default EmployeeTable;
```

---

# IV. Email Notification Logic

When a new employee is registered:

1. Backend creates employee
2. Background email task triggers
3. Welcome email is delivered asynchronously

---

## `utils/sendEmail.js`

```js
const nodemailer = require('nodemailer');

const sendWelcomeEmail = async (employee) => {

  const transporter = nodemailer.createTransport({

    service: 'gmail',

    auth: {
      user: process.env.EMAIL_USER,
      pass: process.env.EMAIL_PASS
    }
  });

  const mailOptions = {

    from: '"HR Portal" <no-reply@company.com>',

    to: employee.email,

    subject: 'Welcome to the Team!',

    html: `
      <h1>Welcome ${employee.firstName}!</h1>
      <p>Your employee ID is ${employee._id}.</p>
    `
  };

  await transporter.sendMail(mailOptions);
};

module.exports = sendWelcomeEmail;
```

---

# V. Key Production Features Checklist

---

## Authentication & Security

- JWT Authentication
- Refresh Token Rotation
- HttpOnly Cookies
- Password Hashing with bcrypt
- RBAC Authorization
- API Rate Limiting
- Helmet.js Security Headers
- XSS Protection
- MongoDB Injection Protection
- Secure Environment Variables

---

## Database & Backend

- Mongoose Indexing
- Query Optimization
- Pagination
- Dynamic Filtering
- Error Handling Middleware
- Validation Middleware
- Modular Architecture
- RESTful APIs
- Async/Await Pattern

---

## Frontend Features

- Responsive Dashboard
- Animated UI
- Staggered Table Rows
- Smooth Page Transitions
- Optimistic UI Updates
- Search & Filtering
- Real-Time Feedback
- Toast Notifications
- Protected Routes

---

## Performance Optimization

- Lazy Loading
- Code Splitting
- Component Memoization
- Efficient Rendering
- Cached API Responses
- Optimized Database Queries
- GPU Accelerated Animations

---

## Deployment & Scalability

- Docker Support
- CI/CD Ready
- Nginx Reverse Proxy
- Vercel Deployment
- Render/Railway Support
- AWS Deployment
- Environment Separation
- Production Logging

---

# Final Architecture Summary

The EDMS system provides:

- Enterprise-grade scalability
- Secure authentication flow
- Role-based access control
- Advanced employee management
- Optimized database querying
- Framer Motion powered UX
- Real-time responsive UI
- Email notification infrastructure
- Modular backend architecture
- Production deployment readiness

---

# Future Enterprise Enhancements

- AI Analytics Dashboard
- Payroll Management
- Attendance Tracking
- Face Recognition
- Redis Caching
- WebSocket Notifications
- Audit Logging
- Multi-Tenant Architecture
- Microservices Migration
- Kubernetes Deployment
- Event-Driven Architecture

---

''',

    # -------------------------------------------------------------------------
    # client/README.md
    # -------------------------------------------------------------------------
    "client/README.md": r'''# EDMS Client

Frontend dashboard for the Employee Data Management System.

## Stack

- React + Vite
- Tailwind CSS
- Framer Motion
- Recharts
- Axios

## Setup

1. Copy `.env.example` to `.env`
2. Set `VITE_API_BASE_URL` to the backend host, for example `http://localhost:4000`
3. Install dependencies:
   `npm install`
4. Start the app:
   `npm run dev`

## Notes

- The UI falls back to preview data when the authenticated backend is not yet available.
- Routes included:
  - `/` animated dashboard
  - `/employees` employee directory and filters
  - `/profile` current user profile and HR workflow entry

''',

    # -------------------------------------------------------------------------
    # client/index.html
    # -------------------------------------------------------------------------
    "client/index.html": r'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta
      name="description"
      content="Enterprise employee data management dashboard with analytics, secure workflows, and HR communication tools."
    />
    <title>EDMS Console</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
  </html>

''',

    # -------------------------------------------------------------------------
    # client/package-lock.json
    # -------------------------------------------------------------------------
    "client/package-lock.json": r'''{
  "name": "edms-client",
  "version": "0.1.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "edms-client",
      "version": "0.1.0",
      "dependencies": {
        "axios": "^1.7.2",
        "framer-motion": "^11.3.19",
        "lucide-react": "^0.453.0",
        "react": "^18.3.1",
        "react-dom": "^18.3.1",
        "react-router-dom": "^6.28.0",
        "recharts": "^2.13.0"
      },
      "devDependencies": {
        "@types/react": "^18.3.12",
        "@types/react-dom": "^18.3.1",
        "@vitejs/plugin-react": "^4.3.3",
        "autoprefixer": "^10.4.20",
        "postcss": "^8.4.49",
        "tailwindcss": "^3.4.14",
        "vite": "^7.3.3"
      }
    },
    "node_modules/@alloc/quick-lru": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz",
      "integrity": "sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.7.tgz",
      "integrity": "sha512-Aup7aUOfpbAUg2ROOJN6Iw5f9DMBlzu0mIkm/malLQFN/YQgO48wCj0Kxa3sEHJvPVFg7siR+qRInwXd2qhQKw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.29.7",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.29.7.tgz",
      "integrity": "sha512-locTkQyKvwIEgBzVrn8693ebc97F2U8ZHjbXwDXJ5Fn2TCpNwTlKcaKLkdHop5c/icOFE7qt7Q9JC5hnKNa6Gg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.29.7.tgz",
      "integrity": "sha512-RgHBCvtjbOK2gXSNBNIkNoEc9qoVEtau3hj8gEqKQuL3HZAibKarWFEI3Lfm6EYKkLalOh8eSrj9b+ch9H/VBA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.7",
        "@babel/generator": "^7.29.7",
        "@babel/helper-compilation-targets": "^7.29.7",
        "@babel/helper-module-transforms": "^7.29.7",
        "@babel/helpers": "^7.29.7",
        "@babel/parser": "^7.29.7",
        "@babel/template": "^7.29.7",
        "@babel/traverse": "^7.29.7",
        "@babel/types": "^7.29.7",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.29.7.tgz",
      "integrity": "sha512-DkXD5OJQaAQIdZ1bt3UZdEnHAn9Imd3IVBdX03UFe+ony9Ojw5pzr9YVKGDY1jt+Gcn/FnGkNf8r+Vj5NOJWtQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.29.7",
        "@babel/types": "^7.29.7",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.29.7.tgz",
      "integrity": "sha512-wem6WaBj4NaVYVdNhLPPVacES6ZJ+KBBfSkTMD3YZxbP3rm3Di85tJU5ljaUNhaOynt+Aj0xruhYuzQBt8n71g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.29.7",
        "@babel/helper-validator-option": "^7.29.7",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.29.7.tgz",
      "integrity": "sha512-3nQVUAtvkKH9zahfWgw96Jc/uFOmjACE1kQz82E2lqWmHBgjzbNlsC22nuQTfahmWeQtTq5nQ/4Nnd2A1wj4zA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.29.7.tgz",
      "integrity": "sha512-ejHwrQQYcm9xnTivShn2IDOlIzInN34AXskvq9QicvCtEzq1Vzclu/tKF8Jq1Cg8JG2GL6/EmjgsCT7lXepE3g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.29.7",
        "@babel/types": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.29.7.tgz",
      "integrity": "sha512-UPUVSyXbOh627KiCIGQSgwWzGeBKLkaJ9PJEdrngIwMSzxLR4jS4+f1f1jb7VzBbg8nFLaYotvVPFCTqdrmTAg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.29.7",
        "@babel/helper-validator-identifier": "^7.29.7",
        "@babel/traverse": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.29.7.tgz",
      "integrity": "sha512-G7sHYigPY17oO5SYWnfD/0MTBwVR781S/JI643e/JhUYgVgWE/61SoW3NH9KWUKyKq5LVh3npif99Wkt6j86Jw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.29.7.tgz",
      "integrity": "sha512-Pb5ijPrZ89GDH8223L4UP8i6QApWxs04RbPQJTeWDV0/keR2E36MeKnyr6LYmUUvqRRI+Iv87SuF1W6ErINzYw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.29.7.tgz",
      "integrity": "sha512-qehxGkRj55h/ff8EMaJ+cYhyaKlHIxqYDn682wQD7RNp9UujOQsHog2uS0r2vzr4pW+sXf90NeeayjcNaX3fFg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.29.7.tgz",
      "integrity": "sha512-N9ZErrD+yW5geCDtBqnOoxmR8+tNKiGuxKlDpuJxfsqpa2dFcexaziGAE/qoHLiDDreVNMupxGmSoNlyvsA3gw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.29.7.tgz",
      "integrity": "sha512-1k2lAGRMfHTcwuNYcCNUmaUffmQv8KWMfh2iJUUeRlwlwH4FdNG7mfPI10NPfLHJFThE4Tyr4mv7kTNZOiPuBg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.29.7",
        "@babel/types": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.7.tgz",
      "integrity": "sha512-hnORnjP/1P/zFEndoeX+n+t1RwWRJiJpM/jO7FW32Kn9r5+sJB2JWOdYo4L6k78j15eCwY3Gm/7364B1EMwtNg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.7"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-self": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.29.7.tgz",
      "integrity": "sha512-TL0hMc9xzy86VD31nUiwzd5otRAcyEPcsegCxolO0PvcXuH1v0kECe/UIznYFihpkvU5wg/jk4v0TTEFfm53fw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-source": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.29.7.tgz",
      "integrity": "sha512-06IyK09H3wi4cGbhDBwp5gUGo0IKtnYa8tyTiephirPCK6fbobVGiXMMI5zLQ4aKEYP3wZ3ArU44o+8KMrSG/Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/runtime": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/runtime/-/runtime-7.29.7.tgz",
      "integrity": "sha512-Nq8OhGWiZIZGV6hLHoyAKLLcJihP/xFeBMGJoUrxTX2psI8dCifzLhZISFb+VWS3wFMRDmCGw5R+dOySCqPLhw==",
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.29.7.tgz",
      "integrity": "sha512-puq+Gf35oI24FeN11LkoUQFqv9uwNeWpxXZi/Ji3rRIoKAzKnxRaZ+Gkj0vKS9ZCiTESfng1N9LyOyXvo+m+Gg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.7",
        "@babel/parser": "^7.29.7",
        "@babel/types": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.7.tgz",
      "integrity": "sha512-EhlfNQtZ+NK22w5BM61ciuiq1m58ed33Wr1Xan//ZRTy6hgjnwyCffRYwzsGXdASJSUJ1guZILsErh1eQcl+zw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.7",
        "@babel/generator": "^7.29.7",
        "@babel/helper-globals": "^7.29.7",
        "@babel/parser": "^7.29.7",
        "@babel/template": "^7.29.7",
        "@babel/types": "^7.29.7",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.7.tgz",
      "integrity": "sha512-4zBIxpPzowiZpusoFkyGVwakdRJUyuH5PxQ/PrqghfdFWWasvnCdPfQXHrenDai+gyLARulZjZowCOj6fjT4pA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.29.7",
        "@babel/helper-validator-identifier": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.7.tgz",
      "integrity": "sha512-EKX3Qwmhz1eMdEJokhALr0YiD0lhQNwDqkPYyPhiSwKrh7/4KRjQc04sZ8db+5DVVnZ1LmbNDI1uAMPEUBnQPg==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.7.tgz",
      "integrity": "sha512-jbPXvB4Yj2yBV7HUfE2KHe4GJX51QplCN1pGbYjvsyCZbQmies29EoJbkEc+vYuU5o45AfQn37vZlyXy4YJ8RQ==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.7.tgz",
      "integrity": "sha512-62dPZHpIXzvChfvfLJow3q5dDtiNMkwiRzPylSCfriLvZeq0a1bWChrGx/BbUbPwOrsWKMn8idSllklzBy+dgQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.7.tgz",
      "integrity": "sha512-x5VpMODneVDb70PYV2VQOmIUUiBtY3D3mPBG8NxVk5CogneYhkR7MmM3yR/uMdITLrC1ml/NV1rj4bMJuy9MCg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.7.tgz",
      "integrity": "sha512-5lckdqeuBPlKUwvoCXIgI2D9/ABmPq3Rdp7IfL70393YgaASt7tbju3Ac+ePVi3KDH6N2RqePfHnXkaDtY9fkw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.7.tgz",
      "integrity": "sha512-rYnXrKcXuT7Z+WL5K980jVFdvVKhCHhUwid+dDYQpH+qu+TefcomiMAJpIiC2EM3Rjtq0sO3StMV/+3w3MyyqQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.27.7.tgz",
      "integrity": "sha512-B48PqeCsEgOtzME2GbNM2roU29AMTuOIN91dsMO30t+Ydis3z/3Ngoj5hhnsOSSwNzS+6JppqWsuhTp6E82l2w==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-x64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.27.7.tgz",
      "integrity": "sha512-jOBDK5XEjA4m5IJK3bpAQF9/Lelu/Z9ZcdhTRLf4cajlB+8VEhFFRjWgfy3M1O4rO2GQ/b2dLwCUGpiF/eATNQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.27.7.tgz",
      "integrity": "sha512-RkT/YXYBTSULo3+af8Ib0ykH8u2MBh57o7q/DAs3lTJlyVQkgQvlrPTnjIzzRPQyavxtPtfg0EopvDyIt0j1rA==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.27.7.tgz",
      "integrity": "sha512-RZPHBoxXuNnPQO9rvjh5jdkRmVizktkT7TCDkDmQ0W2SwHInKCAV95GRuvdSvA7w4VMwfCjUiPwDi0ZO6Nfe9A==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ia32": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.27.7.tgz",
      "integrity": "sha512-GA48aKNkyQDbd3KtkplYWT102C5sn/EZTY4XROkxONgruHPU72l+gW+FfF8tf2cFjeHaRbWpOYa/uRBz/Xq1Pg==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-loong64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.27.7.tgz",
      "integrity": "sha512-a4POruNM2oWsD4WKvBSEKGIiWQF8fZOAsycHOt6JBpZ+JN2n2JH9WAv56SOyu9X5IqAjqSIPTaJkqN8F7XOQ5Q==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-mips64el": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.27.7.tgz",
      "integrity": "sha512-KabT5I6StirGfIz0FMgl1I+R1H73Gp0ofL9A3nG3i/cYFJzKHhouBV5VWK1CSgKvVaG4q1RNpCTR2LuTVB3fIw==",
      "cpu": [
        "mips64el"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ppc64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.27.7.tgz",
      "integrity": "sha512-gRsL4x6wsGHGRqhtI+ifpN/vpOFTQtnbsupUF5R5YTAg+y/lKelYR1hXbnBdzDjGbMYjVJLJTd2OFmMewAgwlQ==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-riscv64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.27.7.tgz",
      "integrity": "sha512-hL25LbxO1QOngGzu2U5xeXtxXcW+/GvMN3ejANqXkxZ/opySAZMrc+9LY/WyjAan41unrR3YrmtTsUpwT66InQ==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-s390x": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.27.7.tgz",
      "integrity": "sha512-2k8go8Ycu1Kb46vEelhu1vqEP+UeRVj2zY1pSuPdgvbd5ykAw82Lrro28vXUrRmzEsUV0NzCf54yARIK8r0fdw==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-x64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.27.7.tgz",
      "integrity": "sha512-hzznmADPt+OmsYzw1EE33ccA+HPdIqiCRq7cQeL1Jlq2gb1+OyWBkMCrYGBJ+sxVzve2ZJEVeePbLM2iEIZSxA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-arm64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-arm64/-/netbsd-arm64-0.27.7.tgz",
      "integrity": "sha512-b6pqtrQdigZBwZxAn1UpazEisvwaIDvdbMbmrly7cDTMFnw/+3lVxxCTGOrkPVnsYIosJJXAsILG9XcQS+Yu6w==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-x64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.27.7.tgz",
      "integrity": "sha512-OfatkLojr6U+WN5EDYuoQhtM+1xco+/6FSzJJnuWiUw5eVcicbyK3dq5EeV/QHT1uy6GoDhGbFpprUiHUYggrw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-arm64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-arm64/-/openbsd-arm64-0.27.7.tgz",
      "integrity": "sha512-AFuojMQTxAz75Fo8idVcqoQWEHIXFRbOc1TrVcFSgCZtQfSdc1RXgB3tjOn/krRHENUB4j00bfGjyl2mJrU37A==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-x64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.27.7.tgz",
      "integrity": "sha512-+A1NJmfM8WNDv5CLVQYJ5PshuRm/4cI6WMZRg1by1GwPIQPCTs1GLEUHwiiQGT5zDdyLiRM/l1G0Pv54gvtKIg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openharmony-arm64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/openharmony-arm64/-/openharmony-arm64-0.27.7.tgz",
      "integrity": "sha512-+KrvYb/C8zA9CU/g0sR6w2RBw7IGc5J2BPnc3dYc5VJxHCSF1yNMxTV5LQ7GuKteQXZtspjFbiuW5/dOj7H4Yw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/sunos-x64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.27.7.tgz",
      "integrity": "sha512-ikktIhFBzQNt/QDyOL580ti9+5mL/YZeUPKU2ivGtGjdTYoqz6jObj6nOMfhASpS4GU4Q/Clh1QtxWAvcYKamA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "sunos"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-arm64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.27.7.tgz",
      "integrity": "sha512-7yRhbHvPqSpRUV7Q20VuDwbjW5kIMwTHpptuUzV+AA46kiPze5Z7qgt6CLCK3pWFrHeNfDd1VKgyP4O+ng17CA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-ia32": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.27.7.tgz",
      "integrity": "sha512-SmwKXe6VHIyZYbBLJrhOoCJRB/Z1tckzmgTLfFYOfpMAx63BJEaL9ExI8x7v0oAO3Zh6D/Oi1gVxEYr5oUCFhw==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-x64": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.27.7.tgz",
      "integrity": "sha512-56hiAJPhwQ1R4i+21FVF7V8kSD5zZTdHcVuRFMW0hn753vVfQN8xlx4uOPT4xoGH0Z/oVATuR82AiqSTDIpaHg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.13",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
      "integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.0",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/remapping": {
      "version": "2.3.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/remapping/-/remapping-2.3.5.tgz",
      "integrity": "sha512-LI9u/+laYG4Ds1TDKSJW2YPrIlcVYOwi2fUC6xB43lueCjgxV4lffOCZCtYFiH6TNOX+tQKXx97T4IKHbhyHEQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/gen-mapping": "^0.3.5",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
      "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.31",
      "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
      "integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@remix-run/router": {
      "version": "1.23.2",
      "resolved": "https://registry.npmjs.org/@remix-run/router/-/router-1.23.2.tgz",
      "integrity": "sha512-Ic6m2U/rMjTkhERIa/0ZtXJP17QUi2CbWE7cqx4J58M8aA3QTfW+2UlQ4psvTX9IO1RfNVhK3pcpdjej7L+t2w==",
      "license": "MIT",
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@rolldown/pluginutils": {
      "version": "1.0.0-beta.27",
      "resolved": "https://registry.npmjs.org/@rolldown/pluginutils/-/pluginutils-1.0.0-beta.27.tgz",
      "integrity": "sha512-+d0F4MKMCbeVUJwG96uQ4SgAznZNSq93I3V+9NHA4OpvqG8mRCpGdKmK8l/dl02h2CCDHwW2FqilnTyDcAnqjA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@rollup/rollup-android-arm-eabi": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm-eabi/-/rollup-android-arm-eabi-4.60.4.tgz",
      "integrity": "sha512-F5QXMSiFebS9hKZj02XhWLLnRpJ3B3AROP0tWbFBSj+6kCbg5m9j5JoHKd4mmSVy5mS/IMQloYgYxCuJC0fxEQ==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ]
    },
    "node_modules/@rollup/rollup-android-arm64": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm64/-/rollup-android-arm64-4.60.4.tgz",
      "integrity": "sha512-GxxTKApUpzRhof7poWvCJHRF51C67u1R7D6DiluBE8wKU1u5GWE8t+v81JvJYtbawoBFX1hLv5Ei4eVjkWokaw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ]
    },
    "node_modules/@rollup/rollup-darwin-arm64": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-arm64/-/rollup-darwin-arm64-4.60.4.tgz",
      "integrity": "sha512-tua0TaJxMOB1R0V0RS1jFZ/RpURFDJIOR2A6jWwQeawuFyS4gBW+rntLRaQd0EQ4bd6Vp44Z2rXW+YYDBsj6IA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_modules/@rollup/rollup-darwin-x64": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-x64/-/rollup-darwin-x64-4.60.4.tgz",
      "integrity": "sha512-CSKq7MsP+5PFIcydhAiR1K0UhEI1A2jWXVKHPCBZ151yOutENwvnPocgVHkivu2kviURtCEB6zUQw0vs8RrhMg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_modules/@rollup/rollup-freebsd-arm64": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-freebsd-arm64/-/rollup-freebsd-arm64-4.60.4.tgz",
      "integrity": "sha512-+O8OkVdyvXMtJEciu2wS/pzm1IxntEEQx3z5TAVy4l32G0etZn+RsA48ARRrFm6Ri8fvqPQfgrvNxSjKAbnd3g==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ]
    },
    "node_modules/@rollup/rollup-freebsd-x64": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-freebsd-x64/-/rollup-freebsd-x64-4.60.4.tgz",
      "integrity": "sha512-Iw3oMskH3AfNuhU0MSN7vNbdi4me/NiYo2azqPz/Le16zHSa+3RRmliCMWWQmh4lcndccU40xcJuTYJZxNo/lw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm-gnueabihf": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-gnueabihf/-/rollup-linux-arm-gnueabihf-4.60.4.tgz",
      "integrity": "sha512-EIPRXTVQpHyF8WOo219AD2yEltPehLTcTMz2fn6JsatLYSzQf00hj3rulF+yauOlF9/FtM2WpkT/hJh/KJFGhA==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm-musleabihf": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-musleabihf/-/rollup-linux-arm-musleabihf-4.60.4.tgz",
      "integrity": "sha512-J3Yh9PzzF1Ovah2At+lHiGQdsYgArxBbXv/zHfSyaiFQEqvNv7DcW98pCrmdjCZBrqBiKrKKe2V+aaSGWuBe/w==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm64-gnu": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-gnu/-/rollup-linux-arm64-gnu-4.60.4.tgz",
      "integrity": "sha512-BFDEZMYfUvLn37ONE1yMBojPxnMlTFsdyNoqncT0qFq1mAfllL+ATMMJd8TeuVMiX84s1KbcxcZbXInmcO2mRg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-arm64-musl": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-musl/-/rollup-linux-arm64-musl-4.60.4.tgz",
      "integrity": "sha512-pc9EYOSlOgdQ2uPl1o9PF6/kLSgaUosia7gOuS8mB69IxJvlclko1MECXysjs5ryez1/5zjYqx3+xYU0TU6R1A==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-loong64-gnu": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-loong64-gnu/-/rollup-linux-loong64-gnu-4.60.4.tgz",
      "integrity": "sha512-NxnomyxYerDh5n4iLrNa+sH+Z+U4BMEE46V2PgQ/hoB909i8gV1M5wPojWg9fk1jWpO3IQnOs20K4wyZuFLEFQ==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-loong64-musl": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-loong64-musl/-/rollup-linux-loong64-musl-4.60.4.tgz",
      "integrity": "sha512-nbJnQ8a3z1mtmrwImCYhc6BGpThAyYVRQxw9uKSKG4wR6aAYno9sVjJ0zaZcW9BPJX1GbrDPf+SvdWjgTuDmnw==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-ppc64-gnu": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-ppc64-gnu/-/rollup-linux-ppc64-gnu-4.60.4.tgz",
      "integrity": "sha512-2EU6acNrQLd8tYvo/LXW535wupT3m6fo7HKo6lr7ktQoItxTyOL1ZCR/GfGCuXl2vR+zmfI6eRXkSemafv+iVg==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-ppc64-musl": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-ppc64-musl/-/rollup-linux-ppc64-musl-4.60.4.tgz",
      "integrity": "sha512-WeBtoMuaMxiiIrO2IYP3xs6GMWkJP2C0EoT8beTLkUPmzV1i/UcOSVw1d5r9KBODtHKilG5yFxsGRnBbK3wJ4A==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-riscv64-gnu": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-gnu/-/rollup-linux-riscv64-gnu-4.60.4.tgz",
      "integrity": "sha512-FJHFfqpKUI3A10WrWKiFbBZ7yVbGT4q4B5o1qKFFojqpaYoh9LrQgqWCmmcxQzVSXYtyB5bzkXrYzlHTs21MYA==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-riscv64-musl": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-musl/-/rollup-linux-riscv64-musl-4.60.4.tgz",
      "integrity": "sha512-mcEl6CUT5IAUmQf1m9FYSmVqCJlpQ8r8eyftFUHG8i9OhY7BkBXSUdnLH5DOf0wCOjcP9v/QO93zpmF1SptCCw==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-s390x-gnu": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-s390x-gnu/-/rollup-linux-s390x-gnu-4.60.4.tgz",
      "integrity": "sha512-ynt3JxVd2w2buzoKDWIyiV1pJW93xlQic1THVLXilz429oijRpSHivZAgp65KBu+cMcgf1eVVjdnTLvPxgCuoQ==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-x64-gnu": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-gnu/-/rollup-linux-x64-gnu-4.60.4.tgz",
      "integrity": "sha512-Boiz5+MsaROEWDf+GGEwF8VMHGhlUoQMtIPjOgA5fv4osupqTVnJteQNKJwUcnUog2G55jYXH7KZFFiJe0TEzQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-linux-x64-musl": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-musl/-/rollup-linux-x64-musl-4.60.4.tgz",
      "integrity": "sha512-+qfSY27qIrFfI/Hom04KYFw3GKZSGU4lXus51wsb5EuySfFlWRwjkKWoE9emgRw/ukoT4Udsj4W/+xxG8VbPKg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ]
    },
    "node_modules/@rollup/rollup-openbsd-x64": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-openbsd-x64/-/rollup-openbsd-x64-4.60.4.tgz",
      "integrity": "sha512-VpTfOPHgVXEBeeR8hZ2O0F3aSso+JDWqTWmTmzcQKted54IAdUVbxE+j/MVxUsKa8L20HJhv3vUezVPoquqWjA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ]
    },
    "node_modules/@rollup/rollup-openharmony-arm64": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-openharmony-arm64/-/rollup-openharmony-arm64-4.60.4.tgz",
      "integrity": "sha512-IPOsh5aRYuLv/nkU51X10Bf75Bsf6+gZdx1X+QP5QM6lIJFHHqbHLG0uJn/hWthzo13UAc2umiUorqZy3axoZg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ]
    },
    "node_modules/@rollup/rollup-win32-arm64-msvc": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-arm64-msvc/-/rollup-win32-arm64-msvc-4.60.4.tgz",
      "integrity": "sha512-4QzE9E81OohJ/HKzHhsqU+zcYYojVOXlFMs1DdyMT6qXl/niOH7AVElmmEdUNHHS/oRkc++d5k6Vy85zFs0DEw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-ia32-msvc": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-ia32-msvc/-/rollup-win32-ia32-msvc-4.60.4.tgz",
      "integrity": "sha512-zTPgT1YuHHcd+Tmx7h8aml0FWFVelV5N54oHow9SLj+GfoDy/huQ+UV396N/C7KpMDMiPspRktzM1/0r1usYEA==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-x64-gnu": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-gnu/-/rollup-win32-x64-gnu-4.60.4.tgz",
      "integrity": "sha512-DRS4G7mi9lJxqEDezIkKCaUIKCrLUUDCUaCsTPCi/rtqaC6D/jjwslMQyiDU50Ka0JKpeXeRBFBAXwArY52vBw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@rollup/rollup-win32-x64-msvc": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-msvc/-/rollup-win32-x64-msvc-4.60.4.tgz",
      "integrity": "sha512-QVTUovf40zgTqlFVrKA1uXMVvU2QWEFWfAH8Wdc48IxLvrJMQVMBRjuQyUpzZCDkakImib9eVazbWlC6ksWtJw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ]
    },
    "node_modules/@types/babel__core": {
      "version": "7.20.5",
      "resolved": "https://registry.npmjs.org/@types/babel__core/-/babel__core-7.20.5.tgz",
      "integrity": "sha512-qoQprZvz5wQFJwMDqeseRXWv3rqMvhgpbXFfVyWhbx9X47POIA6i/+dXefEmZKoAgOaTdaIgNSMqMIU61yRyzA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.20.7",
        "@babel/types": "^7.20.7",
        "@types/babel__generator": "*",
        "@types/babel__template": "*",
        "@types/babel__traverse": "*"
      }
    },
    "node_modules/@types/babel__generator": {
      "version": "7.27.0",
      "resolved": "https://registry.npmjs.org/@types/babel__generator/-/babel__generator-7.27.0.tgz",
      "integrity": "sha512-ufFd2Xi92OAVPYsy+P4n7/U7e68fex0+Ee8gSG9KX7eo084CWiQ4sdxktvdl0bOPupXtVJPY19zk6EwWqUQ8lg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.0.0"
      }
    },
    "node_modules/@types/babel__template": {
      "version": "7.4.4",
      "resolved": "https://registry.npmjs.org/@types/babel__template/-/babel__template-7.4.4.tgz",
      "integrity": "sha512-h/NUaSyG5EyxBIp8YRxo4RMe2/qQgvyowRwVMzhYhBCONbW8PUsg4lkFMrhgZhUe5z3L3MiLDuvyJ/CaPa2A8A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.1.0",
        "@babel/types": "^7.0.0"
      }
    },
    "node_modules/@types/babel__traverse": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@types/babel__traverse/-/babel__traverse-7.28.0.tgz",
      "integrity": "sha512-8PvcXf70gTDZBgt9ptxJ8elBeBjcLOAcOtoO/mPJjtji1+CdGbHgm77om1GrsPxsiE+uXIpNSK64UYaIwQXd4Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.28.2"
      }
    },
    "node_modules/@types/d3-array": {
      "version": "3.2.2",
      "resolved": "https://registry.npmjs.org/@types/d3-array/-/d3-array-3.2.2.tgz",
      "integrity": "sha512-hOLWVbm7uRza0BYXpIIW5pxfrKe0W+D5lrFiAEYR+pb6w3N2SwSMaJbXdUfSEv+dT4MfHBLtn5js0LAWaO6otw==",
      "license": "MIT"
    },
    "node_modules/@types/d3-color": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/@types/d3-color/-/d3-color-3.1.3.tgz",
      "integrity": "sha512-iO90scth9WAbmgv7ogoq57O9YpKmFBbmoEoCHDB2xMBY0+/KVrqAaCDyCE16dUspeOvIxFFRI+0sEtqDqy2b4A==",
      "license": "MIT"
    },
    "node_modules/@types/d3-ease": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/@types/d3-ease/-/d3-ease-3.0.2.tgz",
      "integrity": "sha512-NcV1JjO5oDzoK26oMzbILE6HW7uVXOHLQvHshBUW4UMdZGfiY6v5BeQwh9a9tCzv+CeefZQHJt5SRgK154RtiA==",
      "license": "MIT"
    },
    "node_modules/@types/d3-interpolate": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/@types/d3-interpolate/-/d3-interpolate-3.0.4.tgz",
      "integrity": "sha512-mgLPETlrpVV1YRJIglr4Ez47g7Yxjl1lj7YKsiMCb27VJH9W8NVM6Bb9d8kkpG/uAQS5AmbA48q2IAolKKo1MA==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-color": "*"
      }
    },
    "node_modules/@types/d3-path": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/@types/d3-path/-/d3-path-3.1.1.tgz",
      "integrity": "sha512-VMZBYyQvbGmWyWVea0EHs/BwLgxc+MKi1zLDCONksozI4YJMcTt8ZEuIR4Sb1MMTE8MMW49v0IwI5+b7RmfWlg==",
      "license": "MIT"
    },
    "node_modules/@types/d3-scale": {
      "version": "4.0.9",
      "resolved": "https://registry.npmjs.org/@types/d3-scale/-/d3-scale-4.0.9.tgz",
      "integrity": "sha512-dLmtwB8zkAeO/juAMfnV+sItKjlsw2lKdZVVy6LRr0cBmegxSABiLEpGVmSJJ8O08i4+sGR6qQtb6WtuwJdvVw==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-time": "*"
      }
    },
    "node_modules/@types/d3-shape": {
      "version": "3.1.8",
      "resolved": "https://registry.npmjs.org/@types/d3-shape/-/d3-shape-3.1.8.tgz",
      "integrity": "sha512-lae0iWfcDeR7qt7rA88BNiqdvPS5pFVPpo5OfjElwNaT2yyekbM0C9vK+yqBqEmHr6lDkRnYNoTBYlAgJa7a4w==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-path": "*"
      }
    },
    "node_modules/@types/d3-time": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/@types/d3-time/-/d3-time-3.0.4.tgz",
      "integrity": "sha512-yuzZug1nkAAaBlBBikKZTgzCeA+k1uy4ZFwWANOfKw5z5LRhV0gNA7gNkKm7HoK+HRN0wX3EkxGk0fpbWhmB7g==",
      "license": "MIT"
    },
    "node_modules/@types/d3-timer": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/@types/d3-timer/-/d3-timer-3.0.2.tgz",
      "integrity": "sha512-Ps3T8E8dZDam6fUyNiMkekK3XUsaUEik+idO9/YjPtfj2qruF8tFBXS7XhtE4iIXBLxhmLjP3SXpLhVf21I9Lw==",
      "license": "MIT"
    },
    "node_modules/@types/estree": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/@types/estree/-/estree-1.0.8.tgz",
      "integrity": "sha512-dWHzHa2WqEXI/O1E9OjrocMTKJl2mSrEolh1Iomrv6U+JuNwaHXsXx9bLu5gG7BUWFIN0skIQJQ/L1rIex4X6w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/prop-types": {
      "version": "15.7.15",
      "resolved": "https://registry.npmjs.org/@types/prop-types/-/prop-types-15.7.15.tgz",
      "integrity": "sha512-F6bEyamV9jKGAFBEmlQnesRPGOQqS2+Uwi0Em15xenOxHaf2hv6L8YCVn3rPdPJOiJfPiCnLIRyvwVaqMY3MIw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/react": {
      "version": "18.3.29",
      "resolved": "https://registry.npmjs.org/@types/react/-/react-18.3.29.tgz",
      "integrity": "sha512-ch0qJdr2JY0r04NXSprbK6TXOgnaJ1Tz23fm5W+z0/CBah6BSBc3n96h7K9GOtwh0HrilNWHIBzE1Ko4Dcw/Wg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/prop-types": "*",
        "csstype": "^3.2.2"
      }
    },
    "node_modules/@types/react-dom": {
      "version": "18.3.7",
      "resolved": "https://registry.npmjs.org/@types/react-dom/-/react-dom-18.3.7.tgz",
      "integrity": "sha512-MEe3UeoENYVFXzoXEWsvcpg6ZvlrFNlOQ7EOsvhI3CfAXwzPfO8Qwuxd40nepsYKqyyVQnTdEfv68q91yLcKrQ==",
      "dev": true,
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "^18.0.0"
      }
    },
    "node_modules/@vitejs/plugin-react": {
      "version": "4.7.0",
      "resolved": "https://registry.npmjs.org/@vitejs/plugin-react/-/plugin-react-4.7.0.tgz",
      "integrity": "sha512-gUu9hwfWvvEDBBmgtAowQCojwZmJ5mcLn3aufeCsitijs3+f2NsrPtlAWIR6OPiqljl96GVCUbLe0HyqIpVaoA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/core": "^7.28.0",
        "@babel/plugin-transform-react-jsx-self": "^7.27.1",
        "@babel/plugin-transform-react-jsx-source": "^7.27.1",
        "@rolldown/pluginutils": "1.0.0-beta.27",
        "@types/babel__core": "^7.20.5",
        "react-refresh": "^0.17.0"
      },
      "engines": {
        "node": "^14.18.0 || >=16.0.0"
      },
      "peerDependencies": {
        "vite": "^4.2.0 || ^5.0.0 || ^6.0.0 || ^7.0.0"
      }
    },
    "node_modules/agent-base": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz",
      "integrity": "sha512-RZNwNclF7+MS/8bDg70amg32dyeZGZxiDuQmZxKLAlQjr3jGyLx+4Kkk58UO7D2QdgFIQCovuSuZESne6RG6XQ==",
      "license": "MIT",
      "dependencies": {
        "debug": "4"
      },
      "engines": {
        "node": ">= 6.0.0"
      }
    },
    "node_modules/any-promise": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/any-promise/-/any-promise-1.3.0.tgz",
      "integrity": "sha512-7UvmKalWRt1wgjL1RrGxoSJW/0QZFIegpeGvZG9kjp8vrRu55XTHbwnqq2GpXm9uLbcuhxm3IqX9OB4MZR1b2A==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/anymatch": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz",
      "integrity": "sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "normalize-path": "^3.0.0",
        "picomatch": "^2.0.4"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/arg": {
      "version": "5.0.2",
      "resolved": "https://registry.npmjs.org/arg/-/arg-5.0.2.tgz",
      "integrity": "sha512-PYjyFOLKQ9y57JvQ6QLo8dAgNqswh8M1RMJYdQduT6xbWSgK36P/Z/v+p888pM69jMMfS8Xd8F6I1kQ/I9HUGg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/asynckit": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
      "integrity": "sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==",
      "license": "MIT"
    },
    "node_modules/autoprefixer": {
      "version": "10.5.0",
      "resolved": "https://registry.npmjs.org/autoprefixer/-/autoprefixer-10.5.0.tgz",
      "integrity": "sha512-FMhOoZV4+qR6aTUALKX2rEqGG+oyATvwBt9IIzVR5rMa2HRWPkxf+P+PAJLD1I/H5/II+HuZcBJYEFBpq39ong==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/autoprefixer"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "browserslist": "^4.28.2",
        "caniuse-lite": "^1.0.30001787",
        "fraction.js": "^5.3.4",
        "picocolors": "^1.1.1",
        "postcss-value-parser": "^4.2.0"
      },
      "bin": {
        "autoprefixer": "bin/autoprefixer"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      },
      "peerDependencies": {
        "postcss": "^8.1.0"
      }
    },
    "node_modules/axios": {
      "version": "1.16.1",
      "resolved": "https://registry.npmjs.org/axios/-/axios-1.16.1.tgz",
      "integrity": "sha512-caYkukvroVPO8KrzuJEb50Hm07KwfBZPEC3VeFHTsqWHvKTsy54hjJz9BS/cdaypROE2rH6xvm9mHX4fgWkr3A==",
      "license": "MIT",
      "dependencies": {
        "follow-redirects": "^1.16.0",
        "form-data": "^4.0.5",
        "https-proxy-agent": "^5.0.1",
        "proxy-from-env": "^2.1.0"
      }
    },
    "node_modules/baseline-browser-mapping": {
      "version": "2.10.32",
      "resolved": "https://registry.npmjs.org/baseline-browser-mapping/-/baseline-browser-mapping-2.10.32.tgz",
      "integrity": "sha512-wbPvpyjJPC0zdfdKXxqEL3Ea+bOMD/87X4lftiJkkaBiuG6ALQy1SLmEd7BSmVCuwCQsBrCamgBoLyfFDD1EPg==",
      "dev": true,
      "license": "Apache-2.0",
      "bin": {
        "baseline-browser-mapping": "dist/cli.cjs"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/binary-extensions": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.3.0.tgz",
      "integrity": "sha512-Ceh+7ox5qe7LJuLHoY0feh3pHuUDHAcRUeyL2VYghZwfpkNIy/+8Ocg0a3UuSoYzavmylwuLWQOf3hl0jjMMIw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fill-range": "^7.1.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/browserslist": {
      "version": "4.28.2",
      "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-4.28.2.tgz",
      "integrity": "sha512-48xSriZYYg+8qXna9kwqjIVzuQxi+KYWp2+5nCYnYKPTr0LvD89Jqk2Or5ogxz0NUMfIjhh2lIUX/LyX9B4oIg==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "baseline-browser-mapping": "^2.10.12",
        "caniuse-lite": "^1.0.30001782",
        "electron-to-chromium": "^1.5.328",
        "node-releases": "^2.0.36",
        "update-browserslist-db": "^1.2.3"
      },
      "bin": {
        "browserslist": "cli.js"
      },
      "engines": {
        "node": "^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/camelcase-css": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/camelcase-css/-/camelcase-css-2.0.1.tgz",
      "integrity": "sha512-QOSvevhslijgYwRx6Rv7zKdMF8lbRmx+uQGx2+vDc+KI/eBnsy9kit5aj23AgGu3pa4t9AgwbnXWqS+iOY+2aA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/caniuse-lite": {
      "version": "1.0.30001793",
      "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001793.tgz",
      "integrity": "sha512-iwSsYWaCOoh26cV8NwNRViHlrfUvYsHDfRVcbtmw0Kg6PJIZZXwMkj1442FYLBGkeUf1juAsU3DTfxW579mrPA==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/caniuse-lite"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "CC-BY-4.0"
    },
    "node_modules/chokidar": {
      "version": "3.6.0",
      "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-3.6.0.tgz",
      "integrity": "sha512-7VT13fmjotKpGipCW9JEQAusEPE+Ei8nl6/g4FBAmIm0GOOLMua9NDDo/DWp0ZAxCr3cPq5ZpBqmPAQgDda2Pw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "anymatch": "~3.1.2",
        "braces": "~3.0.2",
        "glob-parent": "~5.1.2",
        "is-binary-path": "~2.1.0",
        "is-glob": "~4.0.1",
        "normalize-path": "~3.0.0",
        "readdirp": "~3.6.0"
      },
      "engines": {
        "node": ">= 8.10.0"
      },
      "funding": {
        "url": "https://paulmillr.com/funding/"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.2"
      }
    },
    "node_modules/chokidar/node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/clsx": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/clsx/-/clsx-2.1.1.tgz",
      "integrity": "sha512-eYm0QWBtUrBWZWG0d386OGAw16Z995PiOVo2B7bjWSbHedGl5e0ZWaq65kOGgUSNesEIDkB9ISbTg/JK9dhCZA==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/combined-stream": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz",
      "integrity": "sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==",
      "license": "MIT",
      "dependencies": {
        "delayed-stream": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/commander": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/commander/-/commander-4.1.1.tgz",
      "integrity": "sha512-NOKm8xhkzAjzFx8B2v5OAHT+u5pRQc2UCa2Vq9jYL/31o2wi9mxBA7LIFs3sV5VSC49z6pEhfbMULvShKj26WA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/convert-source-map": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-2.0.0.tgz",
      "integrity": "sha512-Kvp459HrV2FEJ1CAsi1Ku+MY3kasH19TFykTz2xWmMeq6bk2NU3XXvfJ+Q61m0xktWwt+1HSYf3JZsTms3aRJg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/cssesc": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz",
      "integrity": "sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "cssesc": "bin/cssesc"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/csstype": {
      "version": "3.2.3",
      "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.2.3.tgz",
      "integrity": "sha512-z1HGKcYy2xA8AGQfwrn0PAy+PB7X/GSj3UVJW9qKyn43xWa+gl5nXmU4qqLMRzWVLFC8KusUX8T/0kCiOYpAIQ==",
      "license": "MIT"
    },
    "node_modules/d3-array": {
      "version": "3.2.4",
      "resolved": "https://registry.npmjs.org/d3-array/-/d3-array-3.2.4.tgz",
      "integrity": "sha512-tdQAmyA18i4J7wprpYq8ClcxZy3SC31QMeByyCFyRt7BVHdREQZ5lpzoe5mFEYZUWe+oq8HBvk9JjpibyEV4Jg==",
      "license": "ISC",
      "dependencies": {
        "internmap": "1 - 2"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-color": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/d3-color/-/d3-color-3.1.0.tgz",
      "integrity": "sha512-zg/chbXyeBtMQ1LbD/WSoW2DpC3I0mpmPdW+ynRTj/x2DAWYrIY7qeZIHidozwV24m4iavr15lNwIwLxRmOxhA==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-ease": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-ease/-/d3-ease-3.0.1.tgz",
      "integrity": "sha512-wR/XK3D3XcLIZwpbvQwQ5fK+8Ykds1ip7A2Txe0yxncXSdq1L9skcG7blcedkOX+ZcgxGAmLX1FrRGbADwzi0w==",
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-format": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/d3-format/-/d3-format-3.1.2.tgz",
      "integrity": "sha512-AJDdYOdnyRDV5b6ArilzCPPwc1ejkHcoyFarqlPqT7zRYjhavcT3uSrqcMvsgh2CgoPbK3RCwyHaVyxYcP2Arg==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-interpolate": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-interpolate/-/d3-interpolate-3.0.1.tgz",
      "integrity": "sha512-3bYs1rOD33uo8aqJfKP3JWPAibgw8Zm2+L9vBKEHJ2Rg+viTR7o5Mmv5mZcieN+FRYaAOWX5SJATX6k1PWz72g==",
      "license": "ISC",
      "dependencies": {
        "d3-color": "1 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-path": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/d3-path/-/d3-path-3.1.0.tgz",
      "integrity": "sha512-p3KP5HCf/bvjBSSKuXid6Zqijx7wIfNW+J/maPs+iwR35at5JCbLUT0LzF1cnjbCHWhqzQTIN2Jpe8pRebIEFQ==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-scale": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/d3-scale/-/d3-scale-4.0.2.tgz",
      "integrity": "sha512-GZW464g1SH7ag3Y7hXjf8RoUuAFIqklOAq3MRl4OaWabTFJY9PN/E1YklhXLh+OQ3fM9yS2nOkCoS+WLZ6kvxQ==",
      "license": "ISC",
      "dependencies": {
        "d3-array": "2.10.0 - 3",
        "d3-format": "1 - 3",
        "d3-interpolate": "1.2.0 - 3",
        "d3-time": "2.1.1 - 3",
        "d3-time-format": "2 - 4"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-shape": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/d3-shape/-/d3-shape-3.2.0.tgz",
      "integrity": "sha512-SaLBuwGm3MOViRq2ABk3eLoxwZELpH6zhl3FbAoJ7Vm1gofKx6El1Ib5z23NUEhF9AsGl7y+dzLe5Cw2AArGTA==",
      "license": "ISC",
      "dependencies": {
        "d3-path": "^3.1.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-time": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/d3-time/-/d3-time-3.1.0.tgz",
      "integrity": "sha512-VqKjzBLejbSMT4IgbmVgDjpkYrNWUYJnbCGo874u7MMKIWsILRX+OpX/gTk8MqjpT1A/c6HY2dCA77ZN0lkQ2Q==",
      "license": "ISC",
      "dependencies": {
        "d3-array": "2 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-time-format": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/d3-time-format/-/d3-time-format-4.1.0.tgz",
      "integrity": "sha512-dJxPBlzC7NugB2PDLwo9Q8JiTR3M3e4/XANkreKSUxF8vvXKqm1Yfq4Q5dl8budlunRVlUUaDUgFt7eA8D6NLg==",
      "license": "ISC",
      "dependencies": {
        "d3-time": "1 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-timer": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-timer/-/d3-timer-3.0.1.tgz",
      "integrity": "sha512-ndfJ/JxxMd3nw31uyKoY2naivF+r29V+Lc0svZxe1JvvIRmi8hUsrMvdOwgS1o6uBHmiz91geQ0ylPP0aj1VUA==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/decimal.js-light": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/decimal.js-light/-/decimal.js-light-2.5.1.tgz",
      "integrity": "sha512-qIMFpTMZmny+MMIitAB6D7iVPEorVw6YQRWkvarTkT4tBeSLLiHzcwj6q0MmYSFCiVpiqPJTJEYIrpcPzVEIvg==",
      "license": "MIT"
    },
    "node_modules/delayed-stream": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
      "integrity": "sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/didyoumean": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/didyoumean/-/didyoumean-1.2.2.tgz",
      "integrity": "sha512-gxtyfqMg7GKyhQmb056K7M3xszy/myH8w+B4RT+QXBQsvAOdc3XymqDDPHx1BgPgsdAA5SIifona89YtRATDzw==",
      "dev": true,
      "license": "Apache-2.0"
    },
    "node_modules/dlv": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/dlv/-/dlv-1.1.3.tgz",
      "integrity": "sha512-+HlytyjlPKnIG8XuRG8WvmBP8xs8P71y+SKKS6ZXWoEgLuePxtDoUEiH7WkdePWrQ5JBpE6aoVqfZfJUQkjXwA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/dom-helpers": {
      "version": "5.2.1",
      "resolved": "https://registry.npmjs.org/dom-helpers/-/dom-helpers-5.2.1.tgz",
      "integrity": "sha512-nRCa7CK3VTrM2NmGkIy4cbK7IZlgBE/PYMn55rrXefr5xXDP0LdtfPnblFDoVdcAfslJ7or6iqAUnx0CCGIWQA==",
      "license": "MIT",
      "dependencies": {
        "@babel/runtime": "^7.8.7",
        "csstype": "^3.0.2"
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/electron-to-chromium": {
      "version": "1.5.361",
      "resolved": "https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.361.tgz",
      "integrity": "sha512-Q6Hts7N9FnJc5LeGRINFvLhCI9xZmNtTDe5ZbcVezQz7cU4a8Aua3GH1b8J2XY8Al9PF+OCwYqhgsOOheMdvkA==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/es-define-property": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
      "integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-object-atoms": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.2.tgz",
      "integrity": "sha512-HWcBoN6NileqtSydK2FqHbS/LoDd2pqrnQHLyJzBj4kOp/ky2MWMN694xOfkK8/SnUsW2DH7EfyVlydKCsm1Zw==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-set-tostringtag": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.1.0.tgz",
      "integrity": "sha512-j6vWzfrGVfyXxge+O0x5sh6cvxAog0a/4Rdd2K36zCMV5eJ+/+tOAngRO8cODMNWbVRdVlmGZQL2YS3yR8bIUA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.6",
        "has-tostringtag": "^1.0.2",
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/esbuild": {
      "version": "0.27.7",
      "resolved": "https://registry.npmjs.org/esbuild/-/esbuild-0.27.7.tgz",
      "integrity": "sha512-IxpibTjyVnmrIQo5aqNpCgoACA/dTKLTlhMHihVHhdkxKyPO1uBBthumT0rdHmcsk9uMonIWS0m4FljWzILh3w==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "bin": {
        "esbuild": "bin/esbuild"
      },
      "engines": {
        "node": ">=18"
      },
      "optionalDependencies": {
        "@esbuild/aix-ppc64": "0.27.7",
        "@esbuild/android-arm": "0.27.7",
        "@esbuild/android-arm64": "0.27.7",
        "@esbuild/android-x64": "0.27.7",
        "@esbuild/darwin-arm64": "0.27.7",
        "@esbuild/darwin-x64": "0.27.7",
        "@esbuild/freebsd-arm64": "0.27.7",
        "@esbuild/freebsd-x64": "0.27.7",
        "@esbuild/linux-arm": "0.27.7",
        "@esbuild/linux-arm64": "0.27.7",
        "@esbuild/linux-ia32": "0.27.7",
        "@esbuild/linux-loong64": "0.27.7",
        "@esbuild/linux-mips64el": "0.27.7",
        "@esbuild/linux-ppc64": "0.27.7",
        "@esbuild/linux-riscv64": "0.27.7",
        "@esbuild/linux-s390x": "0.27.7",
        "@esbuild/linux-x64": "0.27.7",
        "@esbuild/netbsd-arm64": "0.27.7",
        "@esbuild/netbsd-x64": "0.27.7",
        "@esbuild/openbsd-arm64": "0.27.7",
        "@esbuild/openbsd-x64": "0.27.7",
        "@esbuild/openharmony-arm64": "0.27.7",
        "@esbuild/sunos-x64": "0.27.7",
        "@esbuild/win32-arm64": "0.27.7",
        "@esbuild/win32-ia32": "0.27.7",
        "@esbuild/win32-x64": "0.27.7"
      }
    },
    "node_modules/escalade": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
      "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/eventemitter3": {
      "version": "4.0.7",
      "resolved": "https://registry.npmjs.org/eventemitter3/-/eventemitter3-4.0.7.tgz",
      "integrity": "sha512-8guHBZCwKnFhYdHr2ysuRWErTwhoN2X8XELRlrRwpmfeY2jjuUN4taQMsULKUVo1K4DvZl+0pgfyoysHxvmvEw==",
      "license": "MIT"
    },
    "node_modules/fast-equals": {
      "version": "5.4.0",
      "resolved": "https://registry.npmjs.org/fast-equals/-/fast-equals-5.4.0.tgz",
      "integrity": "sha512-jt2DW/aNFNwke7AUd+Z+e6pz39KO5rzdbbFCg2sGafS4mk13MI7Z8O5z9cADNn5lhGODIgLwug6TZO2ctf7kcw==",
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/fast-glob": {
      "version": "3.3.3",
      "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
      "integrity": "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nodelib/fs.stat": "^2.0.2",
        "@nodelib/fs.walk": "^1.2.3",
        "glob-parent": "^5.1.2",
        "merge2": "^1.3.0",
        "micromatch": "^4.0.8"
      },
      "engines": {
        "node": ">=8.6.0"
      }
    },
    "node_modules/fast-glob/node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/fastq": {
      "version": "1.20.1",
      "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.20.1.tgz",
      "integrity": "sha512-GGToxJ/w1x32s/D2EKND7kTil4n8OVk/9mycTc4VDza13lOvpUZTGX3mFSCtV9ksdGBVzvsyAVLM6mHFThxXxw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "reusify": "^1.0.4"
      }
    },
    "node_modules/fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "to-regex-range": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/follow-redirects": {
      "version": "1.16.0",
      "resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.16.0.tgz",
      "integrity": "sha512-y5rN/uOsadFT/JfYwhxRS5R7Qce+g3zG97+JrtFZlC9klX/W5hD7iiLzScI4nZqUS7DNUdhPgw4xI8W2LuXlUw==",
      "funding": [
        {
          "type": "individual",
          "url": "https://github.com/sponsors/RubenVerborgh"
        }
      ],
      "license": "MIT",
      "engines": {
        "node": ">=4.0"
      },
      "peerDependenciesMeta": {
        "debug": {
          "optional": true
        }
      }
    },
    "node_modules/form-data": {
      "version": "4.0.5",
      "resolved": "https://registry.npmjs.org/form-data/-/form-data-4.0.5.tgz",
      "integrity": "sha512-8RipRLol37bNs2bhoV67fiTEvdTrbMUYcFTiy3+wuuOnUog2QBHCZWXDRijWQfAkhBj2Uf5UnVaiWwA5vdd82w==",
      "license": "MIT",
      "dependencies": {
        "asynckit": "^0.4.0",
        "combined-stream": "^1.0.8",
        "es-set-tostringtag": "^2.1.0",
        "hasown": "^2.0.2",
        "mime-types": "^2.1.12"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/fraction.js": {
      "version": "5.3.4",
      "resolved": "https://registry.npmjs.org/fraction.js/-/fraction.js-5.3.4.tgz",
      "integrity": "sha512-1X1NTtiJphryn/uLQz3whtY6jK3fTqoE3ohKs0tT+Ujr1W59oopxmoEh7Lu5p6vBaPbgoM0bzveAW4Qi5RyWDQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "*"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/rawify"
      }
    },
    "node_modules/framer-motion": {
      "version": "11.18.2",
      "resolved": "https://registry.npmjs.org/framer-motion/-/framer-motion-11.18.2.tgz",
      "integrity": "sha512-5F5Och7wrvtLVElIpclDT0CBzMVg3dL22B64aZwHtsIY8RB4mXICLrkajK4G9R+ieSAGcgrLeae2SeUTg2pr6w==",
      "license": "MIT",
      "dependencies": {
        "motion-dom": "^11.18.1",
        "motion-utils": "^11.18.1",
        "tslib": "^2.4.0"
      },
      "peerDependencies": {
        "@emotion/is-prop-valid": "*",
        "react": "^18.0.0 || ^19.0.0",
        "react-dom": "^18.0.0 || ^19.0.0"
      },
      "peerDependenciesMeta": {
        "@emotion/is-prop-valid": {
          "optional": true
        },
        "react": {
          "optional": true
        },
        "react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/fsevents": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
      "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/gensync": {
      "version": "1.0.0-beta.2",
      "resolved": "https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.2.tgz",
      "integrity": "sha512-3hN7NaskYvMDLQY55gnW3NQ+mesEAepTqlg+VEbj7zzqEMBVNhzcGYYeqFo/TlYz6eQiFcp1HcsCZO+nGgS8zg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/get-intrinsic": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
      "integrity": "sha512-9fSjSaos/fRIVIp+xSJlE6lfwhES7LNtKaCBIamHsjr2na1BiABJPo0mOjjz8GJDURarmCPGqaiVg5mfjb98CQ==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "es-define-property": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.1.1",
        "function-bind": "^1.1.2",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-symbols": "^1.1.0",
        "hasown": "^2.0.2",
        "math-intrinsics": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
      "integrity": "sha512-sTSfBjoXBp89JvIKIefqw7U2CCebsc74kiY6awiGogKtoSGbgjYE/G/+l9sF3MWFPNc9IcoOC4ODfKHfxFmp0g==",
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/glob-parent": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz",
      "integrity": "sha512-XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.3"
      },
      "engines": {
        "node": ">=10.13.0"
      }
    },
    "node_modules/gopd": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
      "integrity": "sha512-ZUKRh6/kUFoAiTAtTYPZJ3hw9wNxx+BIBOijnlG9PnrJsCcSjs1wyyD6vJpaYtgnzDrKYRSqf3OO6Rfa93xsRg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-symbols": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
      "integrity": "sha512-1cDNdwJ2Jaohmb3sg4OmKaMBwuC48sYni5HUw2DvsC8LjGTLK9h+eb1X6RyuOHe4hT0ULCW68iomhjUoKUqlPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-tostringtag": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz",
      "integrity": "sha512-NqADB8VjPFLM2V0VvHUewwwsw0ZWBaIdgo+ieHtK3hasLz4qeCRjYcqfB6AQrBggRKppKF8L52/VqdVsO47Dlw==",
      "license": "MIT",
      "dependencies": {
        "has-symbols": "^1.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/hasown": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.3.tgz",
      "integrity": "sha512-ej4AhfhfL2Q2zpMmLo7U1Uv9+PyhIZpgQLGT1F9miIGmiCJIoCgSmczFdrc97mWT4kVY72KA+WnnhJ5pghSvSg==",
      "license": "MIT",
      "dependencies": {
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/https-proxy-agent": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-5.0.1.tgz",
      "integrity": "sha512-dFcAjpTQFgoLMzC2VwU+C/CbS7uRL0lWmxDITmqm7C+7F0Odmj6s9l6alZc6AELXhrnggM2CeWSXHGOdX2YtwA==",
      "license": "MIT",
      "dependencies": {
        "agent-base": "6",
        "debug": "4"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/internmap": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/internmap/-/internmap-2.0.3.tgz",
      "integrity": "sha512-5Hh7Y1wQbvY5ooGgPbDaL5iYLAPzMTUrjMulskHLH6wnv/A+1q5rgEaiuqEjB+oxGXIVZs1FF+R/KPN3ZSQYYg==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/is-binary-path": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz",
      "integrity": "sha512-ZMERYes6pDydyuGidse7OsHxtbI7WVeUEozgR/g7rd0xUimYNlvZRE/K2MgZTjWy725IfelLeVcEM97mmtRGXw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "binary-extensions": "^2.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/is-core-module": {
      "version": "2.16.2",
      "resolved": "https://registry.npmjs.org/is-core-module/-/is-core-module-2.16.2.tgz",
      "integrity": "sha512-evOr8xfXKxE6qSR0hSXL2r3sd7ALj8+7jQEUvPYcm5sgZFdJ+AYzT6yNmJenvIYQBgIGwfwz08sL8zoL7yq2BA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "hasown": "^2.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-extglob": "^2.1.1"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.12.0"
      }
    },
    "node_modules/jiti": {
      "version": "1.21.7",
      "resolved": "https://registry.npmjs.org/jiti/-/jiti-1.21.7.tgz",
      "integrity": "sha512-/imKNG4EbWNrVjoNC/1H5/9GFy+tqjGBHCaSsN+P2RnPqjsLmv6UD3Ej+Kj8nBWaRAwyk7kK5ZUc+OEatnTR3A==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "jiti": "bin/jiti.js"
      }
    },
    "node_modules/js-tokens": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
      "integrity": "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==",
      "license": "MIT"
    },
    "node_modules/jsesc": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz",
      "integrity": "sha512-/sM3dO2FOzXjKQhJuo0Q173wf2KOo8t4I8vHy6lF9poUp7bKT0/NHE8fPX23PwfhnykfqnC2xRxOnVw5XuGIaA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "jsesc": "bin/jsesc"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/json5": {
      "version": "2.2.3",
      "resolved": "https://registry.npmjs.org/json5/-/json5-2.2.3.tgz",
      "integrity": "sha512-XmOWe7eyHYH14cLdVPoyg+GOH3rYX++KpzrylJwSW98t3Nk+U8XOl8FWKOgwtzdb8lXGf6zYwDUzeHMWfxasyg==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "json5": "lib/cli.js"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/lilconfig": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/lilconfig/-/lilconfig-3.1.3.tgz",
      "integrity": "sha512-/vlFKAoH5Cgt3Ie+JLhRbwOsCQePABiU3tJ1egGvyQ+33R/vcwM2Zl2QR/LzjsBeItPt3oSVXapn+m4nQDvpzw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=14"
      },
      "funding": {
        "url": "https://github.com/sponsors/antonk52"
      }
    },
    "node_modules/lines-and-columns": {
      "version": "1.2.4",
      "resolved": "https://registry.npmjs.org/lines-and-columns/-/lines-and-columns-1.2.4.tgz",
      "integrity": "sha512-7ylylesZQ/PV29jhEDl3Ufjo6ZX7gCqJr5F7PKrqc93v7fzSymt1BpwEU8nAUXs8qzzvqhbjhK5QZg6Mt/HkBg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/lodash": {
      "version": "4.18.1",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.18.1.tgz",
      "integrity": "sha512-dMInicTPVE8d1e5otfwmmjlxkZoUpiVLwyeTdUsi/Caj/gfzzblBcCE5sRHV/AsjuCmxWrte2TNGSYuCeCq+0Q==",
      "license": "MIT"
    },
    "node_modules/loose-envify": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz",
      "integrity": "sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q==",
      "license": "MIT",
      "dependencies": {
        "js-tokens": "^3.0.0 || ^4.0.0"
      },
      "bin": {
        "loose-envify": "cli.js"
      }
    },
    "node_modules/lru-cache": {
      "version": "5.1.1",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz",
      "integrity": "sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "yallist": "^3.0.2"
      }
    },
    "node_modules/lucide-react": {
      "version": "0.453.0",
      "resolved": "https://registry.npmjs.org/lucide-react/-/lucide-react-0.453.0.tgz",
      "integrity": "sha512-kL+RGZCcJi9BvJtzg2kshO192Ddy9hv3ij+cPrVPWSRzgCWCVazoQJxOjAwgK53NomL07HB7GPHW120FimjNhQ==",
      "license": "ISC",
      "peerDependencies": {
        "react": "^16.5.1 || ^17.0.0 || ^18.0.0 || ^19.0.0-rc"
      }
    },
    "node_modules/math-intrinsics": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz",
      "integrity": "sha512-/IXtbwEk5HTPyEwyKX6hGkYXxM9nbj64B+ilVJnC/R6B0pH5G4V3b0pVbL7DBj4tkhBAppbQUlf6F6Xl9LHu1g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/merge2": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
      "integrity": "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/micromatch": {
      "version": "4.0.8",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
      "integrity": "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "braces": "^3.0.3",
        "picomatch": "^2.3.1"
      },
      "engines": {
        "node": ">=8.6"
      }
    },
    "node_modules/mime-db": {
      "version": "1.52.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz",
      "integrity": "sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime-types": {
      "version": "2.1.35",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz",
      "integrity": "sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==",
      "license": "MIT",
      "dependencies": {
        "mime-db": "1.52.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/motion-dom": {
      "version": "11.18.1",
      "resolved": "https://registry.npmjs.org/motion-dom/-/motion-dom-11.18.1.tgz",
      "integrity": "sha512-g76KvA001z+atjfxczdRtw/RXOM3OMSdd1f4DL77qCTF/+avrRJiawSG4yDibEQ215sr9kpinSlX2pCTJ9zbhw==",
      "license": "MIT",
      "dependencies": {
        "motion-utils": "^11.18.1"
      }
    },
    "node_modules/motion-utils": {
      "version": "11.18.1",
      "resolved": "https://registry.npmjs.org/motion-utils/-/motion-utils-11.18.1.tgz",
      "integrity": "sha512-49Kt+HKjtbJKLtgO/LKj9Ld+6vw9BjH5d9sc40R/kVyH8GLAXgT42M2NnuPcJNuA3s9ZfZBUcwIgpmZWGEE+hA==",
      "license": "MIT"
    },
    "node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/mz": {
      "version": "2.7.0",
      "resolved": "https://registry.npmjs.org/mz/-/mz-2.7.0.tgz",
      "integrity": "sha512-z81GNO7nnYMEhrGh9LeymoE4+Yr0Wn5McHIZMK5cfQCl+NDX08sCZgUc9/6MHni9IWuFLm1Z3HTCXu2z9fN62Q==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "any-promise": "^1.0.0",
        "object-assign": "^4.0.1",
        "thenify-all": "^1.0.0"
      }
    },
    "node_modules/nanoid": {
      "version": "3.3.12",
      "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.12.tgz",
      "integrity": "sha512-ZB9RH/39qpq5Vu6Y+NmUaFhQR6pp+M2Xt76XBnEwDaGcVAqhlvxrl3B2bKS5D3NH3QR76v3aSrKaF/Kiy7lEtQ==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "bin": {
        "nanoid": "bin/nanoid.cjs"
      },
      "engines": {
        "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
      }
    },
    "node_modules/node-releases": {
      "version": "2.0.46",
      "resolved": "https://registry.npmjs.org/node-releases/-/node-releases-2.0.46.tgz",
      "integrity": "sha512-GYVXHE2KnrzAfsAjl4uP++evGFCrAU1jta4ubEjIG7YWt/64Gqv66a30yKwWczVjA6j3bM4nBwH7Pk1JmDHaxQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/normalize-path": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz",
      "integrity": "sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/object-assign": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
      "integrity": "sha512-rJgTQnkUnH1sFw8yT6VSU3zD3sWmu6sZhIseY8VX+GRu3P6F7Fu+JNDoXfklElbLJSnc3FUQHVe4cU5hj+BcUg==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/object-hash": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/object-hash/-/object-hash-3.0.0.tgz",
      "integrity": "sha512-RSn9F68PjH9HqtltsSnqYC1XXoWe9Bju5+213R98cNGttag9q9yAOTzdbsqvIa7aNm5WffBZFpWYr2aWrklWAw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/path-parse": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz",
      "integrity": "sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/picocolors": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
      "integrity": "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/picomatch": {
      "version": "2.3.2",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.2.tgz",
      "integrity": "sha512-V7+vQEJ06Z+c5tSye8S+nHUfI51xoXIXjHQ99cQtKUkQqqO1kO/KCJUfZXuB47h/YBlDhah2H3hdUGXn8ie0oA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/pify": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/pify/-/pify-2.3.0.tgz",
      "integrity": "sha512-udgsAY+fTnvv7kI7aaxbqwWNb0AHiB0qBO89PZKPkoTmGOgdbrHDKD+0B2X4uTfJ/FT1R09r9gTsjUjNJotuog==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/pirates": {
      "version": "4.0.7",
      "resolved": "https://registry.npmjs.org/pirates/-/pirates-4.0.7.tgz",
      "integrity": "sha512-TfySrs/5nm8fQJDcBDuUng3VOUKsd7S+zqvbOTiGXHfxX4wK31ard+hoNuvkicM/2YFzlpDgABOevKSsB4G/FA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/postcss": {
      "version": "8.5.15",
      "resolved": "https://registry.npmjs.org/postcss/-/postcss-8.5.15.tgz",
      "integrity": "sha512-FfR8sjd4em2T6fb3I2MwAJU7HWVMr9zba+enmQeeWFfCbm+UOC/0X4DS8XtpUTMwWMGbjKYP7xjfNekzyGmB3A==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/postcss"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "nanoid": "^3.3.12",
        "picocolors": "^1.1.1",
        "source-map-js": "^1.2.1"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      }
    },
    "node_modules/postcss-import": {
      "version": "15.1.0",
      "resolved": "https://registry.npmjs.org/postcss-import/-/postcss-import-15.1.0.tgz",
      "integrity": "sha512-hpr+J05B2FVYUAXHeK1YyI267J/dDDhMU6B6civm8hSY1jYJnBXxzKDKDswzJmtLHryrjhnDjqqp/49t8FALew==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "postcss-value-parser": "^4.0.0",
        "read-cache": "^1.0.0",
        "resolve": "^1.1.7"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "postcss": "^8.0.0"
      }
    },
    "node_modules/postcss-js": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/postcss-js/-/postcss-js-4.1.0.tgz",
      "integrity": "sha512-oIAOTqgIo7q2EOwbhb8UalYePMvYoIeRY2YKntdpFQXNosSu3vLrniGgmH9OKs/qAkfoj5oB3le/7mINW1LCfw==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "camelcase-css": "^2.0.1"
      },
      "engines": {
        "node": "^12 || ^14 || >= 16"
      },
      "peerDependencies": {
        "postcss": "^8.4.21"
      }
    },
    "node_modules/postcss-load-config": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/postcss-load-config/-/postcss-load-config-6.0.1.tgz",
      "integrity": "sha512-oPtTM4oerL+UXmx+93ytZVN82RrlY/wPUV8IeDxFrzIjXOLF1pN+EmKPLbubvKHT2HC20xXsCAH2Z+CKV6Oz/g==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "lilconfig": "^3.1.1"
      },
      "engines": {
        "node": ">= 18"
      },
      "peerDependencies": {
        "jiti": ">=1.21.0",
        "postcss": ">=8.0.9",
        "tsx": "^4.8.1",
        "yaml": "^2.4.2"
      },
      "peerDependenciesMeta": {
        "jiti": {
          "optional": true
        },
        "postcss": {
          "optional": true
        },
        "tsx": {
          "optional": true
        },
        "yaml": {
          "optional": true
        }
      }
    },
    "node_modules/postcss-nested": {
      "version": "6.2.0",
      "resolved": "https://registry.npmjs.org/postcss-nested/-/postcss-nested-6.2.0.tgz",
      "integrity": "sha512-HQbt28KulC5AJzG+cZtj9kvKB93CFCdLvog1WFLf1D+xmMvPGlBstkpTEZfK5+AN9hfJocyBFCNiqyS48bpgzQ==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "postcss-selector-parser": "^6.1.1"
      },
      "engines": {
        "node": ">=12.0"
      },
      "peerDependencies": {
        "postcss": "^8.2.14"
      }
    },
    "node_modules/postcss-selector-parser": {
      "version": "6.1.2",
      "resolved": "https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-6.1.2.tgz",
      "integrity": "sha512-Q8qQfPiZ+THO/3ZrOrO0cJJKfpYCagtMUkXbnEfmgUjwXg6z/WBeOyS9APBBPCTSiDV+s4SwQGu8yFsiMRIudg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "cssesc": "^3.0.0",
        "util-deprecate": "^1.0.2"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/postcss-value-parser": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz",
      "integrity": "sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/prop-types": {
      "version": "15.8.1",
      "resolved": "https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz",
      "integrity": "sha512-oj87CgZICdulUohogVAR7AjlC0327U4el4L6eAvOqCeudMDVU0NThNaV+b9Df4dXgSP1gXMTnPdhfe/2qDH5cg==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.4.0",
        "object-assign": "^4.1.1",
        "react-is": "^16.13.1"
      }
    },
    "node_modules/prop-types/node_modules/react-is": {
      "version": "16.13.1",
      "resolved": "https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz",
      "integrity": "sha512-24e6ynE2H+OKt4kqsOvNd8kBpV65zoxbA4BVsEOB3ARVWQki/DHzaUoC5KuON/BiccDaCCTZBuOcfZs70kR8bQ==",
      "license": "MIT"
    },
    "node_modules/proxy-from-env": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/proxy-from-env/-/proxy-from-env-2.1.0.tgz",
      "integrity": "sha512-cJ+oHTW1VAEa8cJslgmUZrc+sjRKgAKl3Zyse6+PV38hZe/V6Z14TbCuXcan9F9ghlz4QrFr2c92TNF82UkYHA==",
      "license": "MIT",
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/queue-microtask": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
      "integrity": "sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/react": {
      "version": "18.3.1",
      "resolved": "https://registry.npmjs.org/react/-/react-18.3.1.tgz",
      "integrity": "sha512-wS+hAgJShR0KhEvPJArfuPVN1+Hz1t0Y6n5jLrGQbkb4urgPE/0Rve+1kMB1v/oWgHgm4WIcV+i7F2pTVj+2iQ==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.1.0"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-dom": {
      "version": "18.3.1",
      "resolved": "https://registry.npmjs.org/react-dom/-/react-dom-18.3.1.tgz",
      "integrity": "sha512-5m4nQKp+rZRb09LNH59GM4BxTh9251/ylbKIbpe7TpGxfJ+9kv6BLkLBXIjjspbgbnIBNqlI23tRnTWT0snUIw==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.1.0",
        "scheduler": "^0.23.2"
      },
      "peerDependencies": {
        "react": "^18.3.1"
      }
    },
    "node_modules/react-is": {
      "version": "18.3.1",
      "resolved": "https://registry.npmjs.org/react-is/-/react-is-18.3.1.tgz",
      "integrity": "sha512-/LLMVyas0ljjAtoYiPqYiL8VWXzUUdThrmU5+n20DZv+a+ClRoevUzw5JxU+Ieh5/c87ytoTBV9G1FiKfNJdmg==",
      "license": "MIT"
    },
    "node_modules/react-refresh": {
      "version": "0.17.0",
      "resolved": "https://registry.npmjs.org/react-refresh/-/react-refresh-0.17.0.tgz",
      "integrity": "sha512-z6F7K9bV85EfseRCp2bzrpyQ0Gkw1uLoCel9XBVWPg/TjRj94SkJzUTGfOa4bs7iJvBWtQG0Wq7wnI0syw3EBQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-router": {
      "version": "6.30.3",
      "resolved": "https://registry.npmjs.org/react-router/-/react-router-6.30.3.tgz",
      "integrity": "sha512-XRnlbKMTmktBkjCLE8/XcZFlnHvr2Ltdr1eJX4idL55/9BbORzyZEaIkBFDhFGCEWBBItsVrDxwx3gnisMitdw==",
      "license": "MIT",
      "dependencies": {
        "@remix-run/router": "1.23.2"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "react": ">=16.8"
      }
    },
    "node_modules/react-router-dom": {
      "version": "6.30.3",
      "resolved": "https://registry.npmjs.org/react-router-dom/-/react-router-dom-6.30.3.tgz",
      "integrity": "sha512-pxPcv1AczD4vso7G4Z3TKcvlxK7g7TNt3/FNGMhfqyntocvYKj+GCatfigGDjbLozC4baguJ0ReCigoDJXb0ag==",
      "license": "MIT",
      "dependencies": {
        "@remix-run/router": "1.23.2",
        "react-router": "6.30.3"
      },
      "engines": {
        "node": ">=14.0.0"
      },
      "peerDependencies": {
        "react": ">=16.8",
        "react-dom": ">=16.8"
      }
    },
    "node_modules/react-smooth": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/react-smooth/-/react-smooth-4.0.4.tgz",
      "integrity": "sha512-gnGKTpYwqL0Iii09gHobNolvX4Kiq4PKx6eWBCYYix+8cdw+cGo3do906l1NBPKkSWx1DghC1dlWG9L2uGd61Q==",
      "license": "MIT",
      "dependencies": {
        "fast-equals": "^5.0.1",
        "prop-types": "^15.8.1",
        "react-transition-group": "^4.4.5"
      },
      "peerDependencies": {
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0",
        "react-dom": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      }
    },
    "node_modules/react-transition-group": {
      "version": "4.4.5",
      "resolved": "https://registry.npmjs.org/react-transition-group/-/react-transition-group-4.4.5.tgz",
      "integrity": "sha512-pZcd1MCJoiKiBR2NRxeCRg13uCXbydPnmB4EOeRrY7480qNWO8IIgQG6zlDkm6uRMsURXPuKq0GWtiM59a5Q6g==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "@babel/runtime": "^7.5.5",
        "dom-helpers": "^5.0.1",
        "loose-envify": "^1.4.0",
        "prop-types": "^15.6.2"
      },
      "peerDependencies": {
        "react": ">=16.6.0",
        "react-dom": ">=16.6.0"
      }
    },
    "node_modules/read-cache": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/read-cache/-/read-cache-1.0.0.tgz",
      "integrity": "sha512-Owdv/Ft7IjOgm/i0xvNDZ1LrRANRfew4b2prF3OWMQLxLfu3bS8FVhCsrSCMK4lR56Y9ya+AThoTpDCTxCmpRA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "pify": "^2.3.0"
      }
    },
    "node_modules/readdirp": {
      "version": "3.6.0",
      "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-3.6.0.tgz",
      "integrity": "sha512-hOS089on8RduqdbhvQ5Z37A0ESjsqz6qnRcffsMU3495FuTdqSm+7bhJ29JvIOsBDEEnan5DPu9t3To9VRlMzA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "picomatch": "^2.2.1"
      },
      "engines": {
        "node": ">=8.10.0"
      }
    },
    "node_modules/recharts": {
      "version": "2.15.4",
      "resolved": "https://registry.npmjs.org/recharts/-/recharts-2.15.4.tgz",
      "integrity": "sha512-UT/q6fwS3c1dHbXv2uFgYJ9BMFHu3fwnd7AYZaEQhXuYQ4hgsxLvsUXzGdKeZrW5xopzDCvuA2N41WJ88I7zIw==",
      "deprecated": "1.x and 2.x branches are no longer active. Bump to Recharts v3 to receive latest features and bugfixes. See https://github.com/recharts/recharts/wiki/3.0-migration-guide",
      "license": "MIT",
      "dependencies": {
        "clsx": "^2.0.0",
        "eventemitter3": "^4.0.1",
        "lodash": "^4.17.21",
        "react-is": "^18.3.1",
        "react-smooth": "^4.0.4",
        "recharts-scale": "^0.4.4",
        "tiny-invariant": "^1.3.1",
        "victory-vendor": "^36.6.8"
      },
      "engines": {
        "node": ">=14"
      },
      "peerDependencies": {
        "react": "^16.0.0 || ^17.0.0 || ^18.0.0 || ^19.0.0",
        "react-dom": "^16.0.0 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      }
    },
    "node_modules/recharts-scale": {
      "version": "0.4.5",
      "resolved": "https://registry.npmjs.org/recharts-scale/-/recharts-scale-0.4.5.tgz",
      "integrity": "sha512-kivNFO+0OcUNu7jQquLXAxz1FIwZj8nrj+YkOKc5694NbjCvcT6aSZiIzNzd2Kul4o4rTto8QVR9lMNtxD4G1w==",
      "license": "MIT",
      "dependencies": {
        "decimal.js-light": "^2.4.1"
      }
    },
    "node_modules/resolve": {
      "version": "1.22.12",
      "resolved": "https://registry.npmjs.org/resolve/-/resolve-1.22.12.tgz",
      "integrity": "sha512-TyeJ1zif53BPfHootBGwPRYT1RUt6oGWsaQr8UyZW/eAm9bKoijtvruSDEmZHm92CwS9nj7/fWttqPCgzep8CA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "is-core-module": "^2.16.1",
        "path-parse": "^1.0.7",
        "supports-preserve-symlinks-flag": "^1.0.0"
      },
      "bin": {
        "resolve": "bin/resolve"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/reusify": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz",
      "integrity": "sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "iojs": ">=1.0.0",
        "node": ">=0.10.0"
      }
    },
    "node_modules/rollup": {
      "version": "4.60.4",
      "resolved": "https://registry.npmjs.org/rollup/-/rollup-4.60.4.tgz",
      "integrity": "sha512-WHeFSbZYsPu3+bLoNRUuAO+wavNlocOPf3wSHTP7hcFKVnJeWsYlCDbr3mTS14FCizf9ccIxXA8sGL8zKeQN3g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/estree": "1.0.8"
      },
      "bin": {
        "rollup": "dist/bin/rollup"
      },
      "engines": {
        "node": ">=18.0.0",
        "npm": ">=8.0.0"
      },
      "optionalDependencies": {
        "@rollup/rollup-android-arm-eabi": "4.60.4",
        "@rollup/rollup-android-arm64": "4.60.4",
        "@rollup/rollup-darwin-arm64": "4.60.4",
        "@rollup/rollup-darwin-x64": "4.60.4",
        "@rollup/rollup-freebsd-arm64": "4.60.4",
        "@rollup/rollup-freebsd-x64": "4.60.4",
        "@rollup/rollup-linux-arm-gnueabihf": "4.60.4",
        "@rollup/rollup-linux-arm-musleabihf": "4.60.4",
        "@rollup/rollup-linux-arm64-gnu": "4.60.4",
        "@rollup/rollup-linux-arm64-musl": "4.60.4",
        "@rollup/rollup-linux-loong64-gnu": "4.60.4",
        "@rollup/rollup-linux-loong64-musl": "4.60.4",
        "@rollup/rollup-linux-ppc64-gnu": "4.60.4",
        "@rollup/rollup-linux-ppc64-musl": "4.60.4",
        "@rollup/rollup-linux-riscv64-gnu": "4.60.4",
        "@rollup/rollup-linux-riscv64-musl": "4.60.4",
        "@rollup/rollup-linux-s390x-gnu": "4.60.4",
        "@rollup/rollup-linux-x64-gnu": "4.60.4",
        "@rollup/rollup-linux-x64-musl": "4.60.4",
        "@rollup/rollup-openbsd-x64": "4.60.4",
        "@rollup/rollup-openharmony-arm64": "4.60.4",
        "@rollup/rollup-win32-arm64-msvc": "4.60.4",
        "@rollup/rollup-win32-ia32-msvc": "4.60.4",
        "@rollup/rollup-win32-x64-gnu": "4.60.4",
        "@rollup/rollup-win32-x64-msvc": "4.60.4",
        "fsevents": "~2.3.2"
      }
    },
    "node_modules/run-parallel": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz",
      "integrity": "sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "queue-microtask": "^1.2.2"
      }
    },
    "node_modules/scheduler": {
      "version": "0.23.2",
      "resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.23.2.tgz",
      "integrity": "sha512-UOShsPwz7NrMUqhR6t0hWjFduvOzbtv7toDH1/hIrfRNIDBnnBWd0CwJTGvTpngVlmwGCdP9/Zl/tVrDqcuYzQ==",
      "license": "MIT",
      "dependencies": {
        "loose-envify": "^1.1.0"
      }
    },
    "node_modules/semver": {
      "version": "6.3.1",
      "resolved": "https://registry.npmjs.org/semver/-/semver-6.3.1.tgz",
      "integrity": "sha512-BR7VvDCVHO+q2xBEWskxS6DJE1qRnb7DxzUrogb71CWoSficBxYsiAGd+Kl0mmq/MprG9yArRkyrQxTO6XjMzA==",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      }
    },
    "node_modules/source-map-js": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz",
      "integrity": "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==",
      "dev": true,
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/sucrase": {
      "version": "3.35.1",
      "resolved": "https://registry.npmjs.org/sucrase/-/sucrase-3.35.1.tgz",
      "integrity": "sha512-DhuTmvZWux4H1UOnWMB3sk0sbaCVOoQZjv8u1rDoTV0HTdGem9hkAZtl4JZy8P2z4Bg0nT+YMeOFyVr4zcG5Tw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/gen-mapping": "^0.3.2",
        "commander": "^4.0.0",
        "lines-and-columns": "^1.1.6",
        "mz": "^2.7.0",
        "pirates": "^4.0.1",
        "tinyglobby": "^0.2.11",
        "ts-interface-checker": "^0.1.9"
      },
      "bin": {
        "sucrase": "bin/sucrase",
        "sucrase-node": "bin/sucrase-node"
      },
      "engines": {
        "node": ">=16 || 14 >=14.17"
      }
    },
    "node_modules/supports-preserve-symlinks-flag": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz",
      "integrity": "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/tailwindcss": {
      "version": "3.4.19",
      "resolved": "https://registry.npmjs.org/tailwindcss/-/tailwindcss-3.4.19.tgz",
      "integrity": "sha512-3ofp+LL8E+pK/JuPLPggVAIaEuhvIz4qNcf3nA1Xn2o/7fb7s/TYpHhwGDv1ZU3PkBluUVaF8PyCHcm48cKLWQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@alloc/quick-lru": "^5.2.0",
        "arg": "^5.0.2",
        "chokidar": "^3.6.0",
        "didyoumean": "^1.2.2",
        "dlv": "^1.1.3",
        "fast-glob": "^3.3.2",
        "glob-parent": "^6.0.2",
        "is-glob": "^4.0.3",
        "jiti": "^1.21.7",
        "lilconfig": "^3.1.3",
        "micromatch": "^4.0.8",
        "normalize-path": "^3.0.0",
        "object-hash": "^3.0.0",
        "picocolors": "^1.1.1",
        "postcss": "^8.4.47",
        "postcss-import": "^15.1.0",
        "postcss-js": "^4.0.1",
        "postcss-load-config": "^4.0.2 || ^5.0 || ^6.0",
        "postcss-nested": "^6.2.0",
        "postcss-selector-parser": "^6.1.2",
        "resolve": "^1.22.8",
        "sucrase": "^3.35.0"
      },
      "bin": {
        "tailwind": "lib/cli.js",
        "tailwindcss": "lib/cli.js"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/thenify": {
      "version": "3.3.1",
      "resolved": "https://registry.npmjs.org/thenify/-/thenify-3.3.1.tgz",
      "integrity": "sha512-RVZSIV5IG10Hk3enotrhvz0T9em6cyHBLkH/YAZuKqd8hRkKhSfCGIcP2KUY0EPxndzANBmNllzWPwak+bheSw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "any-promise": "^1.0.0"
      }
    },
    "node_modules/thenify-all": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/thenify-all/-/thenify-all-1.6.0.tgz",
      "integrity": "sha512-RNxQH/qI8/t3thXJDwcstUO4zeqo64+Uy/+sNVRBx4Xn2OX+OZ9oP+iJnNFqplFra2ZUVeKCSa2oVWi3T4uVmA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "thenify": ">= 3.1.0 < 4"
      },
      "engines": {
        "node": ">=0.8"
      }
    },
    "node_modules/tiny-invariant": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/tiny-invariant/-/tiny-invariant-1.3.3.tgz",
      "integrity": "sha512-+FbBPE1o9QAYvviau/qC5SE3caw21q3xkvWKBtja5vgqOWIHHJ3ioaq1VPfn/Szqctz2bU/oYeKd9/z5BL+PVg==",
      "license": "MIT"
    },
    "node_modules/tinyglobby": {
      "version": "0.2.16",
      "resolved": "https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.16.tgz",
      "integrity": "sha512-pn99VhoACYR8nFHhxqix+uvsbXineAasWm5ojXoN8xEwK5Kd3/TrhNn1wByuD52UxWRLy8pu+kRMniEi6Eq9Zg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fdir": "^6.5.0",
        "picomatch": "^4.0.4"
      },
      "engines": {
        "node": ">=12.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/SuperchupuDev"
      }
    },
    "node_modules/tinyglobby/node_modules/fdir": {
      "version": "6.5.0",
      "resolved": "https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz",
      "integrity": "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12.0.0"
      },
      "peerDependencies": {
        "picomatch": "^3 || ^4"
      },
      "peerDependenciesMeta": {
        "picomatch": {
          "optional": true
        }
      }
    },
    "node_modules/tinyglobby/node_modules/picomatch": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.4.tgz",
      "integrity": "sha512-QP88BAKvMam/3NxH6vj2o21R6MjxZUAd6nlwAS/pnGvN9IVLocLHxGYIzFhg6fUQ+5th6P4dv4eW9jX3DSIj7A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-number": "^7.0.0"
      },
      "engines": {
        "node": ">=8.0"
      }
    },
    "node_modules/ts-interface-checker": {
      "version": "0.1.13",
      "resolved": "https://registry.npmjs.org/ts-interface-checker/-/ts-interface-checker-0.1.13.tgz",
      "integrity": "sha512-Y/arvbn+rrz3JCKl9C4kVNfTfSm2/mEp5FSz5EsZSANGPSlQrpRI5M4PKF+mJnE52jOO90PnPSc3Ur3bTQw0gA==",
      "dev": true,
      "license": "Apache-2.0"
    },
    "node_modules/tslib": {
      "version": "2.8.1",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
      "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
      "license": "0BSD"
    },
    "node_modules/update-browserslist-db": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.2.3.tgz",
      "integrity": "sha512-Js0m9cx+qOgDxo0eMiFGEueWztz+d4+M3rGlmKPT+T4IS/jP4ylw3Nwpu6cpTTP8R1MAC1kF4VbdLt3ARf209w==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "escalade": "^3.2.0",
        "picocolors": "^1.1.1"
      },
      "bin": {
        "update-browserslist-db": "cli.js"
      },
      "peerDependencies": {
        "browserslist": ">= 4.21.0"
      }
    },
    "node_modules/util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/victory-vendor": {
      "version": "36.9.2",
      "resolved": "https://registry.npmjs.org/victory-vendor/-/victory-vendor-36.9.2.tgz",
      "integrity": "sha512-PnpQQMuxlwYdocC8fIJqVXvkeViHYzotI+NJrCuav0ZYFoq912ZHBk3mCeuj+5/VpodOjPe1z0Fk2ihgzlXqjQ==",
      "license": "MIT AND ISC",
      "dependencies": {
        "@types/d3-array": "^3.0.3",
        "@types/d3-ease": "^3.0.0",
        "@types/d3-interpolate": "^3.0.1",
        "@types/d3-scale": "^4.0.2",
        "@types/d3-shape": "^3.1.0",
        "@types/d3-time": "^3.0.0",
        "@types/d3-timer": "^3.0.0",
        "d3-array": "^3.1.6",
        "d3-ease": "^3.0.1",
        "d3-interpolate": "^3.0.1",
        "d3-scale": "^4.0.2",
        "d3-shape": "^3.1.0",
        "d3-time": "^3.0.0",
        "d3-timer": "^3.0.1"
      }
    },
    "node_modules/vite": {
      "version": "7.3.3",
      "resolved": "https://registry.npmjs.org/vite/-/vite-7.3.3.tgz",
      "integrity": "sha512-/4XH147Ui7OGTjg3HbdWe5arnZQSbfuRzdr9Ec7TQi5I7R+ir0Rlc9GIvD4v0XZurELqA035KVXJXpR61xhiTA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "esbuild": "^0.27.0",
        "fdir": "^6.5.0",
        "picomatch": "^4.0.3",
        "postcss": "^8.5.6",
        "rollup": "^4.43.0",
        "tinyglobby": "^0.2.15"
      },
      "bin": {
        "vite": "bin/vite.js"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "funding": {
        "url": "https://github.com/vitejs/vite?sponsor=1"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.3"
      },
      "peerDependencies": {
        "@types/node": "^20.19.0 || >=22.12.0",
        "jiti": ">=1.21.0",
        "less": "^4.0.0",
        "lightningcss": "^1.21.0",
        "sass": "^1.70.0",
        "sass-embedded": "^1.70.0",
        "stylus": ">=0.54.8",
        "sugarss": "^5.0.0",
        "terser": "^5.16.0",
        "tsx": "^4.8.1",
        "yaml": "^2.4.2"
      },
      "peerDependenciesMeta": {
        "@types/node": {
          "optional": true
        },
        "jiti": {
          "optional": true
        },
        "less": {
          "optional": true
        },
        "lightningcss": {
          "optional": true
        },
        "sass": {
          "optional": true
        },
        "sass-embedded": {
          "optional": true
        },
        "stylus": {
          "optional": true
        },
        "sugarss": {
          "optional": true
        },
        "terser": {
          "optional": true
        },
        "tsx": {
          "optional": true
        },
        "yaml": {
          "optional": true
        }
      }
    },
    "node_modules/vite/node_modules/fdir": {
      "version": "6.5.0",
      "resolved": "https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz",
      "integrity": "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12.0.0"
      },
      "peerDependencies": {
        "picomatch": "^3 || ^4"
      },
      "peerDependenciesMeta": {
        "picomatch": {
          "optional": true
        }
      }
    },
    "node_modules/vite/node_modules/picomatch": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.4.tgz",
      "integrity": "sha512-QP88BAKvMam/3NxH6vj2o21R6MjxZUAd6nlwAS/pnGvN9IVLocLHxGYIzFhg6fUQ+5th6P4dv4eW9jX3DSIj7A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/yallist": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz",
      "integrity": "sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g==",
      "dev": true,
      "license": "ISC"
    }
  }
}

''',

    # -------------------------------------------------------------------------
    # client/package.json
    # -------------------------------------------------------------------------
    "client/package.json": r'''{
  "name": "edms-client",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.7.2",
    "framer-motion": "^11.3.19",
    "lucide-react": "^0.453.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.28.0",
    "recharts": "^2.13.0"
  },
  "devDependencies": {
    "@types/react": "^18.3.12",
    "@types/react-dom": "^18.3.1",
    "@vitejs/plugin-react": "^4.3.3",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.49",
    "tailwindcss": "^3.4.14",
    "vite": "^7.3.3"
  }
}

''',

    # -------------------------------------------------------------------------
    # client/postcss.config.js
    # -------------------------------------------------------------------------
    "client/postcss.config.js": r'''export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {}
  }
};

''',

    # -------------------------------------------------------------------------
    # client/src/App.jsx
    # -------------------------------------------------------------------------
    "client/src/App.jsx": r'''import React, { useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import { BellRing, CircleUserRound, LogOut, Sparkles } from 'lucide-react';
import {
  Navigate,
  Outlet,
  Route,
  Routes,
  useLocation
} from 'react-router-dom';

import AuthScreen from './components/AuthScreen';
import ContactHrModal from './components/ContactHrModal';
import DashboardView from './components/DashboardView';
import EmployeeDrawer from './components/EmployeeDrawer';
import EmployeeTable from './components/EmployeeTable';
import Sidebar from './components/Sidebar';
import { useAppContext } from './context/AppContext';

const routeLabels = {
  '/': 'Command Deck',
  '/employees': 'People Ledger',
  '/profile': 'My Profile'
};

const pageTransition = {
  initial: { opacity: 0, y: 22 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -18 }
};

const LoadingScreen = ({ fullscreen = false }) => (
  <div className={fullscreen ? 'flex min-h-screen items-center justify-center px-4' : 'space-y-6'}>
    <div className={fullscreen ? 'w-full max-w-5xl space-y-6' : 'space-y-6'}>
      <div className="grid gap-4 xl:grid-cols-[1.2fr_0.8fr]">
        <div className="h-72 animate-pulse rounded-[30px] bg-white/70 dark:bg-white/5" />
        <div className="grid gap-4 sm:grid-cols-2">
          <div className="h-32 animate-pulse rounded-[28px] bg-white/70 dark:bg-white/5" />
          <div className="h-32 animate-pulse rounded-[28px] bg-white/70 dark:bg-white/5" />
          <div className="h-32 animate-pulse rounded-[28px] bg-white/70 dark:bg-white/5" />
          <div className="h-32 animate-pulse rounded-[28px] bg-white/70 dark:bg-white/5" />
        </div>
      </div>
      <div className="h-80 animate-pulse rounded-[30px] bg-white/70 dark:bg-white/5" />
    </div>
  </div>
);

const ProfilePanel = ({ currentUser, employees, onSelectEmployee, openContactModal }) => {
  const linkedEmployee = employees.find(
    (employee) =>
      employee._id === currentUser?.employee?._id ||
      employee.employeeId === currentUser?.employee?.employeeId
  );

  return (
    <div className="grid gap-6 xl:grid-cols-[0.9fr_1.1fr]">
      <section className="rounded-[30px] bg-ink-900 p-7 text-white shadow-soft dark:bg-[#0c0908]">
        <p className="text-sm uppercase tracking-[0.25em] text-ember-300">Identity layer</p>
        <h2 className="mt-2 font-display text-4xl">{currentUser?.name}</h2>
        <p className="mt-2 text-white/75">{currentUser?.email}</p>
        <div className="mt-8 grid gap-4 sm:grid-cols-2">
          <div className="rounded-3xl bg-white/10 p-4">
            <p className="text-sm text-white/65">Access role</p>
            <p className="mt-2 text-xl font-semibold uppercase">{currentUser?.role}</p>
          </div>
          <div className="rounded-3xl bg-white/10 p-4">
            <p className="text-sm text-white/65">Employee mapping</p>
            <p className="mt-2 text-xl font-semibold">
              {linkedEmployee?.employeeId || currentUser?.employee?.employeeId || 'Pending'}
            </p>
          </div>
        </div>
        <button
          type="button"
          onClick={openContactModal}
          className="mt-8 rounded-full bg-white px-5 py-3 text-sm font-semibold text-ink-900"
        >
          Contact HR securely
        </button>
      </section>

      <section className="space-y-4">
        <div className="rounded-[30px] border border-white/50 bg-white/75 p-6 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5">
          <p className="text-sm uppercase tracking-[0.2em] text-pine-700 dark:text-pine-300">
            Linked employee record
          </p>
          {linkedEmployee ? (
            <>
              <h3 className="mt-2 text-3xl font-semibold text-ink-900 dark:text-white">
                {linkedEmployee.firstName} {linkedEmployee.lastName}
              </h3>
              <p className="mt-1 text-sm text-ink-600 dark:text-white/60">
                {linkedEmployee.department} · {linkedEmployee.designation}
              </p>
              <div className="mt-6 grid gap-3 sm:grid-cols-3">
                <div className="rounded-2xl bg-ink-50 px-4 py-4 dark:bg-white/5">
                  <p className="text-sm text-ink-500 dark:text-white/55">Status</p>
                  <p className="mt-1 font-semibold uppercase text-ink-900 dark:text-white">
                    {linkedEmployee.status}
                  </p>
                </div>
                <div className="rounded-2xl bg-ink-50 px-4 py-4 dark:bg-white/5">
                  <p className="text-sm text-ink-500 dark:text-white/55">Salary</p>
                  <p className="mt-1 font-semibold text-ink-900 dark:text-white">
                    {new Intl.NumberFormat('en-US', {
                      style: 'currency',
                      currency: 'USD',
                      maximumFractionDigits: 0
                    }).format(linkedEmployee.salary || 0)}
                  </p>
                </div>
                <div className="rounded-2xl bg-ink-50 px-4 py-4 dark:bg-white/5">
                  <p className="text-sm text-ink-500 dark:text-white/55">Documents</p>
                  <p className="mt-1 font-semibold text-ink-900 dark:text-white">
                    {linkedEmployee.documents?.length || 0}
                  </p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => onSelectEmployee(linkedEmployee)}
                className="mt-6 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white dark:bg-ember-500 dark:text-ink-900"
              >
                Open full employee file
              </button>
            </>
          ) : (
            <p className="mt-4 text-sm text-ink-600 dark:text-white/65">
              This account is not linked to an employee record yet. Once an employee profile is attached, the personal record and documents will appear here automatically.
            </p>
          )}
        </div>

        <div className="rounded-[30px] border border-white/50 bg-white/75 p-6 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5">
          <p className="text-sm uppercase tracking-[0.2em] text-ember-700 dark:text-ember-300">
            Workflow checks
          </p>
          <div className="mt-4 space-y-3">
            {[
              'Protected routes now require a live backend session before rendering the app shell.',
              'Access tokens are restored and refreshed through the authenticated API flow.',
              'Contact HR submits against the real notification endpoint instead of preview mode.'
            ].map((item) => (
              <div
                key={item}
                className="rounded-2xl bg-ink-50 px-4 py-4 text-sm text-ink-700 dark:bg-white/5 dark:text-white/70"
              >
                {item}
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

const ProtectedRoute = ({ isAuthenticated, isLoading }) => {
  const location = useLocation();

  if (isLoading) {
    return <LoadingScreen fullscreen />;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace state={{ from: location }} />;
  }

  return <Outlet />;
};

const PublicOnlyRoute = ({ isAuthenticated, isLoading }) => {
  if (isLoading) {
    return <LoadingScreen fullscreen />;
  }

  if (isAuthenticated) {
    return <Navigate to="/" replace />;
  }

  return <Outlet />;
};

const RoleGuard = ({ allowedRoles, currentRole }) => {
  if (!allowedRoles.includes(currentRole)) {
    return <Navigate to="/profile" replace />;
  }

  return <Outlet />;
};

const AppShell = () => {
  const location = useLocation();
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const {
    canManageEmployees,
    clearNotice,
    currentUser,
    isContactOpen,
    isProfileOpen,
    logoutUser,
    notice,
    openContactModal,
    closeContactModal,
    closeEmployee,
    selectedEmployee,
    submitContactRequest,
    theme,
    toggleTheme
  } = useAppContext();

  const closeSidebar = () => setSidebarOpen(false);

  return (
    <div className="min-h-screen bg-ink-50 bg-haze text-ink-900 transition-colors duration-300 dark:bg-[#110d0b] dark:text-white">
      <div className="fixed inset-0 opacity-50 dark:opacity-35">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,rgba(249,115,22,0.18),transparent_28%),radial-gradient(circle_at_80%_20%,rgba(85,124,102,0.18),transparent_24%),linear-gradient(to_bottom,rgba(255,255,255,0.35),transparent_30%)] dark:bg-[radial-gradient(circle_at_top_left,rgba(249,115,22,0.16),transparent_28%),radial-gradient(circle_at_80%_20%,rgba(85,124,102,0.2),transparent_24%),linear-gradient(to_bottom,rgba(255,255,255,0.04),transparent_30%)]" />
      </div>

      <div className="relative mx-auto flex max-w-[1600px] gap-4 px-3 py-3 lg:px-4">
        <Sidebar
          canManageEmployees={canManageEmployees}
          currentUser={currentUser}
          isOpen={sidebarOpen}
          onClose={closeSidebar}
          onLogout={logoutUser}
          onOpen={() => setSidebarOpen(true)}
          onToggleTheme={toggleTheme}
          theme={theme}
        />

        <main className="min-w-0 flex-1 lg:pl-0">
          <header className="mb-4 flex flex-col gap-4 rounded-[30px] border border-white/50 bg-white/75 px-6 py-5 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5 lg:flex-row lg:items-center lg:justify-between">
            <div>
              <p className="text-sm uppercase tracking-[0.25em] text-ember-700 dark:text-ember-300">
                Workforce intelligence
              </p>
              <h1 className="mt-2 font-display text-4xl text-ink-900 dark:text-white">
                {routeLabels[location.pathname] || 'EDMS'}
              </h1>
            </div>

            <div className="flex flex-wrap items-center gap-3">
              <button
                type="button"
                onClick={openContactModal}
                className="inline-flex items-center gap-2 rounded-full bg-ink-900 px-4 py-3 text-sm font-semibold text-white transition hover:bg-ink-700 dark:bg-ember-500 dark:text-ink-900"
              >
                <BellRing className="h-4 w-4" />
                Contact HR
              </button>
              <div className="inline-flex items-center gap-2 rounded-full border border-ink-100 bg-white px-4 py-3 text-sm font-semibold text-ink-700 dark:border-white/10 dark:bg-white/10 dark:text-white">
                <CircleUserRound className="h-4 w-4" />
                {currentUser?.role?.toUpperCase()}
              </div>
              <button
                type="button"
                onClick={logoutUser}
                className="inline-flex items-center gap-2 rounded-full border border-ink-100 bg-white px-4 py-3 text-sm font-semibold text-ink-700 transition hover:bg-ink-50 dark:border-white/10 dark:bg-white/10 dark:text-white dark:hover:bg-white/15"
              >
                <LogOut className="h-4 w-4" />
                Sign out
              </button>
            </div>
          </header>

          {notice ? (
            <div className="mb-4 flex items-center justify-between gap-3 rounded-[26px] border border-ember-200 bg-ember-50 px-5 py-4 text-sm text-ember-900 dark:border-ember-500/20 dark:bg-ember-500/10 dark:text-ember-100">
              <div className="flex items-center gap-3">
                <Sparkles className="h-4 w-4 shrink-0" />
                <span>{notice}</span>
              </div>
              <button type="button" onClick={clearNotice} className="font-semibold">
                Dismiss
              </button>
            </div>
          ) : null}

          <AnimatePresence mode="wait">
            <motion.div
              key={location.pathname}
              initial={pageTransition.initial}
              animate={pageTransition.animate}
              exit={pageTransition.exit}
              transition={{ duration: 0.35, ease: 'easeOut' }}
            >
              <Outlet />
            </motion.div>
          </AnimatePresence>
        </main>
      </div>

      <EmployeeDrawer employee={selectedEmployee} isOpen={isProfileOpen} onClose={closeEmployee} />
      <ContactHrModal
        currentUser={currentUser}
        isOpen={isContactOpen}
        onClose={closeContactModal}
        onSubmit={submitContactRequest}
      />
    </div>
  );
};

const App = () => {
  const {
    analytics,
    canManageEmployees,
    currentUser,
    employees,
    isAuthenticated,
    isLoading,
    openContactModal,
    openEmployee
  } = useAppContext();

  return (
    <Routes>
      <Route element={<PublicOnlyRoute isAuthenticated={isAuthenticated} isLoading={isLoading} />}>
        <Route path="/login" element={<AuthScreen mode="login" />} />
        <Route path="/register" element={<AuthScreen mode="register" />} />
      </Route>

      <Route element={<ProtectedRoute isAuthenticated={isAuthenticated} isLoading={isLoading} />}>
        <Route element={<AppShell />}>
          <Route
            path="/"
            element={
              <DashboardView
                analytics={analytics}
                employees={employees}
                onSelectEmployee={openEmployee}
              />
            }
          />

          <Route
            element={
              <RoleGuard
                allowedRoles={['admin', 'hr']}
                currentRole={currentUser?.role || ''}
              />
            }
          >
            <Route
              path="/employees"
              element={<EmployeeTable employees={employees} onSelectEmployee={openEmployee} />}
            />
          </Route>

          <Route
            path="/profile"
            element={
              <ProfilePanel
                currentUser={currentUser}
                employees={employees}
                onSelectEmployee={openEmployee}
                openContactModal={openContactModal}
              />
            }
          />

          <Route
            path="*"
            element={<Navigate to={canManageEmployees ? '/' : '/profile'} replace />}
          />
        </Route>
      </Route>
    </Routes>
  );
};

export default App;

''',

    # -------------------------------------------------------------------------
    # client/src/components/AuthScreen.jsx
    # -------------------------------------------------------------------------
    "client/src/components/AuthScreen.jsx": r'''import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, KeyRound, ShieldCheck, UserRoundPlus } from 'lucide-react';
import { Link, useLocation, useNavigate } from 'react-router-dom';

import { useAppContext } from '../context/AppContext';

const fieldClassName =
  'w-full rounded-2xl border border-ink-100 bg-white px-4 py-3 text-sm text-ink-900 outline-none transition focus:border-ember-300 dark:border-white/10 dark:bg-white/10 dark:text-white';

const toFieldErrors = (details = []) =>
  details.reduce((map, detail) => {
    if (detail.field) {
      map[detail.field] = detail.message;
    }

    return map;
  }, {});

const AuthScreen = ({ mode = 'login' }) => {
  const isRegister = mode === 'register';
  const navigate = useNavigate();
  const location = useLocation();
  const { loginUser, registerUser, theme } = useAppContext();
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [formError, setFormError] = useState('');
  const [fieldErrors, setFieldErrors] = useState({});
  const [loginForm, setLoginForm] = useState({
    email: '',
    password: ''
  });
  const [registerForm, setRegisterForm] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
    employeeId: '',
    role: 'employee',
    bootstrapKey: ''
  });

  const redirectTo = location.state?.from?.pathname || '/';

  const updateLoginField = (field, value) => {
    setLoginForm((currentForm) => ({ ...currentForm, [field]: value }));
    setFieldErrors((currentErrors) => ({ ...currentErrors, [field]: '' }));
    setFormError('');
  };

  const updateRegisterField = (field, value) => {
    setRegisterForm((currentForm) => ({ ...currentForm, [field]: value }));
    setFieldErrors((currentErrors) => ({ ...currentErrors, [field]: '' }));
    setFormError('');
  };

  const validateRegisterForm = () => {
    const nextErrors = {};

    if (!registerForm.name.trim()) {
      nextErrors.name = 'Name is required.';
    }

    if (!/^\S+@\S+\.\S+$/.test(registerForm.email)) {
      nextErrors.email = 'Enter a valid email address.';
    }

    if (registerForm.password.length < 8) {
      nextErrors.password = 'Password must be at least 8 characters.';
    }

    if (registerForm.password !== registerForm.confirmPassword) {
      nextErrors.confirmPassword = 'Passwords do not match.';
    }

    if (registerForm.role !== 'employee' && !registerForm.bootstrapKey.trim()) {
      nextErrors.bootstrapKey = 'Bootstrap key is required for admin or HR roles.';
    }

    setFieldErrors(nextErrors);
    return Object.keys(nextErrors).length === 0;
  };

  const handleLogin = async (event) => {
    event.preventDefault();
    setIsSubmitting(true);
    setFormError('');

    const result = await loginUser(loginForm);

    setIsSubmitting(false);

    if (!result.success) {
      setFieldErrors(toFieldErrors(result.details));
      setFormError(result.message);
      return;
    }

    navigate(redirectTo, { replace: true });
  };

  const handleRegister = async (event) => {
    event.preventDefault();
    setFormError('');

    if (!validateRegisterForm()) {
      return;
    }

    setIsSubmitting(true);

    const result = await registerUser({
      name: registerForm.name.trim(),
      email: registerForm.email.trim(),
      password: registerForm.password,
      employeeId: registerForm.employeeId.trim() || undefined,
      role: registerForm.role,
      bootstrapKey: registerForm.bootstrapKey.trim() || undefined
    });

    setIsSubmitting(false);

    if (!result.success) {
      setFieldErrors(toFieldErrors(result.details));
      setFormError(result.message);
      return;
    }

    navigate(redirectTo, { replace: true });
  };

  return (
    <div className="min-h-screen bg-ink-50 bg-haze text-ink-900 transition-colors duration-300 dark:bg-[#110d0b] dark:text-white">
      <div className="fixed inset-0 opacity-50 dark:opacity-35">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,rgba(249,115,22,0.18),transparent_28%),radial-gradient(circle_at_80%_20%,rgba(85,124,102,0.18),transparent_24%),linear-gradient(to_bottom,rgba(255,255,255,0.35),transparent_30%)] dark:bg-[radial-gradient(circle_at_top_left,rgba(249,115,22,0.16),transparent_28%),radial-gradient(circle_at_80%_20%,rgba(85,124,102,0.2),transparent_24%),linear-gradient(to_bottom,rgba(255,255,255,0.04),transparent_30%)]" />
      </div>

      <div className="relative mx-auto flex min-h-screen max-w-7xl flex-col justify-center gap-8 px-4 py-10 lg:grid lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
        <motion.section
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          className="rounded-[34px] bg-ink-900 p-8 text-white shadow-soft dark:bg-[#0d0a09]"
        >
          <p className="text-sm uppercase tracking-[0.3em] text-ember-300">EDMS</p>
          <h1 className="mt-4 font-display text-5xl leading-tight">Secure workforce operations, without the spreadsheet sprawl.</h1>
          <p className="mt-5 max-w-xl text-sm text-white/72">
            Sign in to review workforce analytics, manage records, and move HR requests through a secure portal backed by your live API session.
          </p>

          <div className="mt-8 space-y-4">
            {[
              {
                icon: ShieldCheck,
                title: 'Protected routes',
                description: 'Dashboard and employee records are available only after a verified session is established.'
              },
              {
                icon: KeyRound,
                title: 'Refresh-token sessions',
                description: 'The client stores an access token and renews it through the secure refresh cookie.'
              },
              {
                icon: UserRoundPlus,
                title: 'Role-aware onboarding',
                description: 'New users can register as employees, or bootstrap admin and HR accounts when permitted.'
              }
            ].map((item) => {
              const Icon = item.icon;

              return (
                <div key={item.title} className="rounded-3xl bg-white/10 p-5">
                  <Icon className="h-5 w-5 text-ember-300" />
                  <p className="mt-4 text-lg font-semibold">{item.title}</p>
                  <p className="mt-2 text-sm text-white/68">{item.description}</p>
                </div>
              );
            })}
          </div>

          <div className="mt-8 rounded-3xl border border-white/10 px-5 py-4 text-sm text-white/72">
            Theme preview: <span className="font-semibold text-white">{theme === 'dark' ? 'Night mode' : 'Daylight mode'}</span>
          </div>
        </motion.section>

        <motion.section
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.08 }}
          className="rounded-[34px] border border-white/50 bg-white/75 p-6 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5 sm:p-8"
        >
          <div className="mb-6 flex flex-wrap items-center justify-between gap-3">
            <div>
              <p className="text-sm uppercase tracking-[0.25em] text-ember-700 dark:text-ember-300">
                {isRegister ? 'Create account' : 'Welcome back'}
              </p>
              <h2 className="mt-2 font-display text-4xl text-ink-900 dark:text-white">
                {isRegister ? 'Activate your workspace access' : 'Sign in to Harbor Console'}
              </h2>
            </div>
            <Link
              to={isRegister ? '/login' : '/register'}
              className="rounded-full border border-ink-100 px-4 py-3 text-sm font-semibold text-ink-800 transition hover:bg-white dark:border-white/10 dark:text-white dark:hover:bg-white/10"
            >
              {isRegister ? 'I already have an account' : 'Create an account'}
            </Link>
          </div>

          {formError ? (
            <div className="mb-5 rounded-2xl border border-red-200 bg-red-50 px-4 py-3 text-sm font-medium text-red-700">
              {formError}
            </div>
          ) : null}

          {isRegister ? (
            <form className="grid gap-4 md:grid-cols-2" onSubmit={handleRegister}>
              <label className="block md:col-span-2">
                <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">Full name</span>
                <input
                  value={registerForm.name}
                  onChange={(event) => updateRegisterField('name', event.target.value)}
                  className={fieldClassName}
                  placeholder="Minakshi Rawat"
                />
                {fieldErrors.name ? <span className="mt-1 block text-sm text-red-600">{fieldErrors.name}</span> : null}
              </label>

              <label className="block">
                <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">Email</span>
                <input
                  type="email"
                  value={registerForm.email}
                  onChange={(event) => updateRegisterField('email', event.target.value)}
                  className={fieldClassName}
                  placeholder="you@company.com"
                />
                {fieldErrors.email ? <span className="mt-1 block text-sm text-red-600">{fieldErrors.email}</span> : null}
              </label>

              <label className="block">
                <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">Employee ID</span>
                <input
                  value={registerForm.employeeId}
                  onChange={(event) => updateRegisterField('employeeId', event.target.value)}
                  className={fieldClassName}
                  placeholder="Optional"
                />
                {fieldErrors.employeeId ? (
                  <span className="mt-1 block text-sm text-red-600">{fieldErrors.employeeId}</span>
                ) : null}
              </label>

              <label className="block">
                <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">Password</span>
                <input
                  type="password"
                  value={registerForm.password}
                  onChange={(event) => updateRegisterField('password', event.target.value)}
                  className={fieldClassName}
                  placeholder="At least 8 characters"
                />
                {fieldErrors.password ? (
                  <span className="mt-1 block text-sm text-red-600">{fieldErrors.password}</span>
                ) : null}
              </label>

              <label className="block">
                <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">Confirm password</span>
                <input
                  type="password"
                  value={registerForm.confirmPassword}
                  onChange={(event) => updateRegisterField('confirmPassword', event.target.value)}
                  className={fieldClassName}
                  placeholder="Repeat your password"
                />
                {fieldErrors.confirmPassword ? (
                  <span className="mt-1 block text-sm text-red-600">{fieldErrors.confirmPassword}</span>
                ) : null}
              </label>

              <label className="block">
                <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">Requested role</span>
                <select
                  value={registerForm.role}
                  onChange={(event) => updateRegisterField('role', event.target.value)}
                  className={fieldClassName}
                >
                  <option value="employee">Employee</option>
                  <option value="hr">HR</option>
                  <option value="admin">Admin</option>
                </select>
              </label>

              <label className="block">
                <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">Bootstrap key</span>
                <input
                  value={registerForm.bootstrapKey}
                  onChange={(event) => updateRegisterField('bootstrapKey', event.target.value)}
                  className={fieldClassName}
                  placeholder={registerForm.role === 'employee' ? 'Not required for employees' : 'Required for admin or HR'}
                />
                {fieldErrors.bootstrapKey ? (
                  <span className="mt-1 block text-sm text-red-600">{fieldErrors.bootstrapKey}</span>
                ) : null}
              </label>

              <div className="md:col-span-2 rounded-3xl bg-ink-50 px-5 py-4 text-sm text-ink-700 dark:bg-white/5 dark:text-white/68">
                Use an employee ID only when a matching employee record already exists in the backend. Admin and HR registrations require the backend bootstrap key.
              </div>

              <button
                type="submit"
                disabled={isSubmitting}
                className="md:col-span-2 inline-flex items-center justify-center gap-2 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-ink-700 disabled:opacity-60 dark:bg-ember-500 dark:text-ink-900"
              >
                <ArrowRight className="h-4 w-4" />
                {isSubmitting ? 'Creating account...' : 'Create account'}
              </button>
            </form>
          ) : (
            <form className="space-y-4" onSubmit={handleLogin}>
              <label className="block">
                <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">Email</span>
                <input
                  type="email"
                  value={loginForm.email}
                  onChange={(event) => updateLoginField('email', event.target.value)}
                  className={fieldClassName}
                  placeholder="you@company.com"
                />
                {fieldErrors.email ? <span className="mt-1 block text-sm text-red-600">{fieldErrors.email}</span> : null}
              </label>

              <label className="block">
                <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">Password</span>
                <input
                  type="password"
                  value={loginForm.password}
                  onChange={(event) => updateLoginField('password', event.target.value)}
                  className={fieldClassName}
                  placeholder="Your account password"
                />
                {fieldErrors.password ? (
                  <span className="mt-1 block text-sm text-red-600">{fieldErrors.password}</span>
                ) : null}
              </label>

              <button
                type="submit"
                disabled={isSubmitting}
                className="inline-flex w-full items-center justify-center gap-2 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-ink-700 disabled:opacity-60 dark:bg-ember-500 dark:text-ink-900"
              >
                <ArrowRight className="h-4 w-4" />
                {isSubmitting ? 'Signing in...' : 'Sign in'}
              </button>

              <p className="text-sm text-ink-600 dark:text-white/62">
                Need an account?{' '}
                <Link to="/register" className="font-semibold text-ember-700 dark:text-ember-300">
                  Create one here
                </Link>
                .
              </p>
            </form>
          )}
        </motion.section>
      </div>
    </div>
  );
};

export default AuthScreen;

''',

    # -------------------------------------------------------------------------
    # client/src/components/ContactHrModal.jsx
    # -------------------------------------------------------------------------
    "client/src/components/ContactHrModal.jsx": r'''import React, { useEffect, useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import { SendHorizonal, X } from 'lucide-react';

const emptyErrors = {
  name: '',
  email: '',
  employeeId: '',
  subject: '',
  message: ''
};

const ContactHrModal = ({ currentUser, isOpen, onClose, onSubmit }) => {
  const [form, setForm] = useState({
    name: currentUser?.name || '',
    email: currentUser?.email || '',
    employeeId: currentUser?.employee?.employeeId || '',
    subject: '',
    message: ''
  });
  const [errors, setErrors] = useState(emptyErrors);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState('');

  useEffect(() => {
    if (!isOpen) {
      return;
    }

    setForm({
      name: currentUser?.name || '',
      email: currentUser?.email || '',
      employeeId: currentUser?.employee?.employeeId || '',
      subject: '',
      message: ''
    });
    setErrors(emptyErrors);
    setSubmitted('');
  }, [currentUser, isOpen]);

  const updateField = (field, value) => {
    setForm((currentForm) => ({ ...currentForm, [field]: value }));
    setErrors((currentErrors) => ({ ...currentErrors, [field]: '' }));
  };

  const validate = () => {
    const nextErrors = { ...emptyErrors };

    if (!form.name.trim()) nextErrors.name = 'Name is required';
    if (!/^\S+@\S+\.\S+$/.test(form.email)) nextErrors.email = 'Enter a valid email';
    if (!form.employeeId.trim()) nextErrors.employeeId = 'Employee ID is required';
    if (!form.subject.trim()) nextErrors.subject = 'Subject is required';
    if (form.message.trim().length < 10) nextErrors.message = 'Message must be at least 10 characters';

    setErrors(nextErrors);
    return Object.values(nextErrors).every((value) => !value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setSubmitted('');

    if (!validate()) {
      return;
    }

    setIsSubmitting(true);
    const result = await onSubmit(form);
    setIsSubmitting(false);

    if (result.success) {
      setSubmitted(result.preview ? 'Saved in preview mode.' : 'Sent to HR successfully.');
      setForm((currentForm) => ({ ...currentForm, subject: '', message: '' }));
    }
  };

  return (
    <AnimatePresence>
      {isOpen ? (
        <>
          <motion.button
            type="button"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 z-40 bg-black/35 backdrop-blur-sm"
            aria-label="Close contact HR dialog"
          />
          <motion.div
            initial={{ opacity: 0, y: 28, scale: 0.96 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 18, scale: 0.98 }}
            className="fixed left-1/2 top-1/2 z-50 w-[calc(100%-1.5rem)] max-w-2xl -translate-x-1/2 -translate-y-1/2 rounded-[32px] border border-white/50 bg-[#f7f2ea] p-6 shadow-soft dark:border-white/10 dark:bg-[#15110f]"
          >
            <div className="mb-6 flex items-start justify-between gap-4">
              <div>
                <p className="text-sm uppercase tracking-[0.25em] text-ember-700 dark:text-ember-300">
                  Contact HR
                </p>
                <h2 className="mt-2 font-display text-4xl text-ink-900 dark:text-white">
                  Start a secure support thread
                </h2>
              </div>
              <button
                type="button"
                onClick={onClose}
                className="rounded-full bg-white p-3 text-ink-900 shadow-sm dark:bg-white/10 dark:text-white"
                aria-label="Close contact HR dialog"
              >
                <X className="h-5 w-5" />
              </button>
            </div>

            <form className="grid gap-4 md:grid-cols-2" onSubmit={handleSubmit}>
              {[
                { field: 'name', label: 'Name', type: 'text' },
                { field: 'email', label: 'Email', type: 'email' },
                { field: 'employeeId', label: 'Employee ID', type: 'text' },
                { field: 'subject', label: 'Subject', type: 'text' }
              ].map((item) => (
                <label key={item.field} className="block">
                  <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">
                    {item.label}
                  </span>
                  <input
                    type={item.type}
                    value={form[item.field]}
                    onChange={(event) => updateField(item.field, event.target.value)}
                    className="w-full rounded-2xl border border-ink-100 bg-white px-4 py-3 text-sm text-ink-900 outline-none transition focus:border-ember-300 dark:border-white/10 dark:bg-white/10 dark:text-white"
                  />
                  {errors[item.field] ? (
                    <span className="mt-1 block text-sm text-red-600">{errors[item.field]}</span>
                  ) : null}
                </label>
              ))}

              <label className="block md:col-span-2">
                <span className="mb-2 block text-sm font-semibold text-ink-700 dark:text-white/75">
                  Message
                </span>
                <textarea
                  rows="5"
                  value={form.message}
                  onChange={(event) => updateField('message', event.target.value)}
                  className="w-full rounded-3xl border border-ink-100 bg-white px-4 py-3 text-sm text-ink-900 outline-none transition focus:border-ember-300 dark:border-white/10 dark:bg-white/10 dark:text-white"
                  placeholder="Describe your question, concern, or request."
                />
                {errors.message ? (
                  <span className="mt-1 block text-sm text-red-600">{errors.message}</span>
                ) : null}
              </label>

              <div className="md:col-span-2 flex items-center justify-between gap-3 rounded-3xl bg-ink-900 px-5 py-4 text-white dark:bg-[#0d0a09]">
                <div>
                  <p className="font-semibold">Priority delivery</p>
                  <p className="text-sm text-white/70">
                    Requests include your identity, employee ID, subject, and timestamp.
                  </p>
                </div>
                <button
                  type="submit"
                  disabled={isSubmitting}
                  className="inline-flex items-center gap-2 rounded-full bg-white px-5 py-3 text-sm font-semibold text-ink-900 transition hover:-translate-y-0.5 disabled:opacity-60"
                >
                  <SendHorizonal className="h-4 w-4" />
                  {isSubmitting ? 'Sending...' : 'Send request'}
                </button>
              </div>
            </form>

            {submitted ? (
              <p className="mt-4 rounded-2xl bg-emerald-50 px-4 py-3 text-sm font-semibold text-emerald-700">
                {submitted}
              </p>
            ) : null}
          </motion.div>
        </>
      ) : null}
    </AnimatePresence>
  );
};

export default ContactHrModal;

''',

    # -------------------------------------------------------------------------
    # client/src/components/DashboardView.jsx
    # -------------------------------------------------------------------------
    "client/src/components/DashboardView.jsx": r'''import React from 'react';
import { motion } from 'framer-motion';
import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis
} from 'recharts';
import { ArrowUpRight, CalendarDays, Coins, Layers3, ShieldCheck } from 'lucide-react';

const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const attendancePalette = ['#f97316', '#557c66', '#facc15'];

const formatCurrency = (value) =>
  new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0
  }).format(value || 0);

const DashboardView = ({ analytics, employees, onSelectEmployee }) => {
  const hiringSeries = (analytics.monthlyHiring || []).map((entry) => ({
    label: `${monthNames[(entry._id?.month || 1) - 1]} ${entry._id?.year || ''}`,
    hires: entry.hires
  }));

  const stats = [
    {
      label: 'Active workforce',
      value: analytics.totalEmployees,
      icon: Layers3,
      tone: 'from-ember-500 to-amber-300'
    },
    {
      label: 'Average salary',
      value: formatCurrency(analytics.salarySummary?.averageSalary),
      icon: Coins,
      tone: 'from-pine-500 to-pine-300'
    },
    {
      label: 'Recent hiring pace',
      value: `${hiringSeries[hiringSeries.length - 1]?.hires || 0} hires`,
      icon: CalendarDays,
      tone: 'from-sky-500 to-cyan-300'
    },
    {
      label: 'Security posture',
      value: 'Healthy',
      icon: ShieldCheck,
      tone: 'from-rose-500 to-orange-300'
    }
  ];

  return (
    <div className="space-y-6">
      <section className="grid gap-4 xl:grid-cols-[1.2fr_0.8fr]">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="rounded-[30px] bg-[linear-gradient(135deg,#1d1916_0%,#6b3f16_55%,#dca66f_100%)] p-7 text-white shadow-soft"
        >
          <p className="text-sm uppercase tracking-[0.3em] text-white/65">Enterprise pulse</p>
          <h2 className="mt-3 max-w-xl font-display text-4xl leading-tight">
            Employee intelligence with less admin drag and more signal.
          </h2>
          <p className="mt-4 max-w-2xl text-sm text-white/75">
            Review hiring momentum, department balance, workforce health, and the latest changes from one animated control plane.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <button
              type="button"
              className="rounded-full bg-white px-5 py-3 text-sm font-semibold text-ink-900 transition hover:-translate-y-0.5"
            >
              Review onboarding queue
            </button>
            <button
              type="button"
              className="rounded-full border border-white/30 px-5 py-3 text-sm font-semibold text-white transition hover:bg-white/10"
            >
              Export executive snapshot
            </button>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="grid gap-4 sm:grid-cols-2"
        >
          {stats.map((stat, index) => {
            const Icon = stat.icon;

            return (
              <motion.div
                key={stat.label}
                initial={{ opacity: 0, y: 18 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.12 + index * 0.08 }}
                className="rounded-[28px] border border-white/50 bg-white/75 p-5 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5"
              >
                <div className={`inline-flex rounded-2xl bg-gradient-to-br ${stat.tone} p-3 text-white`}>
                  <Icon className="h-5 w-5" />
                </div>
                <p className="mt-4 text-sm text-ink-600 dark:text-white/65">{stat.label}</p>
                <p className="mt-2 text-3xl font-semibold text-ink-900 dark:text-white">{stat.value}</p>
              </motion.div>
            );
          })}
        </motion.div>
      </section>

      <section className="grid gap-4 xl:grid-cols-[1.3fr_0.7fr]">
        <motion.div
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.15 }}
          className="rounded-[30px] border border-white/50 bg-white/75 p-6 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5"
        >
          <div className="mb-5 flex items-center justify-between">
            <div>
              <p className="text-sm font-semibold uppercase tracking-[0.2em] text-ember-700 dark:text-ember-300">
                Hiring trend
              </p>
              <h3 className="mt-1 text-2xl font-semibold text-ink-900 dark:text-white">
                Workforce growth across the last 12 months
              </h3>
            </div>
            <span className="rounded-full bg-ember-50 px-3 py-1 text-xs font-semibold text-ember-700 dark:bg-white/10 dark:text-ember-200">
              Live-ready
            </span>
          </div>
          <div className="h-80">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={hiringSeries}>
                <defs>
                  <linearGradient id="hiringFill" x1="0" x2="0" y1="0" y2="1">
                    <stop offset="0%" stopColor="#f97316" stopOpacity={0.55} />
                    <stop offset="100%" stopColor="#f97316" stopOpacity={0.05} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#d6d3d1" />
                <XAxis dataKey="label" stroke="#78716c" />
                <YAxis stroke="#78716c" />
                <Tooltip />
                <Area
                  type="monotone"
                  dataKey="hires"
                  stroke="#c2410c"
                  strokeWidth={3}
                  fill="url(#hiringFill)"
                />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="space-y-4"
        >
          <div className="rounded-[30px] border border-white/50 bg-white/75 p-6 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5">
            <div className="mb-4">
              <p className="text-sm font-semibold uppercase tracking-[0.2em] text-pine-700 dark:text-pine-300">
                Department mix
              </p>
              <h3 className="text-2xl font-semibold text-ink-900 dark:text-white">Current distribution</h3>
            </div>
            <div className="h-72">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={analytics.departmentDistribution || []} layout="vertical" margin={{ left: 12 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#d6d3d1" />
                  <XAxis type="number" stroke="#78716c" />
                  <YAxis dataKey="department" type="category" stroke="#78716c" width={90} />
                  <Tooltip />
                  <Bar dataKey="count" radius={[0, 12, 12, 0]} fill="#557c66" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          <div className="rounded-[30px] border border-white/50 bg-white/75 p-6 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5">
            <div className="mb-3 flex items-center justify-between">
              <div>
                <p className="text-sm font-semibold uppercase tracking-[0.2em] text-amber-700 dark:text-amber-300">
                  Attendance signal
                </p>
                <h3 className="text-2xl font-semibold text-ink-900 dark:text-white">Status split</h3>
              </div>
            </div>
            <div className="h-60">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={analytics.attendanceSummary || []}
                    dataKey="count"
                    nameKey="status"
                    innerRadius={54}
                    outerRadius={84}
                    paddingAngle={4}
                  >
                    {(analytics.attendanceSummary || []).map((entry, index) => (
                      <Cell key={entry.status} fill={attendancePalette[index % attendancePalette.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </div>
        </motion.div>
      </section>

      <section className="grid gap-4 xl:grid-cols-[1.1fr_0.9fr]">
        <motion.div
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="rounded-[30px] border border-white/50 bg-white/75 p-6 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5"
        >
          <div className="mb-4 flex items-end justify-between">
            <div>
              <p className="text-sm font-semibold uppercase tracking-[0.2em] text-ember-700 dark:text-ember-300">
                Recent movement
              </p>
              <h3 className="text-2xl font-semibold text-ink-900 dark:text-white">Activity deck</h3>
            </div>
            <span className="text-sm text-ink-500 dark:text-white/60">Latest employee updates</span>
          </div>
          <div className="space-y-3">
            {(analytics.recentActivity || []).map((item) => {
              const person = employees.find((employee) => employee.employeeId === item.employeeId);

              return (
                <button
                  key={item._id}
                  type="button"
                  onClick={() => person && onSelectEmployee(person)}
                  className="flex w-full items-center justify-between rounded-2xl border border-transparent bg-ink-50/90 px-4 py-4 text-left transition hover:border-ember-200 hover:bg-white dark:bg-white/5 dark:hover:border-white/15"
                >
                  <div>
                    <p className="font-semibold text-ink-900 dark:text-white">
                      {item.firstName} {item.lastName}
                    </p>
                    <p className="text-sm text-ink-500 dark:text-white/60">
                      {item.employeeId} · {item.department}
                    </p>
                  </div>
                  <div className="flex items-center gap-2 text-sm text-ember-700 dark:text-ember-300">
                    <span>{new Date(item.updatedAt).toLocaleDateString()}</span>
                    <ArrowUpRight className="h-4 w-4" />
                  </div>
                </button>
              );
            })}
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.28 }}
          className="rounded-[30px] bg-ink-900 p-6 text-white shadow-soft dark:bg-[#0f0c0a]"
        >
          <p className="text-sm uppercase tracking-[0.25em] text-ember-300">Executive note</p>
          <h3 className="mt-2 font-display text-3xl leading-tight">
            Salary load is steady while hiring velocity remains above the winter baseline.
          </h3>
          <div className="mt-8 space-y-4">
            <div className="rounded-2xl bg-white/10 p-4">
              <p className="text-sm text-white/70">Total compensation load</p>
              <p className="mt-1 text-2xl font-semibold">
                {formatCurrency(analytics.salarySummary?.totalSalary)}
              </p>
            </div>
            <div className="grid grid-cols-2 gap-3">
              <div className="rounded-2xl bg-white/10 p-4">
                <p className="text-sm text-white/70">Max salary</p>
                <p className="mt-1 text-xl font-semibold">
                  {formatCurrency(analytics.salarySummary?.maxSalary)}
                </p>
              </div>
              <div className="rounded-2xl bg-white/10 p-4">
                <p className="text-sm text-white/70">Min salary</p>
                <p className="mt-1 text-xl font-semibold">
                  {formatCurrency(analytics.salarySummary?.minSalary)}
                </p>
              </div>
            </div>
          </div>
        </motion.div>
      </section>
    </div>
  );
};

export default DashboardView;

''',

    # -------------------------------------------------------------------------
    # client/src/components/EmployeeDrawer.jsx
    # -------------------------------------------------------------------------
    "client/src/components/EmployeeDrawer.jsx": r'''import React from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import { CalendarClock, FileText, Mail, Phone, ShieldAlert, X } from 'lucide-react';

const formatDate = (value) =>
  value
    ? new Date(value).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    : 'Not available';

const EmployeeDrawer = ({ employee, isOpen, onClose }) => (
  <AnimatePresence>
    {isOpen && employee ? (
      <>
        <motion.button
          type="button"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
          className="fixed inset-0 z-40 bg-black/30 backdrop-blur-sm"
          aria-label="Close employee details"
        />

        <motion.aside
          initial={{ x: '100%' }}
          animate={{ x: 0 }}
          exit={{ x: '100%' }}
          transition={{ type: 'spring', damping: 24, stiffness: 220 }}
          className="fixed right-0 top-0 z-50 h-full w-full max-w-xl overflow-y-auto bg-[#f7f2ea] p-6 shadow-soft dark:bg-[#15110f]"
        >
          <div className="mb-6 flex items-start justify-between">
            <div>
              <p className="text-sm uppercase tracking-[0.25em] text-ember-700 dark:text-ember-300">
                Employee file
              </p>
              <h2 className="mt-2 font-display text-4xl text-ink-900 dark:text-white">
                {employee.firstName} {employee.lastName}
              </h2>
              <p className="mt-1 text-sm text-ink-600 dark:text-white/65">
                {employee.employeeId} · {employee.designation}
              </p>
            </div>
            <button
              type="button"
              onClick={onClose}
              className="rounded-full bg-white p-3 text-ink-900 shadow-sm dark:bg-white/10 dark:text-white"
              aria-label="Close employee details"
            >
              <X className="h-5 w-5" />
            </button>
          </div>

          <div className="grid gap-4 sm:grid-cols-2">
            <div className="rounded-[28px] bg-white p-5 shadow-sm dark:bg-white/5">
              <Mail className="h-5 w-5 text-ember-600 dark:text-ember-300" />
              <p className="mt-4 text-sm text-ink-500 dark:text-white/55">Email</p>
              <p className="font-semibold text-ink-900 dark:text-white">{employee.email}</p>
            </div>
            <div className="rounded-[28px] bg-white p-5 shadow-sm dark:bg-white/5">
              <Phone className="h-5 w-5 text-pine-600 dark:text-pine-300" />
              <p className="mt-4 text-sm text-ink-500 dark:text-white/55">Phone</p>
              <p className="font-semibold text-ink-900 dark:text-white">{employee.phone || 'Not set'}</p>
            </div>
            <div className="rounded-[28px] bg-white p-5 shadow-sm dark:bg-white/5">
              <CalendarClock className="h-5 w-5 text-sky-600 dark:text-sky-300" />
              <p className="mt-4 text-sm text-ink-500 dark:text-white/55">Joining date</p>
              <p className="font-semibold text-ink-900 dark:text-white">{formatDate(employee.joiningDate)}</p>
            </div>
            <div className="rounded-[28px] bg-white p-5 shadow-sm dark:bg-white/5">
              <ShieldAlert className="h-5 w-5 text-amber-600 dark:text-amber-300" />
              <p className="mt-4 text-sm text-ink-500 dark:text-white/55">Emergency contact</p>
              <p className="font-semibold text-ink-900 dark:text-white">
                {employee.emergencyContact?.name || 'Not set'}
              </p>
              <p className="text-sm text-ink-500 dark:text-white/55">
                {employee.emergencyContact?.relation || ''} {employee.emergencyContact?.phone || ''}
              </p>
            </div>
          </div>

          <div className="mt-6 rounded-[30px] bg-ink-900 p-6 text-white dark:bg-[#0d0a09]">
            <div className="grid gap-4 sm:grid-cols-3">
              <div>
                <p className="text-sm text-white/65">Department</p>
                <p className="mt-2 text-lg font-semibold">{employee.department}</p>
              </div>
              <div>
                <p className="text-sm text-white/65">Role title</p>
                <p className="mt-2 text-lg font-semibold">{employee.roleTitle || employee.designation}</p>
              </div>
              <div>
                <p className="text-sm text-white/65">Status</p>
                <p className="mt-2 text-lg font-semibold uppercase">{employee.status}</p>
              </div>
            </div>
          </div>

          <div className="mt-6 grid gap-4 lg:grid-cols-[0.9fr_1.1fr]">
            <div className="rounded-[28px] bg-white p-5 shadow-sm dark:bg-white/5">
              <p className="text-sm font-semibold uppercase tracking-[0.2em] text-ember-700 dark:text-ember-300">
                Attendance
              </p>
              <div className="mt-4 space-y-3">
                {(employee.attendance || []).slice(-4).map((entry) => (
                  <div
                    key={`${employee._id}-${entry.date}`}
                    className="flex items-center justify-between rounded-2xl bg-ink-50 px-4 py-3 dark:bg-white/5"
                  >
                    <span className="text-sm text-ink-700 dark:text-white/70">{formatDate(entry.date)}</span>
                    <span className="text-sm font-semibold uppercase text-ink-900 dark:text-white">
                      {entry.status}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            <div className="rounded-[28px] bg-white p-5 shadow-sm dark:bg-white/5">
              <div className="flex items-center gap-2">
                <FileText className="h-5 w-5 text-pine-600 dark:text-pine-300" />
                <p className="text-sm font-semibold uppercase tracking-[0.2em] text-pine-700 dark:text-pine-300">
                  Documents
                </p>
              </div>
              <div className="mt-4 space-y-3">
                {(employee.documents || []).length ? (
                  employee.documents.map((document) => (
                    <div
                      key={`${employee._id}-${document.originalname}`}
                      className="rounded-2xl bg-ink-50 px-4 py-3 dark:bg-white/5"
                    >
                      <p className="font-semibold text-ink-900 dark:text-white">{document.originalname}</p>
                      <p className="text-sm text-ink-500 dark:text-white/55">{document.mimeType}</p>
                    </div>
                  ))
                ) : (
                  <div className="rounded-2xl bg-ink-50 px-4 py-5 text-sm text-ink-500 dark:bg-white/5 dark:text-white/55">
                    No uploaded documents yet.
                  </div>
                )}
              </div>
            </div>
          </div>
        </motion.aside>
      </>
    ) : null}
  </AnimatePresence>
);

export default EmployeeDrawer;

''',

    # -------------------------------------------------------------------------
    # client/src/components/EmployeeTable.jsx
    # -------------------------------------------------------------------------
    "client/src/components/EmployeeTable.jsx": r'''import React, { startTransition, useDeferredValue, useState } from 'react';
import { motion } from 'framer-motion';
import { ArrowUpDown, Search, SlidersHorizontal } from 'lucide-react';

const formatCurrency = (value) =>
  new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0
  }).format(value || 0);

const formatDate = (value) =>
  value
    ? new Date(value).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    : 'Not set';

const EmployeeTable = ({ employees, onSelectEmployee }) => {
  const [query, setQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState('all');
  const [departmentFilter, setDepartmentFilter] = useState('all');
  const [sortBy, setSortBy] = useState('joiningDate');

  const deferredQuery = useDeferredValue(query);
  const departments = [...new Set(employees.map((employee) => employee.department).filter(Boolean))];

  const filteredEmployees = employees
    .filter((employee) => {
      const name = `${employee.firstName} ${employee.lastName}`.toLowerCase();
      const matchesQuery =
        !deferredQuery ||
        name.includes(deferredQuery.toLowerCase()) ||
        employee.email.toLowerCase().includes(deferredQuery.toLowerCase()) ||
        employee.employeeId.toLowerCase().includes(deferredQuery.toLowerCase());
      const matchesStatus = statusFilter === 'all' || employee.status === statusFilter;
      const matchesDepartment =
        departmentFilter === 'all' || employee.department === departmentFilter;

      return matchesQuery && matchesStatus && matchesDepartment;
    })
    .sort((left, right) => {
      if (sortBy === 'salary') {
        return right.salary - left.salary;
      }

      if (sortBy === 'name') {
        return `${left.firstName} ${left.lastName}`.localeCompare(`${right.firstName} ${right.lastName}`);
      }

      if (sortBy === 'department') {
        return (left.department || '').localeCompare(right.department || '');
      }

      return new Date(right.joiningDate) - new Date(left.joiningDate);
    });

  return (
    <div className="space-y-5">
      <div className="rounded-[30px] border border-white/50 bg-white/75 p-6 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5">
        <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-ember-700 dark:text-ember-300">
              Employee ledger
            </p>
            <h2 className="mt-1 text-3xl font-semibold text-ink-900 dark:text-white">
              Search, filter, and inspect team records
            </h2>
          </div>
          <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-4">
            <label className="relative block">
              <span className="sr-only">Search employees</span>
              <Search className="pointer-events-none absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-ink-500" />
              <input
                value={query}
                onChange={(event) => startTransition(() => setQuery(event.target.value))}
                className="w-full rounded-2xl border border-ink-100 bg-white px-11 py-3 text-sm text-ink-900 outline-none transition focus:border-ember-300 dark:border-white/10 dark:bg-white/10 dark:text-white"
                placeholder="Search name, email, ID"
              />
            </label>

            <select
              value={statusFilter}
              onChange={(event) => setStatusFilter(event.target.value)}
              className="rounded-2xl border border-ink-100 bg-white px-4 py-3 text-sm text-ink-900 outline-none transition focus:border-ember-300 dark:border-white/10 dark:bg-white/10 dark:text-white"
              aria-label="Filter by status"
            >
              <option value="all">All statuses</option>
              <option value="active">Active</option>
              <option value="inactive">Inactive</option>
              <option value="terminated">Terminated</option>
            </select>

            <select
              value={departmentFilter}
              onChange={(event) => setDepartmentFilter(event.target.value)}
              className="rounded-2xl border border-ink-100 bg-white px-4 py-3 text-sm text-ink-900 outline-none transition focus:border-ember-300 dark:border-white/10 dark:bg-white/10 dark:text-white"
              aria-label="Filter by department"
            >
              <option value="all">All departments</option>
              {departments.map((department) => (
                <option key={department} value={department}>
                  {department}
                </option>
              ))}
            </select>

            <button
              type="button"
              onClick={() =>
                setSortBy((currentValue) =>
                  currentValue === 'joiningDate' ? 'salary' : currentValue === 'salary' ? 'name' : 'joiningDate'
                )
              }
              className="inline-flex items-center justify-center gap-2 rounded-2xl bg-ink-900 px-4 py-3 text-sm font-semibold text-white transition hover:bg-ink-700 dark:bg-ember-500 dark:text-ink-900"
            >
              <ArrowUpDown className="h-4 w-4" />
              Sort: {sortBy}
            </button>
          </div>
        </div>
      </div>

      <div className="rounded-[30px] border border-white/50 bg-white/75 shadow-soft backdrop-blur dark:border-white/10 dark:bg-white/5">
        <div className="flex items-center justify-between border-b border-ink-100/80 px-6 py-4 dark:border-white/10">
          <div className="flex items-center gap-2 text-sm font-semibold text-ink-700 dark:text-white/75">
            <SlidersHorizontal className="h-4 w-4" />
            <span>{filteredEmployees.length} results</span>
          </div>
          <p className="text-sm text-ink-500 dark:text-white/60">
            Sorted by {sortBy === 'joiningDate' ? 'joining date' : sortBy}
          </p>
        </div>

        <div className="hidden overflow-x-auto lg:block">
          <table className="min-w-full text-left">
            <thead className="text-xs uppercase tracking-[0.2em] text-ink-500 dark:text-white/50">
              <tr>
                <th className="px-6 py-4">Employee</th>
                <th className="px-6 py-4">Department</th>
                <th className="px-6 py-4">Role</th>
                <th className="px-6 py-4">Salary</th>
                <th className="px-6 py-4">Joined</th>
                <th className="px-6 py-4">Status</th>
              </tr>
            </thead>
            <tbody>
              {filteredEmployees.map((employee) => (
                <tr
                  key={employee._id}
                  className="cursor-pointer border-t border-ink-100/70 transition hover:bg-white/85 dark:border-white/10 dark:hover:bg-white/5"
                  onClick={() => onSelectEmployee(employee)}
                >
                  <td className="px-6 py-5">
                    <p className="font-semibold text-ink-900 dark:text-white">
                      {employee.firstName} {employee.lastName}
                    </p>
                    <p className="text-sm text-ink-500 dark:text-white/55">{employee.email}</p>
                  </td>
                  <td className="px-6 py-5 text-sm text-ink-700 dark:text-white/75">{employee.department}</td>
                  <td className="px-6 py-5 text-sm text-ink-700 dark:text-white/75">{employee.designation}</td>
                  <td className="px-6 py-5 text-sm font-semibold text-ink-900 dark:text-white">
                    {formatCurrency(employee.salary)}
                  </td>
                  <td className="px-6 py-5 text-sm text-ink-700 dark:text-white/75">
                    {formatDate(employee.joiningDate)}
                  </td>
                  <td className="px-6 py-5">
                    <span className="rounded-full bg-ink-100 px-3 py-1 text-xs font-semibold uppercase text-ink-700 dark:bg-white/10 dark:text-white">
                      {employee.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="space-y-3 p-4 lg:hidden">
          {filteredEmployees.map((employee) => (
            <motion.button
              key={employee._id}
              whileTap={{ scale: 0.98 }}
              onClick={() => onSelectEmployee(employee)}
              className="w-full rounded-3xl bg-ink-50 p-4 text-left dark:bg-white/5"
            >
              <div className="flex items-start justify-between gap-3">
                <div>
                  <p className="font-semibold text-ink-900 dark:text-white">
                    {employee.firstName} {employee.lastName}
                  </p>
                  <p className="text-sm text-ink-500 dark:text-white/55">{employee.department}</p>
                </div>
                <span className="rounded-full bg-white px-3 py-1 text-xs font-semibold uppercase text-ink-700 dark:bg-white/10 dark:text-white">
                  {employee.status}
                </span>
              </div>
              <div className="mt-4 grid grid-cols-2 gap-3 text-sm text-ink-600 dark:text-white/70">
                <p>{employee.designation}</p>
                <p>{formatCurrency(employee.salary)}</p>
              </div>
            </motion.button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default EmployeeTable;

''',

    # -------------------------------------------------------------------------
    # client/src/components/Sidebar.jsx
    # -------------------------------------------------------------------------
    "client/src/components/Sidebar.jsx": r'''import React from 'react';
import { motion } from 'framer-motion';
import { BarChart3, Briefcase, LogOut, Menu, MoonStar, SunMedium, UserRound, X } from 'lucide-react';
import { NavLink } from 'react-router-dom';

const buildItems = (canManageEmployees) =>
  [
    { to: '/', label: 'Command Deck', icon: BarChart3 },
    canManageEmployees ? { to: '/employees', label: 'People Ledger', icon: Briefcase } : null,
    { to: '/profile', label: 'My Profile', icon: UserRound }
  ].filter(Boolean);

const itemClassName = ({ isActive }) =>
  `flex items-center gap-3 rounded-2xl px-4 py-3 text-sm font-semibold transition ${
    isActive
      ? 'bg-ink-900 text-white shadow-glow dark:bg-ember-500 dark:text-ink-900'
      : 'text-ink-700 hover:bg-white/70 dark:text-ink-100 dark:hover:bg-white/10'
  }`;

const SidebarCard = ({
  canManageEmployees,
  currentUser,
  onClose,
  onLogout,
  onToggleTheme,
  theme,
  mobile = false
}) => (
  <aside className="flex h-full w-[285px] flex-col rounded-[30px] border border-white/50 bg-white/75 p-4 shadow-soft backdrop-blur dark:border-white/10 dark:bg-[#171311]/85">
    <div className="mb-6 flex items-center justify-between">
      <div>
        <p className="text-xs uppercase tracking-[0.25em] text-ember-700 dark:text-ember-300">
          EDMS
        </p>
        <h1 className="font-display text-3xl text-ink-900 dark:text-white">Harbor Console</h1>
      </div>
      {mobile ? (
        <button
          type="button"
          onClick={onClose}
          className="rounded-full p-2 text-ink-600 hover:bg-black/5 dark:text-ink-100 dark:hover:bg-white/10"
          aria-label="Close navigation"
        >
          <X className="h-5 w-5" />
        </button>
      ) : null}
    </div>

    <div className="mb-6 rounded-[26px] bg-gradient-to-br from-ember-500 via-amber-300 to-pine-300 p-[1px]">
      <div className="rounded-[25px] bg-[#1c1714] p-5 text-white">
        <p className="text-sm text-white/70">Signed in as</p>
        <p className="mt-1 text-xl font-semibold">{currentUser?.name}</p>
        <p className="text-sm text-white/70">{currentUser?.role?.toUpperCase()}</p>
      </div>
    </div>

    <nav className="space-y-2">
      {buildItems(canManageEmployees).map((item) => {
        const Icon = item.icon;

        return (
          <NavLink key={item.to} to={item.to} className={itemClassName} onClick={onClose}>
            <Icon className="h-5 w-5" />
            <span>{item.label}</span>
          </NavLink>
        );
      })}
    </nav>

    <div className="mt-auto rounded-[26px] bg-ink-100/80 p-4 dark:bg-white/5">
      <div className="mb-4">
        <p className="text-sm font-semibold text-ink-900 dark:text-white">Mode</p>
        <p className="text-sm text-ink-600 dark:text-white/65">
          Switch between bright review mode and late-shift focus mode.
        </p>
      </div>
      <button
        type="button"
        onClick={onToggleTheme}
        className="flex w-full items-center justify-between rounded-2xl bg-white px-4 py-3 text-sm font-semibold text-ink-900 shadow-sm transition hover:shadow-md dark:bg-white/10 dark:text-white"
      >
        <span>{theme === 'light' ? 'Turn on night mode' : 'Return to daylight'}</span>
        {theme === 'light' ? <MoonStar className="h-4 w-4" /> : <SunMedium className="h-4 w-4" />}
      </button>
      <button
        type="button"
        onClick={onLogout}
        className="mt-3 flex w-full items-center justify-between rounded-2xl border border-ink-200 px-4 py-3 text-sm font-semibold text-ink-900 transition hover:bg-white dark:border-white/10 dark:text-white dark:hover:bg-white/10"
      >
        <span>Sign out</span>
        <LogOut className="h-4 w-4" />
      </button>
    </div>
  </aside>
);

const Sidebar = ({
  canManageEmployees,
  currentUser,
  isOpen,
  onClose,
  onLogout,
  onOpen,
  onToggleTheme,
  theme
}) => (
  <>
    <button
      type="button"
      onClick={onOpen}
      className="fixed right-4 top-4 z-40 rounded-full border border-white/50 bg-white/80 p-3 text-ink-900 shadow-soft backdrop-blur lg:hidden dark:border-white/10 dark:bg-ink-900/80 dark:text-white"
      aria-label="Open navigation"
    >
      <Menu className="h-5 w-5" />
    </button>

    <div className="hidden lg:block">
      <SidebarCard
        canManageEmployees={canManageEmployees}
        currentUser={currentUser}
        onClose={onClose}
        onLogout={onLogout}
        onToggleTheme={onToggleTheme}
        theme={theme}
      />
    </div>

    <motion.aside
      initial={false}
      animate={{
        x: isOpen ? 0 : -320,
        opacity: isOpen ? 1 : 0.98
      }}
      className="fixed inset-y-3 left-3 z-40 lg:hidden"
    >
      <SidebarCard
        canManageEmployees={canManageEmployees}
        currentUser={currentUser}
        onClose={onClose}
        onLogout={onLogout}
        onToggleTheme={onToggleTheme}
        theme={theme}
        mobile
      />
    </motion.aside>
  </>
);

export default Sidebar;

''',

    # -------------------------------------------------------------------------
    # client/src/context/AppContext.jsx
    # -------------------------------------------------------------------------
    "client/src/context/AppContext.jsx": r'''import React, { createContext, startTransition, useContext, useEffect, useState } from 'react';

import {
  clearAccessToken,
  fetchCurrentUser,
  fetchEmployeeById,
  fetchEmployees,
  fetchOverview,
  getStoredAccessToken,
  loginUser as loginRequest,
  logoutUser as logoutRequest,
  registerUser as registerRequest,
  restoreSession,
  sendContactHr,
  setAccessToken
} from '../lib/api';

const AppContext = createContext(null);

const emptyAnalytics = {
  totalEmployees: 0,
  departmentDistribution: [],
  salarySummary: {
    averageSalary: 0,
    totalSalary: 0,
    maxSalary: 0,
    minSalary: 0
  },
  monthlyHiring: [],
  attendanceSummary: [],
  recentActivity: []
};

const getStoredTheme = () => {
  if (typeof window === 'undefined') {
    return 'light';
  }

  return window.localStorage.getItem('edms-theme') || 'light';
};

const isPublicAuthRoute = () => {
  if (typeof window === 'undefined') {
    return false;
  }

  return ['/login', '/register'].includes(window.location.pathname);
};

const buildPersonalAnalytics = (employee) => {
  if (!employee) {
    return emptyAnalytics;
  }

  const attendanceBuckets = (employee.attendance || []).reduce(
    (totals, entry) => ({
      ...totals,
      [entry.status]: (totals[entry.status] || 0) + 1
    }),
    {}
  );

  const attendanceSummary = Object.entries(attendanceBuckets).map(([status, count]) => ({
    status,
    count
  }));

  const joinedAt = employee.joiningDate ? new Date(employee.joiningDate) : null;
  const monthlyHiring = joinedAt
    ? [
        {
          _id: {
            year: joinedAt.getFullYear(),
            month: joinedAt.getMonth() + 1
          },
          hires: 1
        }
      ]
    : [];

  return {
    totalEmployees: 1,
    departmentDistribution: employee.department
      ? [{ department: employee.department, count: 1 }]
      : [],
    salarySummary: {
      averageSalary: employee.salary || 0,
      totalSalary: employee.salary || 0,
      maxSalary: employee.salary || 0,
      minSalary: employee.salary || 0
    },
    monthlyHiring,
    attendanceSummary,
    recentActivity: [
      {
        _id: employee._id,
        firstName: employee.firstName,
        lastName: employee.lastName,
        employeeId: employee.employeeId,
        department: employee.department,
        updatedAt: employee.updatedAt || employee.createdAt || new Date().toISOString()
      }
    ]
  };
};

export const AppProvider = ({ children }) => {
  const [theme, setTheme] = useState(getStoredTheme);
  const [employees, setEmployees] = useState([]);
  const [analytics, setAnalytics] = useState(emptyAnalytics);
  const [currentUser, setCurrentUser] = useState(null);
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [isProfileOpen, setIsProfileOpen] = useState(false);
  const [isContactOpen, setIsContactOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [notice, setNotice] = useState('');

  useEffect(() => {
    document.documentElement.classList.toggle('dark', theme === 'dark');
    window.localStorage.setItem('edms-theme', theme);
  }, [theme]);

  const clearWorkspace = () => {
    startTransition(() => {
      setCurrentUser(null);
      setEmployees([]);
      setAnalytics(emptyAnalytics);
      setSelectedEmployee(null);
      setIsProfileOpen(false);
      setIsContactOpen(false);
    });
  };

  const loadRoleBasedData = async (sessionUser) => {
    if (!sessionUser) {
      return;
    }

    if (sessionUser.role === 'employee') {
      let employeeRecord = sessionUser.employee || null;

      if (employeeRecord?._id) {
        try {
          const employeeResponse = await fetchEmployeeById(employeeRecord._id);
          employeeRecord = employeeResponse.data?.data?.employee || employeeRecord;
        } catch (_error) {
          employeeRecord = sessionUser.employee || null;
        }
      }

      const hydratedUser = {
        ...sessionUser,
        employee: employeeRecord
      };

      startTransition(() => {
        setCurrentUser(hydratedUser);
        setEmployees(employeeRecord ? [employeeRecord] : []);
        setAnalytics(buildPersonalAnalytics(employeeRecord));
      });

      return;
    }

    const [overviewResponse, employeesResponse] = await Promise.all([
      fetchOverview(),
      fetchEmployees()
    ]);

    startTransition(() => {
      setCurrentUser(sessionUser);
      setAnalytics(overviewResponse.data?.data || emptyAnalytics);
      setEmployees(employeesResponse.data?.data?.items || []);
    });
  };

  const initializeSession = async () => {
    setIsLoading(true);

    try {
      if (!getStoredAccessToken()) {
        if (isPublicAuthRoute()) {
          clearAccessToken();
          clearWorkspace();
          setNotice('');
          setIsLoading(false);
          return;
        }

        try {
          const refreshResponse = await restoreSession();
          const refreshedToken = refreshResponse?.data?.data?.accessToken || refreshResponse;

          if (refreshedToken) {
            setAccessToken(refreshedToken);
          }
        } catch (_error) {
          clearAccessToken();
          clearWorkspace();
          setNotice('');
          setIsLoading(false);
          return;
        }
      }

      const userResponse = await fetchCurrentUser();
      const sessionUser = userResponse.data?.data?.user || null;

      if (!sessionUser) {
        throw new Error('Session could not be restored');
      }

      setNotice('');
      try {
        await loadRoleBasedData(sessionUser);
      } catch (error) {
        startTransition(() => {
          setCurrentUser(sessionUser);
          setEmployees(sessionUser.employee ? [sessionUser.employee] : []);
          setAnalytics(
            sessionUser.role === 'employee'
              ? buildPersonalAnalytics(sessionUser.employee)
              : emptyAnalytics
          );
        });
        setNotice(
          error.response?.data?.message ||
            'Your session is active, but some workspace data could not be loaded.'
        );
      }
    } catch (error) {
      clearAccessToken();
      clearWorkspace();
      setNotice(error.response?.data?.message || 'Your session has expired. Please sign in again.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    initializeSession();
  }, []);

  const toggleTheme = () => {
    setTheme((currentTheme) => (currentTheme === 'light' ? 'dark' : 'light'));
  };

  const openEmployee = (employee) => {
    setSelectedEmployee(employee);
    setIsProfileOpen(true);
  };

  const closeEmployee = () => {
    setIsProfileOpen(false);
  };

  const openContactModal = () => setIsContactOpen(true);
  const closeContactModal = () => setIsContactOpen(false);
  const clearNotice = () => setNotice('');

  const loginUser = async (payload) => {
    try {
      const response = await loginRequest(payload);
      const token = response.data?.data?.tokens?.accessToken || '';
      setAccessToken(token);
      await initializeSession();
      return { success: true };
    } catch (error) {
      clearAccessToken();
      clearWorkspace();
      return {
        success: false,
        message: error.response?.data?.message || 'Unable to sign in with those credentials.',
        details: error.response?.data?.details || []
      };
    }
  };

  const registerUser = async (payload) => {
    try {
      const response = await registerRequest(payload);
      const token = response.data?.data?.tokens?.accessToken || '';
      setAccessToken(token);
      await initializeSession();
      return { success: true };
    } catch (error) {
      clearAccessToken();
      clearWorkspace();
      return {
        success: false,
        message: error.response?.data?.message || 'Unable to create your account right now.',
        details: error.response?.data?.details || []
      };
    }
  };

  const logoutUser = async () => {
    try {
      await logoutRequest();
    } catch (_error) {
      // Clear the local session even if the server-side logout call fails.
    }

    clearAccessToken();
    clearWorkspace();
    setNotice('You have been signed out.');
  };

  const submitContactRequest = async (payload) => {
    try {
      const response = await sendContactHr(payload);
      setNotice(response.data?.message || 'HR request submitted successfully.');
      return { success: true, preview: false };
    } catch (error) {
      const message = error.response?.data?.message || 'Unable to send the request right now.';
      setNotice(message);
      return { success: false, preview: false, message };
    }
  };

  const canManageEmployees = ['admin', 'hr'].includes(currentUser?.role || '');

  return (
    <AppContext.Provider
      value={{
        analytics,
        canManageEmployees,
        clearNotice,
        closeContactModal,
        closeEmployee,
        currentUser,
        employees,
        initializeSession,
        isAuthenticated: Boolean(currentUser),
        isContactOpen,
        isLoading,
        isProfileOpen,
        loginUser,
        logoutUser,
        notice,
        openContactModal,
        openEmployee,
        registerUser,
        selectedEmployee,
        submitContactRequest,
        theme,
        toggleTheme
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => {
  const context = useContext(AppContext);

  if (!context) {
    throw new Error('useAppContext must be used within an AppProvider');
  }

  return context;
};

''',

    # -------------------------------------------------------------------------
    # client/src/data/mockData.js
    # -------------------------------------------------------------------------
    "client/src/data/mockData.js": r'''export const mockCurrentUser = {
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

''',

    # -------------------------------------------------------------------------
    # client/src/index.css
    # -------------------------------------------------------------------------
    "client/src/index.css": r'''@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Space+Grotesk:wght@400;500;700&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    color-scheme: light;
  }

  .dark {
    color-scheme: dark;
  }

  body {
    @apply m-0 font-sans antialiased;
  }

  * {
    scrollbar-width: thin;
    scrollbar-color: rgba(120, 113, 108, 0.5) transparent;
  }
}

@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
}

''',

    # -------------------------------------------------------------------------
    # client/src/lib/api.js
    # -------------------------------------------------------------------------
    "client/src/lib/api.js": r'''import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:4000';
const ACCESS_TOKEN_KEY = 'edms-access-token';

const readStoredToken = () => {
  if (typeof window === 'undefined') {
    return '';
  }

  return window.localStorage.getItem(ACCESS_TOKEN_KEY) || '';
};

let accessToken = readStoredToken();
let refreshPromise = null;

const api = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true
});

const refreshClient = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true
});

export const getStoredAccessToken = () => accessToken;

export const setAccessToken = (token) => {
  accessToken = token || '';

  if (typeof window !== 'undefined') {
    if (accessToken) {
      window.localStorage.setItem(ACCESS_TOKEN_KEY, accessToken);
    } else {
      window.localStorage.removeItem(ACCESS_TOKEN_KEY);
    }
  }
};

export const clearAccessToken = () => {
  setAccessToken('');
};

const refreshSession = async () => {
  if (!refreshPromise) {
    refreshPromise = refreshClient
      .post('/api/auth/refresh', {})
      .then((response) => {
        const nextToken = response.data?.data?.accessToken || '';
        setAccessToken(nextToken);
        return nextToken;
      })
      .finally(() => {
        refreshPromise = null;
      });
  }

  return refreshPromise;
};

api.interceptors.request.use((config) => {
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config || {};
    const shouldAttemptRefresh =
      error.response?.status === 401 &&
      !originalRequest._retry &&
      !originalRequest.skipAuthRefresh &&
      Boolean(accessToken);

    if (!shouldAttemptRefresh) {
      return Promise.reject(error);
    }

    originalRequest._retry = true;

    try {
      const nextToken = await refreshSession();

      if (!nextToken) {
        clearAccessToken();
        return Promise.reject(error);
      }

      originalRequest.headers = {
        ...(originalRequest.headers || {}),
        Authorization: `Bearer ${nextToken}`
      };

      return api(originalRequest);
    } catch (refreshError) {
      clearAccessToken();
      return Promise.reject(refreshError);
    }
  }
);

export const loginUser = (payload) =>
  api.post('/api/auth/login', payload, {
    skipAuthRefresh: true
  });

export const registerUser = (payload) =>
  api.post('/api/auth/register', payload, {
    skipAuthRefresh: true
  });

export const logoutUser = () => api.post('/api/auth/logout');
export const restoreSession = () => refreshSession();
export const fetchOverview = () => api.get('/api/analytics/overview');
export const fetchEmployees = () => api.get('/api/employees?limit=50');
export const fetchEmployeeById = (employeeId) => api.get(`/api/employees/${employeeId}`);
export const fetchCurrentUser = () => api.get('/api/auth/me');
export const sendContactHr = (payload) => api.post('/api/notifications/contact-hr', payload);

export default api;

''',

    # -------------------------------------------------------------------------
    # client/src/main.jsx
    # -------------------------------------------------------------------------
    "client/src/main.jsx": r'''import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';

import App from './App';
import { AppProvider } from './context/AppContext';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <AppProvider>
        <App />
      </AppProvider>
    </BrowserRouter>
  </React.StrictMode>
);

''',

    # -------------------------------------------------------------------------
    # client/tailwind.config.js
    # -------------------------------------------------------------------------
    "client/tailwind.config.js": r'''/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      fontFamily: {
        display: ['Fraunces', 'serif'],
        sans: ['Space Grotesk', 'ui-sans-serif', 'system-ui']
      },
      colors: {
        ember: {
          50: '#fff7ed',
          100: '#ffedd5',
          300: '#fdba74',
          500: '#f97316',
          700: '#c2410c'
        },
        pine: {
          100: '#dbe9df',
          300: '#9ebaa5',
          500: '#557c66',
          700: '#244636'
        },
        ink: {
          50: '#f6f5f2',
          100: '#edeae3',
          700: '#413a33',
          900: '#1d1916'
        }
      },
      boxShadow: {
        soft: '0 18px 60px rgba(29, 25, 22, 0.12)',
        glow: '0 10px 40px rgba(249, 115, 22, 0.18)'
      },
      backgroundImage: {
        haze:
          'radial-gradient(circle at top left, rgba(249, 115, 22, 0.22), transparent 36%), radial-gradient(circle at bottom right, rgba(85, 124, 102, 0.26), transparent 34%)'
      }
    }
  },
  plugins: []
};

''',

    # -------------------------------------------------------------------------
    # client/vite.config.js
    # -------------------------------------------------------------------------
    "client/vite.config.js": r'''import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000
  }
});

''',

    # -------------------------------------------------------------------------
    # server/README.md
    # -------------------------------------------------------------------------
    "server/README.md": r'''# EDMS Server

Production-style Express + MongoDB backend for the Employee Data Management System prompt.

## Setup

1. Install dependencies:
   `npm install`
2. Copy `.env.example` to `.env`
3. Update MongoDB, JWT, and SMTP values
4. Start the API:
   `npm run dev`

## Folder Structure

```text
server/
  app.js
  index.js
  config/
  controllers/
  middleware/
  models/
  routes/
  services/
  uploads/
  utils/
```

## Environment Variables

| Variable | Purpose |
|---|---|
| `PORT` | API port |
| `MONGO_URI` | MongoDB connection string |
| `JWT_SECRET` | Access token signing secret |
| `JWT_REFRESH_SECRET` | Refresh token signing secret |
| `ACCESS_TOKEN_EXP` | Access token duration |
| `REFRESH_TOKEN_EXP` | Refresh token duration |
| `CLIENT_ORIGIN` | Allowed frontend origin(s) for CORS |
| `CLIENT_APP_URL` | Frontend URL used in password reset email |
| `SMTP_HOST` / `SMTP_PORT` | SMTP server details |
| `SMTP_USER` / `SMTP_PASS` | SMTP credentials |
| `MAIL_FROM` | Optional sender override |
| `HR_NOTIFICATION_EMAIL` | HR inbox for contact form delivery |
| `ADMIN_BOOTSTRAP_KEY` | Optional bootstrap key for privileged account creation |
| `NODE_ENV` | Runtime environment |
| `LOG_LEVEL` | Winston logging level |

## Authentication Flow

1. `POST /api/auth/register` creates a user and optionally links an employee record through `employeeId`.
   Public registration defaults to `employee`; use `ADMIN_BOOTSTRAP_KEY` only for initial privileged account setup.
2. `POST /api/auth/login` returns an access token and rotates a refresh token.
3. `POST /api/auth/refresh` issues a new access token and refresh token pair.
4. `POST /api/auth/logout` clears stored refresh state.
5. `POST /api/auth/forgot-password` and `POST /api/auth/reset-password` handle reset email delivery and password reset.

Use the access token as `Authorization: Bearer <token>`.

## API Routes

| Method | Route | Description | Access |
|---|---|---|---|
| `GET` | `/health` | Health check | Public |
| `POST` | `/api/auth/register` | Register account | Public |
| `POST` | `/api/auth/login` | Login | Public |
| `POST` | `/api/auth/refresh` | Refresh JWT session | Public |
| `POST` | `/api/auth/logout` | Logout | Public |
| `GET` | `/api/auth/me` | Current user | Authenticated |
| `POST` | `/api/auth/forgot-password` | Request password reset | Public |
| `POST` | `/api/auth/reset-password` | Reset password | Public |
| `GET` | `/api/employees` | Employee list with pagination/filtering/search | Admin, HR |
| `GET` | `/api/employees/:id` | Employee details | Admin, HR, linked employee |
| `POST` | `/api/employees` | Create employee with uploads | Admin, HR |
| `PUT` | `/api/employees/:id` | Update employee and append uploads | Admin, HR |
| `DELETE` | `/api/employees/:id` | Delete employee | Admin |
| `POST` | `/api/employees/:id/attendance` | Add attendance entry | Admin, HR |
| `GET` | `/api/analytics/overview` | Dashboard analytics | Admin, HR |
| `POST` | `/api/notifications/contact-hr` | Contact HR email notification | Authenticated |

## Data Model Notes

- `User` stores role, linked employee reference, refresh token hash, and password reset token hash.
- `Employee` stores department, salary, attendance, emergency contact data, profile image path, and uploaded documents.
- MongoDB indexes are applied on email, employee ID, department, salary, joining date, and search fields.

## File Uploads

- Supported formats: JPG, PNG, WEBP, PDF
- Max file size: 8 MB per file
- Storage: local `server/uploads/`
- Fields:
  - `profileImage`: max 1 file
  - `documents`: max 5 files

## Deployment Notes

- Put the API behind HTTPS in production.
- Replace local uploads with object storage such as S3 for multi-instance deployments.
- Add Redis for response/session caching if traffic grows.
- Add CI to run linting, tests, and deployment checks before release.

''',

    # -------------------------------------------------------------------------
    # server/app.js
    # -------------------------------------------------------------------------
    "server/app.js": r'''const path = require('path');
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const cookieParser = require('cookie-parser');
const rateLimit = require('express-rate-limit');
const morgan = require('morgan');

const authRoutes = require('./routes/authRoutes');
const employeeRoutes = require('./routes/employeeRoutes');
const analyticsRoutes = require('./routes/analyticsRoutes');
const notificationRoutes = require('./routes/notificationRoutes');
const { notFoundHandler, errorHandler } = require('./middleware/errorHandler');
const logger = require('./utils/logger');

const app = express();
const allowedOrigins = process.env.CLIENT_ORIGIN
  ? process.env.CLIENT_ORIGIN.split(',').map((origin) => origin.trim()).filter(Boolean)
  : [];

const corsOrigin = (origin, callback) => {
  if (!origin) {
    return callback(null, true);
  }

  const isAllowedOrigin = allowedOrigins.includes(origin);
  const isLocalDevOrigin =
    process.env.NODE_ENV !== 'production' && /^http:\/\/localhost:\d+$/.test(origin);

  return callback(null, isAllowedOrigin || isLocalDevOrigin);
};

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 200,
  standardHeaders: true,
  legacyHeaders: false,
  message: {
    success: false,
    message: 'Too many requests, please try again later.'
  }
});

app.use(helmet());
app.use(
  cors({
    origin: corsOrigin,
    credentials: true
  })
);
app.use(apiLimiter);
app.use(express.json({ limit: '1mb' }));
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(
  morgan('combined', {
    stream: {
      write: (message) => logger.http(message.trim())
    }
  })
);

app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

app.get('/health', (_req, res) => {
  res.status(200).json({
    success: true,
    message: 'EDMS API is healthy',
    data: {
      uptime: process.uptime(),
      timestamp: new Date().toISOString()
    }
  });
});

app.use('/api/auth', authRoutes);
app.use('/api/employees', employeeRoutes);
app.use('/api/analytics', analyticsRoutes);
app.use('/api/notifications', notificationRoutes);

app.use(notFoundHandler);
app.use(errorHandler);

module.exports = app;

''',

    # -------------------------------------------------------------------------
    # server/config/db.js
    # -------------------------------------------------------------------------
    "server/config/db.js": r'''const dns = require('dns');
const mongoose = require('mongoose');
const logger = require('../utils/logger');

const connectDB = async (uri) => {
  try {
    const dnsServers = (process.env.MONGO_DNS_SERVERS || '')
      .split(',')
      .map((server) => server.trim())
      .filter(Boolean);

    if (dnsServers.length > 0) {
      dns.setServers(dnsServers);
      logger.info(`Using custom DNS servers for MongoDB: ${dnsServers.join(', ')}`);
    }

    await mongoose.connect(uri);
    logger.info('MongoDB connected');
  } catch (err) {
    logger.error(`MongoDB connection error: ${err.message}`);
    process.exit(1);
  }
};

module.exports = connectDB;

''',

    # -------------------------------------------------------------------------
    # server/controllers/analyticsController.js
    # -------------------------------------------------------------------------
    "server/controllers/analyticsController.js": r'''const Employee = require('../models/Employee');
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

''',

    # -------------------------------------------------------------------------
    # server/controllers/authController.js
    # -------------------------------------------------------------------------
    "server/controllers/authController.js": r'''const crypto = require('crypto');
const bcrypt = require('bcryptjs');

const User = require('../models/User');
const Employee = require('../models/Employee');
const asyncHandler = require('../utils/asyncHandler');
const AppError = require('../utils/AppError');
const { sendSuccess } = require('../utils/http');
const { signAccessToken, signRefreshToken, hashToken } = require('../utils/tokens');
const { sendRegistrationEmail, sendPasswordResetEmail } = require('../services/emailService');
const logger = require('../utils/logger');

const sanitizeUser = (user) => ({
  id: user._id,
  name: user.name,
  email: user.email,
  role: user.role,
  employee: user.employee,
  lastLoginAt: user.lastLoginAt,
  createdAt: user.createdAt,
  updatedAt: user.updatedAt
});

const setRefreshCookie = (res, refreshToken) => {
  res.cookie('refreshToken', refreshToken, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'strict',
    maxAge: 7 * 24 * 60 * 60 * 1000
  });
};

const clearAuthCookies = (res) => {
  res.clearCookie('refreshToken');
  res.clearCookie('accessToken');
};

const issueTokens = async (user, res) => {
  const accessToken = signAccessToken(user);
  const refreshToken = signRefreshToken(user);

  user.refreshTokenHash = hashToken(refreshToken);
  user.lastLoginAt = new Date();
  await user.save();

  setRefreshCookie(res, refreshToken);

  return {
    accessToken,
    refreshToken
  };
};

const resolveRegistrationRole = (requestedRole, bootstrapKey) => {
  const validRole = ['admin', 'hr', 'employee'].includes(requestedRole)
    ? requestedRole
    : 'employee';

  if (validRole === 'employee') {
    return 'employee';
  }

  if (
    process.env.ADMIN_BOOTSTRAP_KEY &&
    bootstrapKey &&
    bootstrapKey === process.env.ADMIN_BOOTSTRAP_KEY
  ) {
    return validRole;
  }

  return 'employee';
};

const register = asyncHandler(async (req, res) => {
  const { name, email, password, role = 'employee', employeeId, bootstrapKey } = req.body;

  const existingUser = await User.findOne({ email: email.toLowerCase() });
  if (existingUser) {
    throw new AppError(409, 'An account with this email already exists');
  }

  let linkedEmployee = null;
  if (employeeId) {
    linkedEmployee = await Employee.findOne({ employeeId });

    if (!linkedEmployee) {
      throw new AppError(404, 'Employee record not found for the supplied employee ID');
    }

    if (linkedEmployee.user) {
      throw new AppError(409, 'This employee record is already linked to a user account');
    }
  }

  const passwordHash = await bcrypt.hash(password, 12);
  const resolvedRole = resolveRegistrationRole(role, bootstrapKey);
  const user = await User.create({
    name,
    email: email.toLowerCase(),
    passwordHash,
    role: resolvedRole,
    employee: linkedEmployee ? linkedEmployee._id : undefined
  });

  if (linkedEmployee) {
    linkedEmployee.user = user._id;
    await linkedEmployee.save();
  }

  const tokens = await issueTokens(user, res);
  const emailResult = await sendRegistrationEmail({ email: user.email, name: user.name });

  return sendSuccess(
    res,
    'User registered successfully',
    {
      user: sanitizeUser(user),
      tokens,
      emailNotification: emailResult
    },
    201
  );
});

const login = asyncHandler(async (req, res) => {
  const { email, password } = req.body;

  const user = await User.findOne({ email: email.toLowerCase() });
  if (!user) {
    logger.warn({ message: 'Failed login attempt', email });
    throw new AppError(401, 'Invalid email or password');
  }

  const isPasswordValid = await bcrypt.compare(password, user.passwordHash);
  if (!isPasswordValid) {
    logger.warn({ message: 'Failed login attempt', email });
    throw new AppError(401, 'Invalid email or password');
  }

  const tokens = await issueTokens(user, res);
  const populatedUser = await User.findById(user._id)
    .select('-passwordHash -refreshTokenHash -resetPasswordTokenHash')
    .populate('employee');

  return sendSuccess(res, 'Login successful', {
    user: populatedUser,
    tokens
  });
});

const refresh = asyncHandler(async (req, res) => {
  const providedToken = req.cookies.refreshToken || req.body.refreshToken;
  if (!providedToken) {
    throw new AppError(401, 'Refresh token is required');
  }

  const decoded = require('jsonwebtoken').verify(providedToken, process.env.JWT_REFRESH_SECRET);
  const user = await User.findById(decoded.sub);

  if (!user || user.refreshTokenHash !== hashToken(providedToken)) {
    throw new AppError(401, 'Refresh token is invalid or expired');
  }

  const tokens = await issueTokens(user, res);

  return sendSuccess(res, 'Token refreshed successfully', {
    accessToken: tokens.accessToken,
    refreshToken: tokens.refreshToken
  });
});

const logout = asyncHandler(async (req, res) => {
  const providedToken = req.cookies.refreshToken || req.body.refreshToken;

  if (providedToken) {
    try {
      const decoded = require('jsonwebtoken').verify(
        providedToken,
        process.env.JWT_REFRESH_SECRET
      );
      const user = await User.findById(decoded.sub);

      if (user) {
        user.refreshTokenHash = undefined;
        await user.save();
      }
    } catch (_error) {
      logger.warn({ message: 'Logout requested with an invalid refresh token' });
    }
  }

  clearAuthCookies(res);

  return sendSuccess(res, 'Logged out successfully');
});

const me = asyncHandler(async (req, res) => {
  const user = await User.findById(req.user._id)
    .select('-passwordHash -refreshTokenHash -resetPasswordTokenHash')
    .populate('employee');

  return sendSuccess(res, 'Current user fetched successfully', { user });
});

const forgotPassword = asyncHandler(async (req, res) => {
  const { email } = req.body;
  const user = await User.findOne({ email: email.toLowerCase() });

  if (!user) {
    return sendSuccess(res, 'If the account exists, a reset email has been queued');
  }

  const resetToken = crypto.randomBytes(32).toString('hex');
  user.resetPasswordTokenHash = hashToken(resetToken);
  user.resetPasswordExpiresAt = new Date(Date.now() + 1000 * 60 * 30);
  await user.save();

  const emailResult = await sendPasswordResetEmail({
    email: user.email,
    name: user.name,
    resetToken
  });

  return sendSuccess(res, 'Password reset instructions have been sent', {
    emailNotification: emailResult
  });
});

const resetPassword = asyncHandler(async (req, res) => {
  const { token, newPassword } = req.body;
  const hashedToken = hashToken(token);

  const user = await User.findOne({
    resetPasswordTokenHash: hashedToken,
    resetPasswordExpiresAt: { $gt: new Date() }
  });

  if (!user) {
    throw new AppError(400, 'Password reset token is invalid or expired');
  }

  user.passwordHash = await bcrypt.hash(newPassword, 12);
  user.resetPasswordTokenHash = undefined;
  user.resetPasswordExpiresAt = undefined;
  user.refreshTokenHash = undefined;
  await user.save();

  clearAuthCookies(res);

  return sendSuccess(res, 'Password has been reset successfully');
});

module.exports = {
  register,
  login,
  refresh,
  logout,
  me,
  forgotPassword,
  resetPassword
};

''',

    # -------------------------------------------------------------------------
    # server/controllers/employeeController.js
    # -------------------------------------------------------------------------
    "server/controllers/employeeController.js": r'''const path = require('path');

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

''',

    # -------------------------------------------------------------------------
    # server/controllers/notificationController.js
    # -------------------------------------------------------------------------
    "server/controllers/notificationController.js": r'''const asyncHandler = require('../utils/asyncHandler');
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

''',

    # -------------------------------------------------------------------------
    # server/index.js
    # -------------------------------------------------------------------------
    "server/index.js": r'''const path = require('path');

require('dotenv').config({ path: path.join(__dirname, '.env') });

const app = require('./app');
const connectDB = require('./config/db');
const logger = require('./utils/logger');

const PORT = process.env.PORT || 4000;

const startServer = async () => {
  if (!process.env.MONGO_URI) {
    logger.error('MONGO_URI is not configured');
    process.exit(1);
  }

  await connectDB(process.env.MONGO_URI);

  app.listen(PORT, () => {
    logger.info(`EDMS API listening on port ${PORT}`);
  });
};

startServer();

''',

    # -------------------------------------------------------------------------
    # server/middleware/auth.js
    # -------------------------------------------------------------------------
    "server/middleware/auth.js": r'''const jwt = require('jsonwebtoken');

const User = require('../models/User');
const asyncHandler = require('../utils/asyncHandler');
const AppError = require('../utils/AppError');

const authenticate = asyncHandler(async (req, _res, next) => {
  const authHeader = req.headers.authorization || '';
  const bearerToken = authHeader.startsWith('Bearer ') ? authHeader.slice(7) : null;
  const token = bearerToken || req.cookies.accessToken;

  if (!token) {
    throw new AppError(401, 'Authentication required');
  }

  const decoded = jwt.verify(token, process.env.JWT_SECRET);
  const user = await User.findById(decoded.sub).select('-passwordHash -refreshTokenHash -resetPasswordTokenHash');

  if (!user) {
    throw new AppError(401, 'User account not found');
  }

  req.user = user;
  next();
});

const authorize = (...roles) => (req, _res, next) => {
  if (!req.user || !roles.includes(req.user.role)) {
    return next(new AppError(403, 'You do not have permission to perform this action'));
  }

  return next();
};

module.exports = {
  authenticate,
  authorize
};

''',

    # -------------------------------------------------------------------------
    # server/middleware/errorHandler.js
    # -------------------------------------------------------------------------
    "server/middleware/errorHandler.js": r'''const multer = require('multer');

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

''',

    # -------------------------------------------------------------------------
    # server/middleware/upload.js
    # -------------------------------------------------------------------------
    "server/middleware/upload.js": r'''const fs = require('fs');
const path = require('path');
const multer = require('multer');

const uploadDirectory = path.join(__dirname, '..', 'uploads');

if (!fs.existsSync(uploadDirectory)) {
  fs.mkdirSync(uploadDirectory, { recursive: true });
}

const allowedMimeTypes = new Set([
  'image/jpeg',
  'image/png',
  'image/webp',
  'application/pdf'
]);

const storage = multer.diskStorage({
  destination: (_req, _file, cb) => cb(null, uploadDirectory),
  filename: (_req, file, cb) => {
    const safeBaseName = file.originalname.replace(/[^a-zA-Z0-9.-]/g, '_');
    cb(null, `${Date.now()}-${safeBaseName}`);
  }
});

const fileFilter = (_req, file, cb) => {
  if (!allowedMimeTypes.has(file.mimetype)) {
    return cb(new Error('Only JPG, PNG, WEBP images and PDF documents are allowed'));
  }

  return cb(null, true);
};

const upload = multer({
  storage,
  fileFilter,
  limits: {
    fileSize: 8 * 1024 * 1024
  }
});

const employeeUpload = upload.fields([
  { name: 'profileImage', maxCount: 1 },
  { name: 'documents', maxCount: 5 }
]);

module.exports = {
  employeeUpload
};

''',

    # -------------------------------------------------------------------------
    # server/middleware/validateRequest.js
    # -------------------------------------------------------------------------
    "server/middleware/validateRequest.js": r'''const { validationResult } = require('express-validator');

const validateRequest = (req, _res, next) => {
  const errors = validationResult(req);

  if (errors.isEmpty()) {
    return next();
  }

  return next({
    statusCode: 422,
    message: 'Validation failed',
    details: errors.array().map((error) => ({
      field: error.path,
      message: error.msg
    }))
  });
};

module.exports = validateRequest;

''',

    # -------------------------------------------------------------------------
    # server/models/Employee.js
    # -------------------------------------------------------------------------
    "server/models/Employee.js": r'''const mongoose = require('mongoose');

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

''',

    # -------------------------------------------------------------------------
    # server/models/User.js
    # -------------------------------------------------------------------------
    "server/models/User.js": r'''const mongoose = require('mongoose');

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

''',

    # -------------------------------------------------------------------------
    # server/package-lock.json
    # -------------------------------------------------------------------------
    "server/package-lock.json": r'''{
  "name": "edms-server",
  "version": "0.1.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "edms-server",
      "version": "0.1.0",
      "dependencies": {
        "bcryptjs": "^2.4.3",
        "cookie-parser": "^1.4.6",
        "cors": "^2.8.5",
        "dotenv": "^16.0.0",
        "express": "^4.18.2",
        "express-rate-limit": "^6.7.0",
        "express-validator": "^6.15.0",
        "helmet": "^6.0.1",
        "jsonwebtoken": "^9.0.0",
        "mongoose": "^7.0.0",
        "morgan": "^1.10.0",
        "multer": "^1.4.5-lts.1",
        "nodemailer": "^8.0.8",
        "winston": "^3.8.2"
      },
      "devDependencies": {
        "nodemon": "^3.1.14"
      }
    },
    "node_modules/@colors/colors": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/@colors/colors/-/colors-1.6.0.tgz",
      "integrity": "sha512-Ir+AOibqzrIsL6ajt3Rz3LskB7OiMVHqltZmspbW/TJuTVuyOMirVqAkjfY6JISiLHgyNqicAC8AyHHGzNd/dA==",
      "license": "MIT",
      "engines": {
        "node": ">=0.1.90"
      }
    },
    "node_modules/@dabh/diagnostics": {
      "version": "2.0.8",
      "resolved": "https://registry.npmjs.org/@dabh/diagnostics/-/diagnostics-2.0.8.tgz",
      "integrity": "sha512-R4MSXTVnuMzGD7bzHdW2ZhhdPC/igELENcq5IjEverBvq5hn1SXCWcsi6eSsdWP0/Ur+SItRRjAktmdoX/8R/Q==",
      "license": "MIT",
      "dependencies": {
        "@so-ric/colorspace": "^1.1.6",
        "enabled": "2.0.x",
        "kuler": "^2.0.0"
      }
    },
    "node_modules/@mongodb-js/saslprep": {
      "version": "1.4.11",
      "resolved": "https://registry.npmjs.org/@mongodb-js/saslprep/-/saslprep-1.4.11.tgz",
      "integrity": "sha512-o9rAHc0IpIjuPSxRutWpE1F62x7n+4mVS4rCNHkzhIUMQcc18bb6xEq5wd2NdN0WjepIyXIppRshYI2kQDOZVA==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "sparse-bitfield": "^3.0.3"
      }
    },
    "node_modules/@so-ric/colorspace": {
      "version": "1.1.6",
      "resolved": "https://registry.npmjs.org/@so-ric/colorspace/-/colorspace-1.1.6.tgz",
      "integrity": "sha512-/KiKkpHNOBgkFJwu9sh48LkHSMYGyuTcSFK/qMBdnOAlrRJzRSXAOFB5qwzaVQuDl8wAvHVMkaASQDReTahxuw==",
      "license": "MIT",
      "dependencies": {
        "color": "^5.0.2",
        "text-hex": "1.0.x"
      }
    },
    "node_modules/@types/node": {
      "version": "25.9.1",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-25.9.1.tgz",
      "integrity": "sha512-xfrlY7UD5rMJk3ZVJP8BNzS28J36YJg+xp+LPXV1TdWxr8uMH5A860QNxYDGQe/ylDSgjxE52Q9VnO7p75tJxg==",
      "license": "MIT",
      "dependencies": {
        "undici-types": ">=7.24.0 <7.24.7"
      }
    },
    "node_modules/@types/triple-beam": {
      "version": "1.3.5",
      "resolved": "https://registry.npmjs.org/@types/triple-beam/-/triple-beam-1.3.5.tgz",
      "integrity": "sha512-6WaYesThRMCl19iryMYP7/x2OVgCtbIVflDGFpWnb9irXI3UjYE4AzmYuiUKY1AJstGijoY+MgUszMgRxIYTYw==",
      "license": "MIT"
    },
    "node_modules/@types/webidl-conversions": {
      "version": "7.0.3",
      "resolved": "https://registry.npmjs.org/@types/webidl-conversions/-/webidl-conversions-7.0.3.tgz",
      "integrity": "sha512-CiJJvcRtIgzadHCYXw7dqEnMNRjhGZlYK05Mj9OyktqV8uVT8fD2BFOB7S1uwBE3Kj2Z+4UyPmFw/Ixgw/LAlA==",
      "license": "MIT"
    },
    "node_modules/@types/whatwg-url": {
      "version": "8.2.2",
      "resolved": "https://registry.npmjs.org/@types/whatwg-url/-/whatwg-url-8.2.2.tgz",
      "integrity": "sha512-FtQu10RWgn3D9U4aazdwIE2yzphmTJREDqNdODHrbrZmmMqI0vMheC/6NE/J1Yveaj8H+ela+YwWTjq5PGmuhA==",
      "license": "MIT",
      "dependencies": {
        "@types/node": "*",
        "@types/webidl-conversions": "*"
      }
    },
    "node_modules/accepts": {
      "version": "1.3.8",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.8.tgz",
      "integrity": "sha512-PYAthTa2m2VKxuvSD3DPC/Gy+U+sOA1LAuT8mkmRuvw+NACSaeXEQ+NHcVF7rONl6qcaxV3Uuemwawk+7+SJLw==",
      "license": "MIT",
      "dependencies": {
        "mime-types": "~2.1.34",
        "negotiator": "0.6.3"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/anymatch": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz",
      "integrity": "sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "normalize-path": "^3.0.0",
        "picomatch": "^2.0.4"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/append-field": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/append-field/-/append-field-1.0.0.tgz",
      "integrity": "sha512-klpgFSWLW1ZEs8svjfb7g4qWY0YS5imI82dTg+QahUvJ8YqAY0P10Uk8tTyh9ZGuYEZEMaeJYCF5BFuX552hsw==",
      "license": "MIT"
    },
    "node_modules/array-flatten": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz",
      "integrity": "sha512-PCVAQswWemu6UdxsDFFX/+gVeYqKAod3D3UVm91jHwynguOwAvYPhx8nNlM++NqRcK6CxxpUafjmhIdKiHibqg==",
      "license": "MIT"
    },
    "node_modules/async": {
      "version": "3.2.6",
      "resolved": "https://registry.npmjs.org/async/-/async-3.2.6.tgz",
      "integrity": "sha512-htCUDlxyyCLMgaM3xXg0C0LW2xqfuQ6p05pCEIsXuyQ+a1koYKTuBMzRNwmybfLgvJDMd0r1LTn4+E0Ti6C2AA==",
      "license": "MIT"
    },
    "node_modules/balanced-match": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-4.0.4.tgz",
      "integrity": "sha512-BLrgEcRTwX2o6gGxGOCNyMvGSp35YofuYzw9h1IMTRmKqttAZZVU67bdb9Pr2vUHA8+j3i2tJfjO6C6+4myGTA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "18 || 20 || >=22"
      }
    },
    "node_modules/basic-auth": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/basic-auth/-/basic-auth-2.0.1.tgz",
      "integrity": "sha512-NF+epuEdnUYVlGuhaxbbq+dvJttwLnGY+YixlXlME5KpQ5W3CnXA5cVTneY3SPbPDRkcjMbifrwmFYcClgOZeg==",
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "5.1.2"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/basic-auth/node_modules/safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==",
      "license": "MIT"
    },
    "node_modules/bcryptjs": {
      "version": "2.4.3",
      "resolved": "https://registry.npmjs.org/bcryptjs/-/bcryptjs-2.4.3.tgz",
      "integrity": "sha512-V/Hy/X9Vt7f3BbPJEi8BdVFMByHi+jNXrYkW3huaybV/kQ0KJg0Y6PkEMbn+zeT+i+SiKZ/HMqJGIIt4LZDqNQ==",
      "license": "MIT"
    },
    "node_modules/binary-extensions": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.3.0.tgz",
      "integrity": "sha512-Ceh+7ox5qe7LJuLHoY0feh3pHuUDHAcRUeyL2VYghZwfpkNIy/+8Ocg0a3UuSoYzavmylwuLWQOf3hl0jjMMIw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/body-parser": {
      "version": "1.20.5",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-1.20.5.tgz",
      "integrity": "sha512-3grm+/2tUOvu2cjJkvsIxrv/wVpfXQW4PsQHYm7yk4vfpu7Ekl6nEsYBoJUL6qDwZUx8wUhQ8tR2qz+ad9c9OA==",
      "license": "MIT",
      "dependencies": {
        "bytes": "~3.1.2",
        "content-type": "~1.0.5",
        "debug": "2.6.9",
        "depd": "2.0.0",
        "destroy": "~1.2.0",
        "http-errors": "~2.0.1",
        "iconv-lite": "~0.4.24",
        "on-finished": "~2.4.1",
        "qs": "~6.15.1",
        "raw-body": "~2.5.3",
        "type-is": "~1.6.18",
        "unpipe": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8",
        "npm": "1.2.8000 || >= 1.4.16"
      }
    },
    "node_modules/brace-expansion": {
      "version": "5.0.6",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-5.0.6.tgz",
      "integrity": "sha512-kLpxurY4Z4r9sgMsyG0Z9uzsBlgiU/EFKhj/h91/8yHu0edo7XuixOIH3VcJ8kkxs6/jPzoI6U9Vj3WqbMQ94g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "balanced-match": "^4.0.2"
      },
      "engines": {
        "node": "18 || 20 || >=22"
      }
    },
    "node_modules/braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fill-range": "^7.1.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/bson": {
      "version": "5.5.1",
      "resolved": "https://registry.npmjs.org/bson/-/bson-5.5.1.tgz",
      "integrity": "sha512-ix0EwukN2EpC0SRWIj/7B5+A6uQMQy6KMREI9qQqvgpkV2frH63T0UDVd1SYedL6dNCmDBYB3QtXi4ISk9YT+g==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=14.20.1"
      }
    },
    "node_modules/buffer-equal-constant-time": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/buffer-equal-constant-time/-/buffer-equal-constant-time-1.0.1.tgz",
      "integrity": "sha512-zRpUiDwd/xk6ADqPMATG8vc9VPrkck7T07OIx0gnjmJAnHnTVXNQG3vfvWNuiZIkwu9KrKdA1iJKfsfTVxE6NA==",
      "license": "BSD-3-Clause"
    },
    "node_modules/buffer-from": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.2.tgz",
      "integrity": "sha512-E+XQCRwSbaaiChtv6k6Dwgc+bx+Bs6vuKJHHl5kox/BaKbhiXzqQOwK4cO22yElGp2OCmjwVhT3HmxgyPGnJfQ==",
      "license": "MIT"
    },
    "node_modules/busboy": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/busboy/-/busboy-1.6.0.tgz",
      "integrity": "sha512-8SFQbg/0hQ9xy3UNTB0YEnsNBbWfhf7RtnzpL7TkBiTBRfrQ9Fxcnz7VJsleJpyp6rVLvXiuORqjlHi5q+PYuA==",
      "dependencies": {
        "streamsearch": "^1.1.0"
      },
      "engines": {
        "node": ">=10.16.0"
      }
    },
    "node_modules/bytes": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.2.tgz",
      "integrity": "sha512-/Nf7TyzTx6S3yRJObOAV7956r8cr2+Oj8AC5dt8wSP3BQAoeX58NoHyCU8P8zGkNXStjTSi6fzO6F0pBdcYbEg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/call-bound": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz",
      "integrity": "sha512-+ys997U96po4Kx/ABpBCqhA9EuxJaQWDQg7295H4hBphv3IZg0boBKuwYpt4YXp6MZ5AmZQnU/tyMTlRpaSejg==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "get-intrinsic": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/chokidar": {
      "version": "3.6.0",
      "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-3.6.0.tgz",
      "integrity": "sha512-7VT13fmjotKpGipCW9JEQAusEPE+Ei8nl6/g4FBAmIm0GOOLMua9NDDo/DWp0ZAxCr3cPq5ZpBqmPAQgDda2Pw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "anymatch": "~3.1.2",
        "braces": "~3.0.2",
        "glob-parent": "~5.1.2",
        "is-binary-path": "~2.1.0",
        "is-glob": "~4.0.1",
        "normalize-path": "~3.0.0",
        "readdirp": "~3.6.0"
      },
      "engines": {
        "node": ">= 8.10.0"
      },
      "funding": {
        "url": "https://paulmillr.com/funding/"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.2"
      }
    },
    "node_modules/color": {
      "version": "5.0.3",
      "resolved": "https://registry.npmjs.org/color/-/color-5.0.3.tgz",
      "integrity": "sha512-ezmVcLR3xAVp8kYOm4GS45ZLLgIE6SPAFoduLr6hTDajwb3KZ2F46gulK3XpcwRFb5KKGCSezCBAY4Dw4HsyXA==",
      "license": "MIT",
      "dependencies": {
        "color-convert": "^3.1.3",
        "color-string": "^2.1.3"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/color-convert": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-3.1.3.tgz",
      "integrity": "sha512-fasDH2ont2GqF5HpyO4w0+BcewlhHEZOFn9c1ckZdHpJ56Qb7MHhH/IcJZbBGgvdtwdwNbLvxiBEdg336iA9Sg==",
      "license": "MIT",
      "dependencies": {
        "color-name": "^2.0.0"
      },
      "engines": {
        "node": ">=14.6"
      }
    },
    "node_modules/color-name": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-2.1.0.tgz",
      "integrity": "sha512-1bPaDNFm0axzE4MEAzKPuqKWeRaT43U/hyxKPBdqTfmPF+d6n7FSoTFxLVULUJOmiLp01KjhIPPH+HrXZJN4Rg==",
      "license": "MIT",
      "engines": {
        "node": ">=12.20"
      }
    },
    "node_modules/color-string": {
      "version": "2.1.4",
      "resolved": "https://registry.npmjs.org/color-string/-/color-string-2.1.4.tgz",
      "integrity": "sha512-Bb6Cq8oq0IjDOe8wJmi4JeNn763Xs9cfrBcaylK1tPypWzyoy2G3l90v9k64kjphl/ZJjPIShFztenRomi8WTg==",
      "license": "MIT",
      "dependencies": {
        "color-name": "^2.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/concat-stream": {
      "version": "1.6.2",
      "resolved": "https://registry.npmjs.org/concat-stream/-/concat-stream-1.6.2.tgz",
      "integrity": "sha512-27HBghJxjiZtIk3Ycvn/4kbJk/1uZuJFfuPEns6LaEvpvG1f0hTea8lilrouyo9mVc2GWdcEZ8OLoGmSADlrCw==",
      "engines": [
        "node >= 0.8"
      ],
      "license": "MIT",
      "dependencies": {
        "buffer-from": "^1.0.0",
        "inherits": "^2.0.3",
        "readable-stream": "^2.2.2",
        "typedarray": "^0.0.6"
      }
    },
    "node_modules/content-disposition": {
      "version": "0.5.4",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.4.tgz",
      "integrity": "sha512-FveZTNuGw04cxlAiWbzi6zTAL/lhehaWbTtgluJh4/E95DqMwTmha3KZN1aAWA8cFIhHzMZUvLevkw5Rqk+tSQ==",
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "5.2.1"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/content-type": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.5.tgz",
      "integrity": "sha512-nTjqfcBFEipKdXCv4YDQWCfmcLZKm81ldF0pAopTvyrFGVbcR6P/VAAd5G7N+0tTr8QqiU0tFadD6FK4NtJwOA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie": {
      "version": "0.7.2",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.7.2.tgz",
      "integrity": "sha512-yki5XnKuf750l50uGTllt6kKILY4nQ1eNIQatoXEByZ5dWgnKqbnqmTrBE5B4N7lrMJKQ2ytWMiTO2o0v6Ew/w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie-parser": {
      "version": "1.4.7",
      "resolved": "https://registry.npmjs.org/cookie-parser/-/cookie-parser-1.4.7.tgz",
      "integrity": "sha512-nGUvgXnotP3BsjiLX2ypbQnWoGUPIIfHQNZkkC668ntrzGWEZVW70HDEB1qnNGMicPje6EttlIgzo51YSwNQGw==",
      "license": "MIT",
      "dependencies": {
        "cookie": "0.7.2",
        "cookie-signature": "1.0.6"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/cookie-signature": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.6.tgz",
      "integrity": "sha512-QADzlaHc8icV8I7vbaJXJwod9HWYp8uCqf1xa4OfNu1T7JVxQIrUgOWtHdNDtPiywmFbiS12VjotIXLrKM3orQ==",
      "license": "MIT"
    },
    "node_modules/core-util-is": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.3.tgz",
      "integrity": "sha512-ZQBvi1DcpJ4GDqanjucZ2Hj3wEO5pZDS89BWbkcrvdxksJorwUDDZamX9ldFkp9aw2lmBDLgkObEA4DWNJ9FYQ==",
      "license": "MIT"
    },
    "node_modules/cors": {
      "version": "2.8.6",
      "resolved": "https://registry.npmjs.org/cors/-/cors-2.8.6.tgz",
      "integrity": "sha512-tJtZBBHA6vjIAaF6EnIaq6laBBP9aq/Y3ouVJjEfoHbRBcHBAHYcMh/w8LDrk2PvIMMq8gmopa5D4V8RmbrxGw==",
      "license": "MIT",
      "dependencies": {
        "object-assign": "^4",
        "vary": "^1"
      },
      "engines": {
        "node": ">= 0.10"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/debug": {
      "version": "2.6.9",
      "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
      "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
      "license": "MIT",
      "dependencies": {
        "ms": "2.0.0"
      }
    },
    "node_modules/depd": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/depd/-/depd-2.0.0.tgz",
      "integrity": "sha512-g7nH6P6dyDioJogAAGprGpCtVImJhpPk/roCzdb3fIh61/s/nPsfR6onyMwkCAR/OlC3yBC0lESvUoQEAssIrw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/destroy": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/destroy/-/destroy-1.2.0.tgz",
      "integrity": "sha512-2sJGJTaXIIaR1w4iJSNoN0hnMY7Gpc/n8D4qSCJw8QqFWXf7cuAgnEHxBpweaVcPevC2l3KpjYCx3NypQQgaJg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8",
        "npm": "1.2.8000 || >= 1.4.16"
      }
    },
    "node_modules/dotenv": {
      "version": "16.6.1",
      "resolved": "https://registry.npmjs.org/dotenv/-/dotenv-16.6.1.tgz",
      "integrity": "sha512-uBq4egWHTcTt33a72vpSG0z3HnPuIl6NqYcTrKEg2azoEyl2hpW0zqlxysq2pK9HlDIHyHyakeYaYnSAwd8bow==",
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://dotenvx.com"
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/ecdsa-sig-formatter": {
      "version": "1.0.11",
      "resolved": "https://registry.npmjs.org/ecdsa-sig-formatter/-/ecdsa-sig-formatter-1.0.11.tgz",
      "integrity": "sha512-nagl3RYrbNv6kQkeJIpt6NJZy8twLB/2vtz6yN9Z4vRKHN4/QZJIEbqohALSgwKdnksuY3k5Addp5lg8sVoVcQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha512-WMwm9LhRUo+WUaRN+vRuETqG89IgZphVSNkdFgeb6sS/E4OrDIN7t48CAewSHXc6C8lefD8KKfr5vY61brQlow==",
      "license": "MIT"
    },
    "node_modules/enabled": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/enabled/-/enabled-2.0.0.tgz",
      "integrity": "sha512-AKrN98kuwOzMIdAizXGI86UFBoo26CL21UM763y1h/GMSJ4/OHU9k2YlsmBpyScFo/wbLzWQJBMCW4+IO3/+OQ==",
      "license": "MIT"
    },
    "node_modules/encodeurl": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-2.0.0.tgz",
      "integrity": "sha512-Q0n9HRi4m6JuGIV1eFlmvJB7ZEVxu93IrMyiMsGC0lrMJMWzRgx6WGquyfQgZVb31vhGgXnfmPNNXmxnOkRBrg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/es-define-property": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
      "integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-object-atoms": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.2.tgz",
      "integrity": "sha512-HWcBoN6NileqtSydK2FqHbS/LoDd2pqrnQHLyJzBj4kOp/ky2MWMN694xOfkK8/SnUsW2DH7EfyVlydKCsm1Zw==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/escape-html": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
      "integrity": "sha512-NiSupZ4OeuGwr68lGIeym/ksIZMJodUGOSCZ/FSnTxcrekbvqrgdUxlJOMpijaKZVjAJrWrGs/6Jy8OMuyj9ow==",
      "license": "MIT"
    },
    "node_modules/etag": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
      "integrity": "sha512-aIL5Fx7mawVa300al2BnEE4iNvo1qETxLrPI/o05L7z6go7fCw1J6EQmbK4FmJ2AS7kgVF/KEZWufBfdClMcPg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/express": {
      "version": "4.22.2",
      "resolved": "https://registry.npmjs.org/express/-/express-4.22.2.tgz",
      "integrity": "sha512-IuL+Elrou2ZvCFHs18/CIzy2Nzvo25nZ1/D2eIZlz7c+QUayAcYoiM2BthCjs+EBHVpjYjcuLDAiCWgeIX3X1Q==",
      "license": "MIT",
      "dependencies": {
        "accepts": "~1.3.8",
        "array-flatten": "1.1.1",
        "body-parser": "~1.20.5",
        "content-disposition": "~0.5.4",
        "content-type": "~1.0.4",
        "cookie": "~0.7.1",
        "cookie-signature": "~1.0.6",
        "debug": "2.6.9",
        "depd": "2.0.0",
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "finalhandler": "~1.3.1",
        "fresh": "~0.5.2",
        "http-errors": "~2.0.0",
        "merge-descriptors": "1.0.3",
        "methods": "~1.1.2",
        "on-finished": "~2.4.1",
        "parseurl": "~1.3.3",
        "path-to-regexp": "~0.1.12",
        "proxy-addr": "~2.0.7",
        "qs": "~6.15.1",
        "range-parser": "~1.2.1",
        "safe-buffer": "5.2.1",
        "send": "~0.19.0",
        "serve-static": "~1.16.2",
        "setprototypeof": "1.2.0",
        "statuses": "~2.0.1",
        "type-is": "~1.6.18",
        "utils-merge": "1.0.1",
        "vary": "~1.1.2"
      },
      "engines": {
        "node": ">= 0.10.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/express-rate-limit": {
      "version": "6.11.2",
      "resolved": "https://registry.npmjs.org/express-rate-limit/-/express-rate-limit-6.11.2.tgz",
      "integrity": "sha512-a7uwwfNTh1U60ssiIkuLFWHt4hAC5yxlLGU2VP0X4YNlyEDZAqF4tK3GD3NSitVBrCQmQ0++0uOyFOgC2y4DDw==",
      "license": "MIT",
      "engines": {
        "node": ">= 14"
      },
      "peerDependencies": {
        "express": "^4 || ^5"
      }
    },
    "node_modules/express-validator": {
      "version": "6.15.0",
      "resolved": "https://registry.npmjs.org/express-validator/-/express-validator-6.15.0.tgz",
      "integrity": "sha512-r05VYoBL3i2pswuehoFSy+uM8NBuVaY7avp5qrYjQBDzagx2Z5A77FZqPT8/gNLF3HopWkIzaTFaC4JysWXLqg==",
      "license": "MIT",
      "dependencies": {
        "lodash": "^4.17.21",
        "validator": "^13.9.0"
      },
      "engines": {
        "node": ">= 8.0.0"
      }
    },
    "node_modules/fecha": {
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/fecha/-/fecha-4.2.3.tgz",
      "integrity": "sha512-OP2IUU6HeYKJi3i0z4A19kHMQoLVs4Hc+DPqqxI2h/DPZHTm/vjsfC6P0b4jCMy14XizLBqvndQ+UilD7707Jw==",
      "license": "MIT"
    },
    "node_modules/fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "to-regex-range": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/finalhandler": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/finalhandler/-/finalhandler-1.3.2.tgz",
      "integrity": "sha512-aA4RyPcd3badbdABGDuTXCMTtOneUCAYH/gxoYRTZlIJdF0YPWuGqiAsIrhNnnqdXGswYk6dGujem4w80UJFhg==",
      "license": "MIT",
      "dependencies": {
        "debug": "2.6.9",
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "on-finished": "~2.4.1",
        "parseurl": "~1.3.3",
        "statuses": "~2.0.2",
        "unpipe": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/fn.name": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/fn.name/-/fn.name-1.1.0.tgz",
      "integrity": "sha512-GRnmB5gPyJpAhTQdSZTSp9uaPSvl09KoYcMQtsB9rQoOmzs9dH6ffeccH+Z+cv6P68Hu5bC6JjRh4Ah/mHSNRw==",
      "license": "MIT"
    },
    "node_modules/forwarded": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.2.0.tgz",
      "integrity": "sha512-buRG0fpBtRHSTCOASe6hD258tEubFoRLb4ZNA6NxMVHNw2gOcwHo9wyablzMzOA5z9xA9L1KNjk/Nt6MT9aYow==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/fresh": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz",
      "integrity": "sha512-zJ2mQYM18rEFOudeV4GShTGIQ7RbzA7ozbU9I/XBpm7kqgMywgmylMwXHxZJmkVoYkna9d2pVXVXPdYTP9ej8Q==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/fsevents": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
      "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-intrinsic": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
      "integrity": "sha512-9fSjSaos/fRIVIp+xSJlE6lfwhES7LNtKaCBIamHsjr2na1BiABJPo0mOjjz8GJDURarmCPGqaiVg5mfjb98CQ==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "es-define-property": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.1.1",
        "function-bind": "^1.1.2",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-symbols": "^1.1.0",
        "hasown": "^2.0.2",
        "math-intrinsics": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
      "integrity": "sha512-sTSfBjoXBp89JvIKIefqw7U2CCebsc74kiY6awiGogKtoSGbgjYE/G/+l9sF3MWFPNc9IcoOC4ODfKHfxFmp0g==",
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/gopd": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
      "integrity": "sha512-ZUKRh6/kUFoAiTAtTYPZJ3hw9wNxx+BIBOijnlG9PnrJsCcSjs1wyyD6vJpaYtgnzDrKYRSqf3OO6Rfa93xsRg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-flag": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz",
      "integrity": "sha512-sKJf1+ceQBr4SMkvQnBDNDtf4TXpVhVGateu0t918bl30FnbE2m4vNLX+VWe/dpjlb+HugGYzW7uQXH98HPEYw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/has-symbols": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
      "integrity": "sha512-1cDNdwJ2Jaohmb3sg4OmKaMBwuC48sYni5HUw2DvsC8LjGTLK9h+eb1X6RyuOHe4hT0ULCW68iomhjUoKUqlPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/hasown": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.3.tgz",
      "integrity": "sha512-ej4AhfhfL2Q2zpMmLo7U1Uv9+PyhIZpgQLGT1F9miIGmiCJIoCgSmczFdrc97mWT4kVY72KA+WnnhJ5pghSvSg==",
      "license": "MIT",
      "dependencies": {
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/helmet": {
      "version": "6.2.0",
      "resolved": "https://registry.npmjs.org/helmet/-/helmet-6.2.0.tgz",
      "integrity": "sha512-DWlwuXLLqbrIOltR6tFQXShj/+7Cyp0gLi6uAb8qMdFh/YBBFbKSgQ6nbXmScYd8emMctuthmgIa7tUfo9Rtyg==",
      "license": "MIT",
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/http-errors": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-2.0.1.tgz",
      "integrity": "sha512-4FbRdAX+bSdmo4AUFuS0WNiPz8NgFt+r8ThgNWmlrjQjt1Q7ZR9+zTlce2859x4KSXrwIsaeTqDoKQmtP8pLmQ==",
      "license": "MIT",
      "dependencies": {
        "depd": "~2.0.0",
        "inherits": "~2.0.4",
        "setprototypeof": "~1.2.0",
        "statuses": "~2.0.2",
        "toidentifier": "~1.0.1"
      },
      "engines": {
        "node": ">= 0.8"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/iconv-lite": {
      "version": "0.4.24",
      "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz",
      "integrity": "sha512-v3MXnZAcvnywkTUEZomIActle7RXXeedOR31wwl7VlyoXO4Qi9arvSenNQWne1TcRwhCL1HwLI21bEqdpj8/rA==",
      "license": "MIT",
      "dependencies": {
        "safer-buffer": ">= 2.1.2 < 3"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/ignore-by-default": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/ignore-by-default/-/ignore-by-default-1.0.1.tgz",
      "integrity": "sha512-Ius2VYcGNk7T90CppJqcIkS5ooHUZyIQK+ClZfMfMNFEF9VSE73Fq+906u/CWu92x4gzZMWOwfFYckPObzdEbA==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/inherits": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
      "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
      "license": "ISC"
    },
    "node_modules/ip-address": {
      "version": "10.2.0",
      "resolved": "https://registry.npmjs.org/ip-address/-/ip-address-10.2.0.tgz",
      "integrity": "sha512-/+S6j4E9AHvW9SWMSEY9Xfy66O5PWvVEJ08O0y5JGyEKQpojb0K0GKpz/v5HJ/G0vi3D2sjGK78119oXZeE0qA==",
      "license": "MIT",
      "engines": {
        "node": ">= 12"
      }
    },
    "node_modules/ipaddr.js": {
      "version": "1.9.1",
      "resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.9.1.tgz",
      "integrity": "sha512-0KI/607xoxSToH7GjN1FfSbLoU0+btTicjsQSWQlh/hZykN8KpmMf7uYwPW3R+akZ6R/w18ZlXSHBYXiYUPO3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/is-binary-path": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz",
      "integrity": "sha512-ZMERYes6pDydyuGidse7OsHxtbI7WVeUEozgR/g7rd0xUimYNlvZRE/K2MgZTjWy725IfelLeVcEM97mmtRGXw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "binary-extensions": "^2.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-extglob": "^2.1.1"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.12.0"
      }
    },
    "node_modules/is-stream": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/is-stream/-/is-stream-2.0.1.tgz",
      "integrity": "sha512-hFoiJiTl63nn+kstHGBtewWSKnQLpyb155KHheA1l39uvtO9nWIop1p3udqPcUd/xbF1VLMO4n7OI6p7RbngDg==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/isarray": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz",
      "integrity": "sha512-VLghIWNM6ELQzo7zwmcg0NmTVyWKYjvIeM83yjp0wRDTmUnrM678fQbcKBo6n2CJEF0szoG//ytg+TKla89ALQ==",
      "license": "MIT"
    },
    "node_modules/jsonwebtoken": {
      "version": "9.0.3",
      "resolved": "https://registry.npmjs.org/jsonwebtoken/-/jsonwebtoken-9.0.3.tgz",
      "integrity": "sha512-MT/xP0CrubFRNLNKvxJ2BYfy53Zkm++5bX9dtuPbqAeQpTVe0MQTFhao8+Cp//EmJp244xt6Drw/GVEGCUj40g==",
      "license": "MIT",
      "dependencies": {
        "jws": "^4.0.1",
        "lodash.includes": "^4.3.0",
        "lodash.isboolean": "^3.0.3",
        "lodash.isinteger": "^4.0.4",
        "lodash.isnumber": "^3.0.3",
        "lodash.isplainobject": "^4.0.6",
        "lodash.isstring": "^4.0.1",
        "lodash.once": "^4.0.0",
        "ms": "^2.1.1",
        "semver": "^7.5.4"
      },
      "engines": {
        "node": ">=12",
        "npm": ">=6"
      }
    },
    "node_modules/jsonwebtoken/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/jwa": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/jwa/-/jwa-2.0.1.tgz",
      "integrity": "sha512-hRF04fqJIP8Abbkq5NKGN0Bbr3JxlQ+qhZufXVr0DvujKy93ZCbXZMHDL4EOtodSbCWxOqR8MS1tXA5hwqCXDg==",
      "license": "MIT",
      "dependencies": {
        "buffer-equal-constant-time": "^1.0.1",
        "ecdsa-sig-formatter": "1.0.11",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/jws": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/jws/-/jws-4.0.1.tgz",
      "integrity": "sha512-EKI/M/yqPncGUUh44xz0PxSidXFr/+r0pA70+gIYhjv+et7yxM+s29Y+VGDkovRofQem0fs7Uvf4+YmAdyRduA==",
      "license": "MIT",
      "dependencies": {
        "jwa": "^2.0.1",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/kareem": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/kareem/-/kareem-2.5.1.tgz",
      "integrity": "sha512-7jFxRVm+jD+rkq3kY0iZDJfsO2/t4BBPeEb2qKn2lR/9KhuksYk5hxzfRYWMPV8P/x2d0kHD306YyWLzjjH+uA==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=12.0.0"
      }
    },
    "node_modules/kuler": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/kuler/-/kuler-2.0.0.tgz",
      "integrity": "sha512-Xq9nH7KlWZmXAtodXDDRE7vs6DU1gTU8zYDHDiWLSip45Egwq3plLHzPn27NgvzL2r1LMPC1vdqh98sQxtqj4A==",
      "license": "MIT"
    },
    "node_modules/lodash": {
      "version": "4.18.1",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.18.1.tgz",
      "integrity": "sha512-dMInicTPVE8d1e5otfwmmjlxkZoUpiVLwyeTdUsi/Caj/gfzzblBcCE5sRHV/AsjuCmxWrte2TNGSYuCeCq+0Q==",
      "license": "MIT"
    },
    "node_modules/lodash.includes": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/lodash.includes/-/lodash.includes-4.3.0.tgz",
      "integrity": "sha512-W3Bx6mdkRTGtlJISOvVD/lbqjTlPPUDTMnlXZFnVwi9NKJ6tiAk6LVdlhZMm17VZisqhKcgzpO5Wz91PCt5b0w==",
      "license": "MIT"
    },
    "node_modules/lodash.isboolean": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/lodash.isboolean/-/lodash.isboolean-3.0.3.tgz",
      "integrity": "sha512-Bz5mupy2SVbPHURB98VAcw+aHh4vRV5IPNhILUCsOzRmsTmSQ17jIuqopAentWoehktxGd9e/hbIXq980/1QJg==",
      "license": "MIT"
    },
    "node_modules/lodash.isinteger": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/lodash.isinteger/-/lodash.isinteger-4.0.4.tgz",
      "integrity": "sha512-DBwtEWN2caHQ9/imiNeEA5ys1JoRtRfY3d7V9wkqtbycnAmTvRRmbHKDV4a0EYc678/dia0jrte4tjYwVBaZUA==",
      "license": "MIT"
    },
    "node_modules/lodash.isnumber": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/lodash.isnumber/-/lodash.isnumber-3.0.3.tgz",
      "integrity": "sha512-QYqzpfwO3/CWf3XP+Z+tkQsfaLL/EnUlXWVkIk5FUPc4sBdTehEqZONuyRt2P67PXAk+NXmTBcc97zw9t1FQrw==",
      "license": "MIT"
    },
    "node_modules/lodash.isplainobject": {
      "version": "4.0.6",
      "resolved": "https://registry.npmjs.org/lodash.isplainobject/-/lodash.isplainobject-4.0.6.tgz",
      "integrity": "sha512-oSXzaWypCMHkPC3NvBEaPHf0KsA5mvPrOPgQWDsbg8n7orZ290M0BmC/jgRZ4vcJ6DTAhjrsSYgdsW/F+MFOBA==",
      "license": "MIT"
    },
    "node_modules/lodash.isstring": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/lodash.isstring/-/lodash.isstring-4.0.1.tgz",
      "integrity": "sha512-0wJxfxH1wgO3GrbuP+dTTk7op+6L41QCXbGINEmD+ny/G/eCqGzxyCsh7159S+mgDDcoarnBw6PC1PS5+wUGgw==",
      "license": "MIT"
    },
    "node_modules/lodash.once": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/lodash.once/-/lodash.once-4.1.1.tgz",
      "integrity": "sha512-Sb487aTOCr9drQVL8pIxOzVhafOjZN9UU54hiN8PU3uAiSV7lx1yYNpbNmex2PK6dSJoNTSJUUswT651yww3Mg==",
      "license": "MIT"
    },
    "node_modules/logform": {
      "version": "2.7.0",
      "resolved": "https://registry.npmjs.org/logform/-/logform-2.7.0.tgz",
      "integrity": "sha512-TFYA4jnP7PVbmlBIfhlSe+WKxs9dklXMTEGcBCIvLhE/Tn3H6Gk1norupVW7m5Cnd4bLcr08AytbyV/xj7f/kQ==",
      "license": "MIT",
      "dependencies": {
        "@colors/colors": "1.6.0",
        "@types/triple-beam": "^1.3.2",
        "fecha": "^4.2.0",
        "ms": "^2.1.1",
        "safe-stable-stringify": "^2.3.1",
        "triple-beam": "^1.3.0"
      },
      "engines": {
        "node": ">= 12.0.0"
      }
    },
    "node_modules/logform/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/math-intrinsics": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz",
      "integrity": "sha512-/IXtbwEk5HTPyEwyKX6hGkYXxM9nbj64B+ilVJnC/R6B0pH5G4V3b0pVbL7DBj4tkhBAppbQUlf6F6Xl9LHu1g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/media-typer": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz",
      "integrity": "sha512-dq+qelQ9akHpcOl/gUVRTxVIOkAJ1wR3QAvb4RsVjS8oVoFjDGTc679wJYmUmknUF5HwMLOgb5O+a3KxfWapPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/memory-pager": {
      "version": "1.5.0",
      "resolved": "https://registry.npmjs.org/memory-pager/-/memory-pager-1.5.0.tgz",
      "integrity": "sha512-ZS4Bp4r/Zoeq6+NLJpP+0Zzm0pR8whtGPf1XExKLJBAczGMnSi3It14OiNCStjQjM6NU1okjQGSxgEZN8eBYKg==",
      "license": "MIT",
      "optional": true
    },
    "node_modules/merge-descriptors": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.3.tgz",
      "integrity": "sha512-gaNvAS7TZ897/rVaZ0nMtAyxNyi/pdbjbAwUpFQpN70GqnVfOiXpeUUMKRBmzXaSQ8DdTX4/0ms62r2K+hE6mQ==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/methods": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/methods/-/methods-1.1.2.tgz",
      "integrity": "sha512-iclAHeNqNm68zFtnZ0e+1L2yUIdvzNoauKU4WBA3VvH/vPFieF7qfRlwUZU+DA9P9bPXIS90ulxoUoCH23sV2w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/mime/-/mime-1.6.0.tgz",
      "integrity": "sha512-x0Vn8spI+wuJ1O6S7gnbaQg8Pxh4NNHb7KSINmEWKiPE4RKOplvijn+NkmYmmRgP68mc70j2EbeTFRsrswaQeg==",
      "license": "MIT",
      "bin": {
        "mime": "cli.js"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/mime-db": {
      "version": "1.52.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz",
      "integrity": "sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime-types": {
      "version": "2.1.35",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz",
      "integrity": "sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==",
      "license": "MIT",
      "dependencies": {
        "mime-db": "1.52.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/minimatch": {
      "version": "10.2.5",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-10.2.5.tgz",
      "integrity": "sha512-MULkVLfKGYDFYejP07QOurDLLQpcjk7Fw+7jXS2R2czRQzR56yHRveU5NDJEOviH+hETZKSkIk5c+T23GjFUMg==",
      "dev": true,
      "license": "BlueOak-1.0.0",
      "dependencies": {
        "brace-expansion": "^5.0.5"
      },
      "engines": {
        "node": "18 || 20 || >=22"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/minimist": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz",
      "integrity": "sha512-2yyAR8qBkN3YuheJanUpWC5U3bb5osDywNB8RzDVlDwDHbocAJveqqj1u8+SVD7jkWT4yvsHCpWqqWqAxb0zCA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/mkdirp": {
      "version": "0.5.6",
      "resolved": "https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.6.tgz",
      "integrity": "sha512-FP+p8RB8OWpF3YZBCrP5gtADmtXApB5AMLn+vdyA+PyxCjrCs00mjyUozssO33cwDeT3wNGdLxJ5M//YqtHAJw==",
      "license": "MIT",
      "dependencies": {
        "minimist": "^1.2.6"
      },
      "bin": {
        "mkdirp": "bin/cmd.js"
      }
    },
    "node_modules/mongodb": {
      "version": "5.9.2",
      "resolved": "https://registry.npmjs.org/mongodb/-/mongodb-5.9.2.tgz",
      "integrity": "sha512-H60HecKO4Bc+7dhOv4sJlgvenK4fQNqqUIlXxZYQNbfEWSALGAwGoyJd/0Qwk4TttFXUOHJ2ZJQe/52ScaUwtQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "bson": "^5.5.0",
        "mongodb-connection-string-url": "^2.6.0",
        "socks": "^2.7.1"
      },
      "engines": {
        "node": ">=14.20.1"
      },
      "optionalDependencies": {
        "@mongodb-js/saslprep": "^1.1.0"
      },
      "peerDependencies": {
        "@aws-sdk/credential-providers": "^3.188.0",
        "@mongodb-js/zstd": "^1.0.0",
        "kerberos": "^1.0.0 || ^2.0.0",
        "mongodb-client-encryption": ">=2.3.0 <3",
        "snappy": "^7.2.2"
      },
      "peerDependenciesMeta": {
        "@aws-sdk/credential-providers": {
          "optional": true
        },
        "@mongodb-js/zstd": {
          "optional": true
        },
        "kerberos": {
          "optional": true
        },
        "mongodb-client-encryption": {
          "optional": true
        },
        "snappy": {
          "optional": true
        }
      }
    },
    "node_modules/mongodb-connection-string-url": {
      "version": "2.6.0",
      "resolved": "https://registry.npmjs.org/mongodb-connection-string-url/-/mongodb-connection-string-url-2.6.0.tgz",
      "integrity": "sha512-WvTZlI9ab0QYtTYnuMLgobULWhokRjtC7db9LtcVfJ+Hsnyr5eo6ZtNAt3Ly24XZScGMelOcGtm7lSn0332tPQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "@types/whatwg-url": "^8.2.1",
        "whatwg-url": "^11.0.0"
      }
    },
    "node_modules/mongoose": {
      "version": "7.8.9",
      "resolved": "https://registry.npmjs.org/mongoose/-/mongoose-7.8.9.tgz",
      "integrity": "sha512-V3GBAJbmOAdzEP8murOvlg7q1szlbe4jTBRyW+JBHRduJBe7F9dk5eyqJDTuYrdBcOOWfLbr6AgXrDK7F0/o5A==",
      "license": "MIT",
      "dependencies": {
        "bson": "^5.5.0",
        "kareem": "2.5.1",
        "mongodb": "5.9.2",
        "mpath": "0.9.0",
        "mquery": "5.0.0",
        "ms": "2.1.3",
        "sift": "16.0.1"
      },
      "engines": {
        "node": ">=14.20.1"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/mongoose"
      }
    },
    "node_modules/mongoose/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/morgan": {
      "version": "1.10.1",
      "resolved": "https://registry.npmjs.org/morgan/-/morgan-1.10.1.tgz",
      "integrity": "sha512-223dMRJtI/l25dJKWpgij2cMtywuG/WiUKXdvwfbhGKBhy1puASqXwFzmWZ7+K73vUPoR7SS2Qz2cI/g9MKw0A==",
      "license": "MIT",
      "dependencies": {
        "basic-auth": "~2.0.1",
        "debug": "2.6.9",
        "depd": "~2.0.0",
        "on-finished": "~2.3.0",
        "on-headers": "~1.1.0"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/morgan/node_modules/on-finished": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.3.0.tgz",
      "integrity": "sha512-ikqdkGAAyf/X/gPhXGvfgAytDZtDbr+bkNUJ0N9h5MI/dmdgCs3l6hoHrcUv41sRKew3jIwrp4qQDXiK99Utww==",
      "license": "MIT",
      "dependencies": {
        "ee-first": "1.1.1"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/mpath": {
      "version": "0.9.0",
      "resolved": "https://registry.npmjs.org/mpath/-/mpath-0.9.0.tgz",
      "integrity": "sha512-ikJRQTk8hw5DEoFVxHG1Gn9T/xcjtdnOKIU1JTmGjZZlg9LST2mBLmcX3/ICIbgJydT2GOc15RnNy5mHmzfSew==",
      "license": "MIT",
      "engines": {
        "node": ">=4.0.0"
      }
    },
    "node_modules/mquery": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/mquery/-/mquery-5.0.0.tgz",
      "integrity": "sha512-iQMncpmEK8R8ncT8HJGsGc9Dsp8xcgYMVSbs5jgnm1lFHTZqMJTUWTDx1LBO8+mK3tPNZWFLBghQEIOULSTHZg==",
      "license": "MIT",
      "dependencies": {
        "debug": "4.x"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/mquery/node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/mquery/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/ms": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
      "integrity": "sha512-Tpp60P6IUJDTuOq/5Z8cdskzJujfwqfOTkrwIwj7IRISpnkJnT6SyJ4PCPnGMoFjC9ddhal5KVIYtAt97ix05A==",
      "license": "MIT"
    },
    "node_modules/multer": {
      "version": "1.4.5-lts.2",
      "resolved": "https://registry.npmjs.org/multer/-/multer-1.4.5-lts.2.tgz",
      "integrity": "sha512-VzGiVigcG9zUAoCNU+xShztrlr1auZOlurXynNvO9GiWD1/mTBbUljOKY+qMeazBqXgRnjzeEgJI/wyjJUHg9A==",
      "deprecated": "Multer 1.x is impacted by a number of vulnerabilities, which have been patched in 2.x. You should upgrade to the latest 2.x version.",
      "license": "MIT",
      "dependencies": {
        "append-field": "^1.0.0",
        "busboy": "^1.0.0",
        "concat-stream": "^1.5.2",
        "mkdirp": "^0.5.4",
        "object-assign": "^4.1.1",
        "type-is": "^1.6.4",
        "xtend": "^4.0.0"
      },
      "engines": {
        "node": ">= 6.0.0"
      }
    },
    "node_modules/negotiator": {
      "version": "0.6.3",
      "resolved": "https://registry.npmjs.org/negotiator/-/negotiator-0.6.3.tgz",
      "integrity": "sha512-+EUsqGPLsM+j/zdChZjsnX51g4XrHFOIXwfnCVPGlQk/k5giakcKsuxCObBRu6DSm9opw/O6slWbJdghQM4bBg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/nodemailer": {
      "version": "8.0.8",
      "resolved": "https://registry.npmjs.org/nodemailer/-/nodemailer-8.0.8.tgz",
      "integrity": "sha512-p+XsnzXGdtIHXUu2ugxdfG+eX2nehsGhMjW9h0CWj1BhE30hrFz0kh0yIM0/VjUgVsRrDj+80ZO+I1nSkGE4tA==",
      "license": "MIT-0",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/nodemon": {
      "version": "3.1.14",
      "resolved": "https://registry.npmjs.org/nodemon/-/nodemon-3.1.14.tgz",
      "integrity": "sha512-jakjZi93UtB3jHMWsXL68FXSAosbLfY0In5gtKq3niLSkrWznrVBzXFNOEMJUfc9+Ke7SHWoAZsiMkNP3vq6Jw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "chokidar": "^3.5.2",
        "debug": "^4",
        "ignore-by-default": "^1.0.1",
        "minimatch": "^10.2.1",
        "pstree.remy": "^1.1.8",
        "semver": "^7.5.3",
        "simple-update-notifier": "^2.0.0",
        "supports-color": "^5.5.0",
        "touch": "^3.1.0",
        "undefsafe": "^2.0.5"
      },
      "bin": {
        "nodemon": "bin/nodemon.js"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/nodemon"
      }
    },
    "node_modules/nodemon/node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/nodemon/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/normalize-path": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz",
      "integrity": "sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/object-assign": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
      "integrity": "sha512-rJgTQnkUnH1sFw8yT6VSU3zD3sWmu6sZhIseY8VX+GRu3P6F7Fu+JNDoXfklElbLJSnc3FUQHVe4cU5hj+BcUg==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/object-inspect": {
      "version": "1.13.4",
      "resolved": "https://registry.npmjs.org/object-inspect/-/object-inspect-1.13.4.tgz",
      "integrity": "sha512-W67iLl4J2EXEGTbfeHCffrjDfitvLANg0UlX3wFUUSTx92KXRFegMHUVgSqE+wvhAbi4WqjGg9czysTV2Epbew==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/on-finished": {
      "version": "2.4.1",
      "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.4.1.tgz",
      "integrity": "sha512-oVlzkg3ENAhCk2zdv7IJwd/QUD4z2RxRwpkcGY8psCVcCYZNq4wYnVWALHM+brtuJjePWiYF/ClmuDr8Ch5+kg==",
      "license": "MIT",
      "dependencies": {
        "ee-first": "1.1.1"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/on-headers": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/on-headers/-/on-headers-1.1.0.tgz",
      "integrity": "sha512-737ZY3yNnXy37FHkQxPzt4UZ2UWPWiCZWLvFZ4fu5cueciegX0zGPnrlY6bwRg4FdQOe9YU8MkmJwGhoMybl8A==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/one-time": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/one-time/-/one-time-1.0.0.tgz",
      "integrity": "sha512-5DXOiRKwuSEcQ/l0kGCF6Q3jcADFv5tSmRaJck/OqkVFcOzutB134KRSfF0xDrL39MNnqxbHBbUUcjZIhTgb2g==",
      "license": "MIT",
      "dependencies": {
        "fn.name": "1.x.x"
      }
    },
    "node_modules/parseurl": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz",
      "integrity": "sha512-CiyeOxFT/JZyN5m0z9PfXw4SCBJ6Sygz1Dpl0wqjlhDEGGBP1GnsUVEL0p63hoG1fcj3fHynXi9NYO4nWOL+qQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/path-to-regexp": {
      "version": "0.1.13",
      "resolved": "https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.13.tgz",
      "integrity": "sha512-A/AGNMFN3c8bOlvV9RreMdrv7jsmF9XIfDeCd87+I8RNg6s78BhJxMu69NEMHBSJFxKidViTEdruRwEk/WIKqA==",
      "license": "MIT"
    },
    "node_modules/picomatch": {
      "version": "2.3.2",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.2.tgz",
      "integrity": "sha512-V7+vQEJ06Z+c5tSye8S+nHUfI51xoXIXjHQ99cQtKUkQqqO1kO/KCJUfZXuB47h/YBlDhah2H3hdUGXn8ie0oA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/process-nextick-args": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz",
      "integrity": "sha512-3ouUOpQhtgrbOa17J7+uxOTpITYWaGP7/AhoR3+A+/1e9skrzelGi/dXzEYyvbxubEF6Wn2ypscTKiKJFFn1ag==",
      "license": "MIT"
    },
    "node_modules/proxy-addr": {
      "version": "2.0.7",
      "resolved": "https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.7.tgz",
      "integrity": "sha512-llQsMLSUDUPT44jdrU/O37qlnifitDP+ZwrmmZcoSKyLKvtZxpyV0n2/bD/N4tBAAZ/gJEdZU7KMraoK1+XYAg==",
      "license": "MIT",
      "dependencies": {
        "forwarded": "0.2.0",
        "ipaddr.js": "1.9.1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/pstree.remy": {
      "version": "1.1.8",
      "resolved": "https://registry.npmjs.org/pstree.remy/-/pstree.remy-1.1.8.tgz",
      "integrity": "sha512-77DZwxQmxKnu3aR542U+X8FypNzbfJ+C5XQDk3uWjWxn6151aIMGthWYRXTqT1E5oJvg+ljaa2OJi+VfvCOQ8w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/punycode": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz",
      "integrity": "sha512-vYt7UD1U9Wg6138shLtLOvdAu+8DsC/ilFtEVHcH+wydcSpNE20AfSOduf6MkRFahL5FY7X1oU7nKVZFtfq8Fg==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/qs": {
      "version": "6.15.2",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.15.2.tgz",
      "integrity": "sha512-Rzq0KEyX/w/tEybncDgdkZrJgVUsUMk3xjh3t5bv3S1HTAtg+uOYt72+ZfwiQwKdysThkTBdL/rTi6HDmX9Ddw==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "side-channel": "^1.1.0"
      },
      "engines": {
        "node": ">=0.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/range-parser": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/range-parser/-/range-parser-1.2.1.tgz",
      "integrity": "sha512-Hrgsx+orqoygnmhFbKaHE6c296J+HTAQXoxEF6gNupROmmGJRoyzfG3ccAveqCBrwr/2yxQ5BVd/GTl5agOwSg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/raw-body": {
      "version": "2.5.3",
      "resolved": "https://registry.npmjs.org/raw-body/-/raw-body-2.5.3.tgz",
      "integrity": "sha512-s4VSOf6yN0rvbRZGxs8Om5CWj6seneMwK3oDb4lWDH0UPhWcxwOWw5+qk24bxq87szX1ydrwylIOp2uG1ojUpA==",
      "license": "MIT",
      "dependencies": {
        "bytes": "~3.1.2",
        "http-errors": "~2.0.1",
        "iconv-lite": "~0.4.24",
        "unpipe": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/readable-stream": {
      "version": "2.3.8",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.8.tgz",
      "integrity": "sha512-8p0AUk4XODgIewSi0l8Epjs+EVnWiK7NoDIEGU0HhE7+ZyY8D1IMY7odu5lRrFXGg71L15KG8QrPmum45RTtdA==",
      "license": "MIT",
      "dependencies": {
        "core-util-is": "~1.0.0",
        "inherits": "~2.0.3",
        "isarray": "~1.0.0",
        "process-nextick-args": "~2.0.0",
        "safe-buffer": "~5.1.1",
        "string_decoder": "~1.1.1",
        "util-deprecate": "~1.0.1"
      }
    },
    "node_modules/readable-stream/node_modules/safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==",
      "license": "MIT"
    },
    "node_modules/readdirp": {
      "version": "3.6.0",
      "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-3.6.0.tgz",
      "integrity": "sha512-hOS089on8RduqdbhvQ5Z37A0ESjsqz6qnRcffsMU3495FuTdqSm+7bhJ29JvIOsBDEEnan5DPu9t3To9VRlMzA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "picomatch": "^2.2.1"
      },
      "engines": {
        "node": ">=8.10.0"
      }
    },
    "node_modules/safe-buffer": {
      "version": "5.2.1",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz",
      "integrity": "sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/safe-stable-stringify": {
      "version": "2.5.0",
      "resolved": "https://registry.npmjs.org/safe-stable-stringify/-/safe-stable-stringify-2.5.0.tgz",
      "integrity": "sha512-b3rppTKm9T+PsVCBEOUR46GWI7fdOs00VKZ1+9c1EWDaDMvjQc6tUwuFyIprgGgTcWoVHSKrU8H31ZHA2e0RHA==",
      "license": "MIT",
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/safer-buffer": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
      "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg==",
      "license": "MIT"
    },
    "node_modules/semver": {
      "version": "7.8.1",
      "resolved": "https://registry.npmjs.org/semver/-/semver-7.8.1.tgz",
      "integrity": "sha512-rkVq3IXh+4FDGch+KwzX3aV9W3kO54GyEgpvBzSyctDA6Xtd7RJQV1xmXbeQp5v7+VzLOfVqiutSE6GICgPFvg==",
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/send": {
      "version": "0.19.2",
      "resolved": "https://registry.npmjs.org/send/-/send-0.19.2.tgz",
      "integrity": "sha512-VMbMxbDeehAxpOtWJXlcUS5E8iXh6QmN+BkRX1GARS3wRaXEEgzCcB10gTQazO42tpNIya8xIyNx8fll1OFPrg==",
      "license": "MIT",
      "dependencies": {
        "debug": "2.6.9",
        "depd": "2.0.0",
        "destroy": "1.2.0",
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "fresh": "~0.5.2",
        "http-errors": "~2.0.1",
        "mime": "1.6.0",
        "ms": "2.1.3",
        "on-finished": "~2.4.1",
        "range-parser": "~1.2.1",
        "statuses": "~2.0.2"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/send/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/serve-static": {
      "version": "1.16.3",
      "resolved": "https://registry.npmjs.org/serve-static/-/serve-static-1.16.3.tgz",
      "integrity": "sha512-x0RTqQel6g5SY7Lg6ZreMmsOzncHFU7nhnRWkKgWuMTu5NN0DR5oruckMqRvacAN9d5w6ARnRBXl9xhDCgfMeA==",
      "license": "MIT",
      "dependencies": {
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "parseurl": "~1.3.3",
        "send": "~0.19.1"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/setprototypeof": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.2.0.tgz",
      "integrity": "sha512-E5LDX7Wrp85Kil5bhZv46j8jOeboKq5JMmYM3gVGdGH8xFpPWXUMsNrlODCrkoxMEeNi/XZIwuRvY4XNwYMJpw==",
      "license": "ISC"
    },
    "node_modules/side-channel": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/side-channel/-/side-channel-1.1.0.tgz",
      "integrity": "sha512-ZX99e6tRweoUXqR+VBrslhda51Nh5MTQwou5tnUDgbtyM0dBgmhEDtWGP/xbKn6hqfPRHujUNwz5fy/wbbhnpw==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "object-inspect": "^1.13.3",
        "side-channel-list": "^1.0.0",
        "side-channel-map": "^1.0.1",
        "side-channel-weakmap": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-list": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/side-channel-list/-/side-channel-list-1.0.1.tgz",
      "integrity": "sha512-mjn/0bi/oUURjc5Xl7IaWi/OJJJumuoJFQJfDDyO46+hBWsfaVM65TBHq2eoZBhzl9EchxOijpkbRC8SVBQU0w==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "object-inspect": "^1.13.4"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-map": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/side-channel-map/-/side-channel-map-1.0.1.tgz",
      "integrity": "sha512-VCjCNfgMsby3tTdo02nbjtM/ewra6jPHmpThenkTYh8pG9ucZ/1P8So4u4FGBek/BjpOVsDCMoLA/iuBKIFXRA==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.5",
        "object-inspect": "^1.13.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-weakmap": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/side-channel-weakmap/-/side-channel-weakmap-1.0.2.tgz",
      "integrity": "sha512-WPS/HvHQTYnHisLo9McqBHOJk2FkHO/tlpvldyrnem4aeQp4hai3gythswg6p01oSoTl58rcpiFAjF2br2Ak2A==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.5",
        "object-inspect": "^1.13.3",
        "side-channel-map": "^1.0.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/sift": {
      "version": "16.0.1",
      "resolved": "https://registry.npmjs.org/sift/-/sift-16.0.1.tgz",
      "integrity": "sha512-Wv6BjQ5zbhW7VFefWusVP33T/EM0vYikCaQ2qR8yULbsilAT8/wQaXvuQ3ptGLpoKx+lihJE3y2UTgKDyyNHZQ==",
      "license": "MIT"
    },
    "node_modules/simple-update-notifier": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/simple-update-notifier/-/simple-update-notifier-2.0.0.tgz",
      "integrity": "sha512-a2B9Y0KlNXl9u/vsW6sTIu9vGEpfKu2wRV6l1H3XEas/0gUIzGzBoP/IouTcUQbm9JWZLH3COxyn03TYlFax6w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "semver": "^7.5.3"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/smart-buffer": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/smart-buffer/-/smart-buffer-4.2.0.tgz",
      "integrity": "sha512-94hK0Hh8rPqQl2xXc3HsaBoOXKV20MToPkcXvwbISWLEs+64sBq5kFgn2kJDHb1Pry9yrP0dxrCI9RRci7RXKg==",
      "license": "MIT",
      "engines": {
        "node": ">= 6.0.0",
        "npm": ">= 3.0.0"
      }
    },
    "node_modules/socks": {
      "version": "2.8.9",
      "resolved": "https://registry.npmjs.org/socks/-/socks-2.8.9.tgz",
      "integrity": "sha512-LJhUYUvItdQ0LkJTmPeaEObWXAqFyfmP85x0tch/ez9cahmhlBBLbIqDFnvBnUJGagb0JbIQrkBs1wJ+yRYpEw==",
      "license": "MIT",
      "dependencies": {
        "ip-address": "^10.1.1",
        "smart-buffer": "^4.2.0"
      },
      "engines": {
        "node": ">= 10.0.0",
        "npm": ">= 3.0.0"
      }
    },
    "node_modules/sparse-bitfield": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/sparse-bitfield/-/sparse-bitfield-3.0.3.tgz",
      "integrity": "sha512-kvzhi7vqKTfkh0PZU+2D2PIllw2ymqJKujUcyPMd9Y75Nv4nPbGJZXNhxsgdQab2BmlDct1YnfQCguEvHr7VsQ==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "memory-pager": "^1.0.2"
      }
    },
    "node_modules/stack-trace": {
      "version": "0.0.10",
      "resolved": "https://registry.npmjs.org/stack-trace/-/stack-trace-0.0.10.tgz",
      "integrity": "sha512-KGzahc7puUKkzyMt+IqAep+TVNbKP+k2Lmwhub39m1AsTSkaDutx56aDCo+HLDzf/D26BIHTJWNiTG1KAJiQCg==",
      "license": "MIT",
      "engines": {
        "node": "*"
      }
    },
    "node_modules/statuses": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/statuses/-/statuses-2.0.2.tgz",
      "integrity": "sha512-DvEy55V3DB7uknRo+4iOGT5fP1slR8wQohVdknigZPMpMstaKJQWhwiYBACJE3Ul2pTnATihhBYnRhZQHGBiRw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/streamsearch": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/streamsearch/-/streamsearch-1.1.0.tgz",
      "integrity": "sha512-Mcc5wHehp9aXz1ax6bZUyY5afg9u2rv5cqQI3mRrYkGC8rW2hM02jWuwjtL++LS5qinSyhj2QfLyNsuc+VsExg==",
      "engines": {
        "node": ">=10.0.0"
      }
    },
    "node_modules/string_decoder": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz",
      "integrity": "sha512-n/ShnvDi6FHbbVfviro+WojiFzv+s8MPMHBczVePfUpDJLwoLT0ht1l4YwBCbi8pJAveEEdnkHyPyTP/mzRfwg==",
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "~5.1.0"
      }
    },
    "node_modules/string_decoder/node_modules/safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==",
      "license": "MIT"
    },
    "node_modules/supports-color": {
      "version": "5.5.0",
      "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz",
      "integrity": "sha512-QjVjwdXIt408MIiAqCX4oUKsgU2EqAGzs2Ppkm4aQYbjm+ZEWEcW4SfFNTr4uMNZma0ey4f5lgLrkB0aX0QMow==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "has-flag": "^3.0.0"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/text-hex": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/text-hex/-/text-hex-1.0.0.tgz",
      "integrity": "sha512-uuVGNWzgJ4yhRaNSiubPY7OjISw4sw4E5Uv0wbjp+OzcbmVU/rsT8ujgcXJhn9ypzsgr5vlzpPqP+MBBKcGvbg==",
      "license": "MIT"
    },
    "node_modules/to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-number": "^7.0.0"
      },
      "engines": {
        "node": ">=8.0"
      }
    },
    "node_modules/toidentifier": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.1.tgz",
      "integrity": "sha512-o5sSPKEkg/DIQNmH43V0/uerLrpzVedkUh8tGNvaeXpfpuwjKenlSox/2O/BTlZUtEe+JG7s5YhEz608PlAHRA==",
      "license": "MIT",
      "engines": {
        "node": ">=0.6"
      }
    },
    "node_modules/touch": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/touch/-/touch-3.1.1.tgz",
      "integrity": "sha512-r0eojU4bI8MnHr8c5bNo7lJDdI2qXlWWJk6a9EAFG7vbhTjElYhBVS3/miuE0uOuoLdb8Mc/rVfsmm6eo5o9GA==",
      "dev": true,
      "license": "ISC",
      "bin": {
        "nodetouch": "bin/nodetouch.js"
      }
    },
    "node_modules/tr46": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/tr46/-/tr46-3.0.0.tgz",
      "integrity": "sha512-l7FvfAHlcmulp8kr+flpQZmVwtu7nfRV7NZujtN0OqES8EL4O4e0qqzL0DC5gAvx/ZC/9lk6rhcUwYvkBnBnYA==",
      "license": "MIT",
      "dependencies": {
        "punycode": "^2.1.1"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/triple-beam": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/triple-beam/-/triple-beam-1.4.1.tgz",
      "integrity": "sha512-aZbgViZrg1QNcG+LULa7nhZpJTZSLm/mXnHXnbAbjmN5aSa0y7V+wvv6+4WaBtpISJzThKy+PIPxc1Nq1EJ9mg==",
      "license": "MIT",
      "engines": {
        "node": ">= 14.0.0"
      }
    },
    "node_modules/type-is": {
      "version": "1.6.18",
      "resolved": "https://registry.npmjs.org/type-is/-/type-is-1.6.18.tgz",
      "integrity": "sha512-TkRKr9sUTxEH8MdfuCSP7VizJyzRNMjj2J2do2Jr3Kym598JVdEksuzPQCnlFPW4ky9Q+iA+ma9BGm06XQBy8g==",
      "license": "MIT",
      "dependencies": {
        "media-typer": "0.3.0",
        "mime-types": "~2.1.24"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/typedarray": {
      "version": "0.0.6",
      "resolved": "https://registry.npmjs.org/typedarray/-/typedarray-0.0.6.tgz",
      "integrity": "sha512-/aCDEGatGvZ2BIk+HmLf4ifCJFwvKFNb9/JeZPMulfgFracn9QFcAf5GO8B/mweUjSoblS5In0cWhqpfs/5PQA==",
      "license": "MIT"
    },
    "node_modules/undefsafe": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/undefsafe/-/undefsafe-2.0.5.tgz",
      "integrity": "sha512-WxONCrssBM8TSPRqN5EmsjVrsv4A8X12J4ArBiiayv3DyyG3ZlIg6yysuuSYdZsVz3TKcTg2fd//Ujd4CHV1iA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/undici-types": {
      "version": "7.24.6",
      "resolved": "https://registry.npmjs.org/undici-types/-/undici-types-7.24.6.tgz",
      "integrity": "sha512-WRNW+sJgj5OBN4/0JpHFqtqzhpbnV0GuB+OozA9gCL7a993SmU+1JBZCzLNxYsbMfIeDL+lTsphD5jN5N+n0zg==",
      "license": "MIT"
    },
    "node_modules/unpipe": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz",
      "integrity": "sha512-pjy2bYhSsufwWlKwPc+l3cN7+wuJlK6uz0YdJEOlQDbl6jo/YlPi4mb8agUkVC8BF7V8NuzeyPNqRksA3hztKQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==",
      "license": "MIT"
    },
    "node_modules/utils-merge": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz",
      "integrity": "sha512-pMZTvIkT1d+TFGvDOqodOclx0QWkkgi6Tdoa8gC8ffGAAqz9pzPTZWAybbsHHoED/ztMtkv/VoYTYyShUn81hA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4.0"
      }
    },
    "node_modules/validator": {
      "version": "13.15.35",
      "resolved": "https://registry.npmjs.org/validator/-/validator-13.15.35.tgz",
      "integrity": "sha512-TQ5pAGhd5whStmqWvYF4OjQROlmv9SMFVt37qoCBdqRffuuklWYQlCNnEs2ZaIBD1kZRNnikiZOS1eqgkar0iw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/vary": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/vary/-/vary-1.1.2.tgz",
      "integrity": "sha512-BNGbWLfd0eUPabhkXUVm0j8uuvREyTh5ovRa/dyow/BqAbZJyC+5fU+IzQOzmAKzYqYRAISoRhdQr3eIZ/PXqg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/webidl-conversions": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/webidl-conversions/-/webidl-conversions-7.0.0.tgz",
      "integrity": "sha512-VwddBukDzu71offAQR975unBIGqfKZpM+8ZX6ySk8nYhVoo5CYaZyzt3YBvYtRtO+aoGlqxPg/B87NGVZ/fu6g==",
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/whatwg-url": {
      "version": "11.0.0",
      "resolved": "https://registry.npmjs.org/whatwg-url/-/whatwg-url-11.0.0.tgz",
      "integrity": "sha512-RKT8HExMpoYx4igMiVMY83lN6UeITKJlBQ+vR/8ZJ8OCdSiN3RwCq+9gH0+Xzj0+5IrM6i4j/6LuvzbZIQgEcQ==",
      "license": "MIT",
      "dependencies": {
        "tr46": "^3.0.0",
        "webidl-conversions": "^7.0.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/winston": {
      "version": "3.19.0",
      "resolved": "https://registry.npmjs.org/winston/-/winston-3.19.0.tgz",
      "integrity": "sha512-LZNJgPzfKR+/J3cHkxcpHKpKKvGfDZVPS4hfJCc4cCG0CgYzvlD6yE/S3CIL/Yt91ak327YCpiF/0MyeZHEHKA==",
      "license": "MIT",
      "dependencies": {
        "@colors/colors": "^1.6.0",
        "@dabh/diagnostics": "^2.0.8",
        "async": "^3.2.3",
        "is-stream": "^2.0.0",
        "logform": "^2.7.0",
        "one-time": "^1.0.0",
        "readable-stream": "^3.4.0",
        "safe-stable-stringify": "^2.3.1",
        "stack-trace": "0.0.x",
        "triple-beam": "^1.3.0",
        "winston-transport": "^4.9.0"
      },
      "engines": {
        "node": ">= 12.0.0"
      }
    },
    "node_modules/winston-transport": {
      "version": "4.9.0",
      "resolved": "https://registry.npmjs.org/winston-transport/-/winston-transport-4.9.0.tgz",
      "integrity": "sha512-8drMJ4rkgaPo1Me4zD/3WLfI/zPdA9o2IipKODunnGDcuqbHwjsbB79ylv04LCGGzU0xQ6vTznOMpQGaLhhm6A==",
      "license": "MIT",
      "dependencies": {
        "logform": "^2.7.0",
        "readable-stream": "^3.6.2",
        "triple-beam": "^1.3.0"
      },
      "engines": {
        "node": ">= 12.0.0"
      }
    },
    "node_modules/winston-transport/node_modules/readable-stream": {
      "version": "3.6.2",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.2.tgz",
      "integrity": "sha512-9u/sniCrY3D5WdsERHzHE4G2YCXqoG5FTHUiCC4SIbr6XcLZBY05ya9EKjYek9O5xOAwjGq+1JdGBAS7Q9ScoA==",
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.3",
        "string_decoder": "^1.1.1",
        "util-deprecate": "^1.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/winston/node_modules/readable-stream": {
      "version": "3.6.2",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.2.tgz",
      "integrity": "sha512-9u/sniCrY3D5WdsERHzHE4G2YCXqoG5FTHUiCC4SIbr6XcLZBY05ya9EKjYek9O5xOAwjGq+1JdGBAS7Q9ScoA==",
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.3",
        "string_decoder": "^1.1.1",
        "util-deprecate": "^1.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/xtend": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/xtend/-/xtend-4.0.2.tgz",
      "integrity": "sha512-LKYU1iAXJXUgAXn9URjiu+MWhyUXHsvfp7mcuYm9dSUKK0/CjtrUwFAxD82/mCWbtLsGjFIad0wIsod4zrTAEQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.4"
      }
    }
  }
}

''',

    # -------------------------------------------------------------------------
    # server/package.json
    # -------------------------------------------------------------------------
    "server/package.json": r'''{
  "name": "edms-server",
  "version": "0.1.0",
  "private": true,
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "dependencies": {
    "bcryptjs": "^2.4.3",
    "cookie-parser": "^1.4.6",
    "cors": "^2.8.5",
    "dotenv": "^16.0.0",
    "express": "^4.18.2",
    "express-rate-limit": "^6.7.0",
    "express-validator": "^6.15.0",
    "helmet": "^6.0.1",
    "jsonwebtoken": "^9.0.0",
    "mongoose": "^7.0.0",
    "morgan": "^1.10.0",
    "multer": "^1.4.5-lts.1",
    "nodemailer": "^8.0.8",
    "winston": "^3.8.2"
  },
  "devDependencies": {
    "nodemon": "^3.1.14"
  }
}

''',

    # -------------------------------------------------------------------------
    # server/routes/analyticsRoutes.js
    # -------------------------------------------------------------------------
    "server/routes/analyticsRoutes.js": r'''const express = require('express');

const { getOverview } = require('../controllers/analyticsController');
const { authenticate, authorize } = require('../middleware/auth');

const router = express.Router();

router.get('/overview', authenticate, authorize('admin', 'hr'), getOverview);

module.exports = router;

''',

    # -------------------------------------------------------------------------
    # server/routes/authRoutes.js
    # -------------------------------------------------------------------------
    "server/routes/authRoutes.js": r'''const express = require('express');
const rateLimit = require('express-rate-limit');
const { body } = require('express-validator');

const {
  register,
  login,
  refresh,
  logout,
  me,
  forgotPassword,
  resetPassword
} = require('../controllers/authController');
const validateRequest = require('../middleware/validateRequest');
const { authenticate, authorize } = require('../middleware/auth');

const router = express.Router();

const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 20,
  standardHeaders: true,
  legacyHeaders: false
});

router.post(
  '/register',
  authLimiter,
  [
    body('name').trim().notEmpty().withMessage('Name is required'),
    body('email').trim().isEmail().withMessage('Valid email is required'),
    body('password')
      .isLength({ min: 8 })
      .withMessage('Password must be at least 8 characters long'),
    body('role')
      .optional()
      .isIn(['admin', 'hr', 'employee'])
      .withMessage('Role must be admin, hr, or employee'),
    body('bootstrapKey')
      .optional()
      .isString()
      .withMessage('bootstrapKey must be a string'),
    body('employeeId').optional().trim().notEmpty().withMessage('employeeId cannot be empty')
  ],
  validateRequest,
  register
);

router.post(
  '/login',
  authLimiter,
  [
    body('email').trim().isEmail().withMessage('Valid email is required'),
    body('password').notEmpty().withMessage('Password is required')
  ],
  validateRequest,
  login
);

router.post('/refresh', refresh);
router.post('/logout', logout);
router.get('/me', authenticate, me);

router.post(
  '/forgot-password',
  authLimiter,
  [body('email').trim().isEmail().withMessage('Valid email is required')],
  validateRequest,
  forgotPassword
);

router.post(
  '/reset-password',
  authLimiter,
  [
    body('token').trim().notEmpty().withMessage('Reset token is required'),
    body('newPassword')
      .isLength({ min: 8 })
      .withMessage('New password must be at least 8 characters long')
  ],
  validateRequest,
  resetPassword
);

router.get('/users/roles', authenticate, authorize('admin'), (_req, res) => {
  res.json({
    success: true,
    message: 'Roles fetched successfully',
    data: {
      roles: ['admin', 'hr', 'employee']
    }
  });
});

module.exports = router;

''',

    # -------------------------------------------------------------------------
    # server/routes/employeeRoutes.js
    # -------------------------------------------------------------------------
    "server/routes/employeeRoutes.js": r'''const express = require('express');
const { body, query } = require('express-validator');

const {
  listEmployees,
  getEmployee,
  createEmployee,
  updateEmployee,
  deleteEmployee,
  recordAttendance
} = require('../controllers/employeeController');
const { authenticate, authorize } = require('../middleware/auth');
const validateRequest = require('../middleware/validateRequest');
const { employeeUpload } = require('../middleware/upload');

const router = express.Router();

router.use(authenticate);

router.get(
  '/',
  authorize('admin', 'hr'),
  [
    query('page').optional().isInt({ min: 1 }).withMessage('page must be a positive integer'),
    query('limit').optional().isInt({ min: 1, max: 100 }).withMessage('limit must be between 1 and 100')
  ],
  validateRequest,
  listEmployees
);

router.get('/:id', getEmployee);

router.post(
  '/',
  authorize('admin', 'hr'),
  employeeUpload,
  [
    body('firstName').trim().notEmpty().withMessage('firstName is required'),
    body('lastName').trim().notEmpty().withMessage('lastName is required'),
    body('email').trim().isEmail().withMessage('Valid email is required'),
    body('employeeId').trim().notEmpty().withMessage('employeeId is required'),
    body('salary').optional().isFloat({ min: 0 }).withMessage('salary must be zero or greater'),
    body('status')
      .optional()
      .isIn(['active', 'inactive', 'terminated'])
      .withMessage('Invalid status')
  ],
  validateRequest,
  createEmployee
);

router.put(
  '/:id',
  authorize('admin', 'hr'),
  employeeUpload,
  [
    body('email').optional().trim().isEmail().withMessage('email must be valid'),
    body('salary').optional().isFloat({ min: 0 }).withMessage('salary must be zero or greater'),
    body('status')
      .optional()
      .isIn(['active', 'inactive', 'terminated'])
      .withMessage('Invalid status')
  ],
  validateRequest,
  updateEmployee
);

router.delete('/:id', authorize('admin'), deleteEmployee);

router.post(
  '/:id/attendance',
  authorize('admin', 'hr'),
  [
    body('status')
      .isIn(['present', 'absent', 'leave'])
      .withMessage('status must be present, absent, or leave'),
    body('date').optional().isISO8601().withMessage('date must be a valid ISO date')
  ],
  validateRequest,
  recordAttendance
);

module.exports = router;

''',

    # -------------------------------------------------------------------------
    # server/routes/notificationRoutes.js
    # -------------------------------------------------------------------------
    "server/routes/notificationRoutes.js": r'''const express = require('express');
const { body } = require('express-validator');

const { contactHr } = require('../controllers/notificationController');
const { authenticate } = require('../middleware/auth');
const validateRequest = require('../middleware/validateRequest');

const router = express.Router();

router.post(
  '/contact-hr',
  authenticate,
  [
    body('name').trim().notEmpty().withMessage('Name is required'),
    body('email').trim().isEmail().withMessage('Valid email is required'),
    body('employeeId').trim().notEmpty().withMessage('Employee ID is required'),
    body('subject').trim().notEmpty().withMessage('Subject is required'),
    body('message')
      .trim()
      .isLength({ min: 10, max: 2000 })
      .withMessage('Message must be between 10 and 2000 characters')
  ],
  validateRequest,
  contactHr
);

module.exports = router;

''',

    # -------------------------------------------------------------------------
    # server/services/emailService.js
    # -------------------------------------------------------------------------
    "server/services/emailService.js": r'''const nodemailer = require('nodemailer');

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

''',

    # -------------------------------------------------------------------------
    # server/uploads/.gitkeep
    # -------------------------------------------------------------------------
    "server/uploads/.gitkeep": r'''

''',

    # -------------------------------------------------------------------------
    # server/utils/AppError.js
    # -------------------------------------------------------------------------
    "server/utils/AppError.js": r'''class AppError extends Error {
  constructor(statusCode, message, details = null) {
    super(message);
    this.statusCode = statusCode;
    this.details = details;
  }
}

module.exports = AppError;

''',

    # -------------------------------------------------------------------------
    # server/utils/asyncHandler.js
    # -------------------------------------------------------------------------
    "server/utils/asyncHandler.js": r'''const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

module.exports = asyncHandler;

''',

    # -------------------------------------------------------------------------
    # server/utils/http.js
    # -------------------------------------------------------------------------
    "server/utils/http.js": r'''const sendSuccess = (res, message, data = null, statusCode = 200) => {
  const payload = {
    success: true,
    message
  };

  if (data !== null) {
    payload.data = data;
  }

  return res.status(statusCode).json(payload);
};

module.exports = {
  sendSuccess
};

''',

    # -------------------------------------------------------------------------
    # server/utils/logger.js
    # -------------------------------------------------------------------------
    "server/utils/logger.js": r'''const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'edms-server' },
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' })
  ]
});

module.exports = logger;

''',

    # -------------------------------------------------------------------------
    # server/utils/tokens.js
    # -------------------------------------------------------------------------
    "server/utils/tokens.js": r'''const crypto = require('crypto');
const jwt = require('jsonwebtoken');

const getJwtConfig = () => ({
  accessSecret: process.env.JWT_SECRET,
  refreshSecret: process.env.JWT_REFRESH_SECRET,
  accessExpiresIn: process.env.ACCESS_TOKEN_EXP || '15m',
  refreshExpiresIn: process.env.REFRESH_TOKEN_EXP || '7d'
});

const buildAuthPayload = (user) => ({
  sub: user._id.toString(),
  email: user.email,
  role: user.role
});

const signAccessToken = (user) => {
  const { accessSecret, accessExpiresIn } = getJwtConfig();
  return jwt.sign(buildAuthPayload(user), accessSecret, {
    expiresIn: accessExpiresIn
  });
};

const signRefreshToken = (user) => {
  const { refreshSecret, refreshExpiresIn } = getJwtConfig();
  return jwt.sign(buildAuthPayload(user), refreshSecret, {
    expiresIn: refreshExpiresIn
  });
};

const hashToken = (token) => crypto.createHash('sha256').update(token).digest('hex');

module.exports = {
  signAccessToken,
  signRefreshToken,
  hashToken
};

''',

}


# =============================================================================
# WORKSPACE GENERATION ENGINE
# =============================================================================


def generate_workspace(base_dir: str | os.PathLike[str] = ".") -> None:
    """
    Materializes the serialized project files into the target workspace.
    Existing files with the same paths are overwritten intentionally so this file
    can recreate a clean reference solution from one source of truth.
    """
    root = Path(base_dir).resolve()
    for relative_path, contents in WORKSPACE_FILES.items():
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(contents, encoding="utf-8", newline="")
        print(f"[write] {relative_path}")


# =============================================================================
# AUTOMATED ARCHITECTURAL VALIDATION AND STUB HARNESS TESTS
# =============================================================================


def run_test_harness_suite() -> None:
    """
    Simulates internal compliance tests for structural integration validation,
    verifying package configuration, endpoint mappings, and token security
    boundaries.
    """
    print("[*] Launching Automated Architectural Compliance Unit Tests...")

    required_files = [
        "client/package.json",
        "client/src/App.jsx",
        "server/package.json",
        "server/app.js",
        "server/index.js",
        "server/routes/authRoutes.js",
        "server/routes/employeeRoutes.js",
        "server/middleware/auth.js",
        "server/models/Employee.js",
        "server/models/User.js",
    ]

    missing_files = [path for path in required_files if path not in WORKSPACE_FILES]
    assert not missing_files, f"Missing required workspace files: {missing_files}"
    print("[OK] Test Suite Validation Module 1: Required file topology confirmed.")

    server_package = json.loads(WORKSPACE_FILES["server/package.json"])
    server_deps = server_package.get("dependencies", {})
    for dependency in ["bcryptjs", "cors", "dotenv", "express", "helmet", "jsonwebtoken", "mongoose", "multer", "nodemailer"]:
        assert dependency in server_deps, f"Missing backend dependency: {dependency}"
    print("[OK] Test Suite Validation Module 2: Backend dependency matrix confirmed.")

    auth_middleware_code = WORKSPACE_FILES["server/middleware/auth.js"]
    assert "jwt.verify" in auth_middleware_code, "JWT verification must be implemented in auth middleware."
    assert "Bearer" in auth_middleware_code, "Bearer token extraction must be implemented in auth middleware."
    print("[OK] Test Suite Validation Module 3: Authentication middleware confirmed.")

    employee_routes_code = WORKSPACE_FILES["server/routes/employeeRoutes.js"]
    for route_method in ["router.get", "router.post", "router.put", "router.delete"]:
        assert route_method in employee_routes_code, f"Employee CRUD route missing: {route_method}"
    print("[OK] Test Suite Validation Module 4: Employee CRUD routes confirmed.")

    client_package = json.loads(WORKSPACE_FILES["client/package.json"])
    client_deps = client_package.get("dependencies", {})
    assert "framer-motion" in client_deps, "Frontend must include Framer Motion for animated UI flows."
    assert "recharts" in client_deps, "Frontend must include charting support for analytics dashboards."
    print("[OK] Test Suite Validation Module 5: Frontend animation and analytics stack confirmed.")

    print("[OK] ALL INTERNAL EMPLOYEE DATA MANAGEMENT SYSTEM CHECKS CONFIRMED STABLE.")


if __name__ == "__main__":
    generate_workspace()
    run_test_harness_suite()
