# AI-Powered Employee Data Management System

## Context and Role

You're acting as a senior full-stack developer who has been handed a real client project. The client is a mid-sized company that needs a proper internal HR tool — not a template, not a demo, but something their team will actually use every day to manage their workforce.

The platform needs to work for three types of people:

- HR managers who are constantly adding and updating employee records
- Admins who need oversight of everything
- Employees who just want to check their own profile

Each of them has different needs and different levels of access, so the system has to handle that cleanly without things breaking or leaking data between roles.

The look and feel matters here. The client wants something that feels modern and fast — smooth animations, a clean dashboard, nothing that looks like it was slapped together.

At the same time, the codebase needs to be maintainable because their internal dev team will be taking it over after handoff. So write code like someone else has to read it tomorrow.

---

# Objective

Here's what this project actually needs to do when it's done:

- Give users a secure way to sign up, log in, and stay logged in across sessions without having to re-authenticate every few minutes.
- Let HR managers and admins fully manage employee records — adding people, updating their details, removing them when needed, and organizing everything by department, salary, or date.
- Make sure each role only sees and does what they're supposed to.
- Build a dashboard that actually looks good.
- Hook up email notifications.
- Include analytics for workforce insights.
- Make the system production-ready with proper validation and security.

---

# Tech Stack

## Frontend

- React.js
- Framer Motion
- Tailwind CSS
- Axios
- React Router v6
- Context API
- Recharts

## Backend

- Node.js
- Express.js
- MongoDB with Mongoose
- JWT Authentication
- bcrypt
- Nodemailer
- Multer
- Helmet.js
- express-rate-limit
- dotenv
- cors

---

# Project Structure

```bash
project-root/
├── frontend/     # React app
├── backend/      # Express API server
└── admin/        # Standalone admin dashboard
```

## Frontend Structure

Frontend should contain:

```bash
frontend/
├── components/
├── pages/
├── context/
├── hooks/
├── utils/
├── animations/
└── api/
```

### Important Rule

Every Axios call must live inside the `api/` folder.

No component should directly call the backend.

---

## Backend Structure

```bash
backend/
├── routes/
├── controllers/
├── middleware/
├── models/
├── config/
└── utils/
```

### Rules

- Routes only define endpoints
- Controllers contain business logic
- Middleware stays isolated

---

## Admin Dashboard

Standalone site using:

- HTML
- CSS
- Vanilla JavaScript

Pages:

- Overview
- Profile
- Settings
- Help

---

# Features Required

---

# 1. User Authentication System

Build:

- Signup
- Login
- Logout
- Persistent Sessions
- Access + Refresh Token Flow

## Requirements

- Passwords hashed with bcrypt
- Passwords never returned in API responses
- Auto logout on token expiry
- Navbar displays:
  - Avatar
  - Name
  - Role
- Unauthenticated users redirected to login

---

# 2. Employee Management System

Each employee record should include:

- Full name
- Email
- Phone number
- Department
- Job title
- Salary
- Joining date
- Profile photo
- Home address
- Personal notes
- Emergency contact
- Favorite flag
- Added by
- Timestamps

## Employee List Features

### Search

- Name
- Department
- Job title

### Filter

- Department
- Date range

### Sort

- Name
- Salary
- Joining date
- Ascending / Descending

### Pagination

- 10 records per page

### Loading State

- Skeleton cards

### Dashboard Features

- Recently Added Employees
- Empty state illustration

---

# 3. Role-Based Access Control

| Role | Permissions |
|------|-------------|
| Admin | Full access |
| HR Manager | Add/Edit employees only |
| Employee | View own profile only |

## Frontend Rules

- Use ProtectedRoute
- Redirect unauthorized users
- Sidebar links depend on role

## Backend Rules

- JWT verification middleware
- Role middleware
- Unauthorized access returns 403

---

# 4. UI and Animation Requirements

Framer Motion handles every animation.

## Required Animations

- Page fade + slide transitions
- Staggered employee cards
- Animated stat counters
- Modal scale animations
- Sidebar transitions
- Hover lift effects

## Performance Rules

Animate only:

- transform
- opacity

Avoid:

- width
- height
- top
- left

### Additional Rules

- Use AnimatePresence
- Use layout prop
- initial animations only once

---

# 5. Layout Requirements

## Main Layout

- Fixed sidebar
- Scrollable content
- Sticky navbar

## Navbar

Contains:

- Logo
- Search bar
- Theme toggle
- User avatar
- Name
- Role

## Sidebar Links

- Dashboard
- Employees
- Analytics
- Settings
- Help

## Responsive Behavior

- Tablet → icon-only sidebar
- Mobile → hamburger menu

---

## Dashboard Sections

### Stat Cards

- Total Employees
- Departments
- New Hires
- Average Salary
- Active Employees
- Favorited Employees

### Charts

- Employee Growth
- Department Distribution

### Recent Employees Table

Columns:

- Name
- Department
- Role
- Salary
- Joining Date
- Actions

---

## Design Rules

- rounded-2xl
- Smooth shadows
- Indigo accent color
- Dark mode support
- p-6 padding
- gap-6 spacing

---

# 6. Contact and Notification System

A floating **Contact HR** button must appear globally.

## Contact Form Fields

- Full Name
- Email
- Employee ID
- Subject
- Message

### Validation

- Minimum 20 characters in message

## Form Behavior

- Client-side validation
- Send email using Nodemailer
- Success toast + smooth close animation
- Inline error handling

---

## Automated Email Events

- New employee added
- Employee updated
- New user registered
- Password reset requested
- Contact form submitted

## Email Format

Each email includes:

- Subject
- Greeting
- Event description
- Relevant data
- Footer with timestamp and system name

---

# 7. Backend System Requirements

## Authentication Routes

```http
POST /api/auth/signup
POST /api/auth/login
POST /api/auth/logout
POST /api/auth/refresh-token
POST /api/auth/forgot-password
POST /api/auth/reset-password
```

## Employee Routes

```http
GET    /api/employees
GET    /api/employees/:id
POST   /api/employees
PUT    /api/employees/:id
DELETE /api/employees/:id
PATCH  /api/employees/:id/favorite
POST   /api/employees/:id/upload
```

## Analytics Routes

```http
GET /api/analytics/summary
GET /api/analytics/growth
GET /api/analytics/departments
GET /api/analytics/salary-trends
```

## Contact Route

```http
POST /api/contact
```

---

# API Response Format

## Success Response

```json
{
  "success": true,
  "message": "Readable success message",
  "data": {}
}
```

## Error Response

```json
{
  "success": false,
  "message": "Readable error message",
  "errors": []
}
```

## Pagination Response

```json
{
  "success": true,
  "message": "Employees fetched successfully",
  "data": [],
  "pagination": {
    "total": 100,
    "page": 1,
    "limit": 10,
    "totalPages": 10
  }
}
```

---

# 8. Security Requirements

## Authentication Security

- bcrypt salt rounds = 10
- Access token expiry = 15 minutes
- Refresh token expiry = 7 days
- Refresh tokens stored in database
- Tokens removed on logout

## Data Security

- Password fields excluded using `.select()`
- Validate and sanitize all inputs
- Reject script/HTML tags
- Validate MongoDB ObjectId

## Server Security

- Rate limiting enabled
- Helmet.js security headers
- Strict CORS setup

---

# Environment Variables

```env
MONGODB_URI=
JWT_SECRET=
JWT_REFRESH_SECRET=
FRONTEND_URL=

EMAIL_HOST=
EMAIL_PORT=
EMAIL_USER=
EMAIL_PASS=

HR_EMAIL=

NODE_ENV=
```

---

# 9. Error Handling Requirements

## Global Error Handler

- Development → full stack trace
- Production → safe error messages only

## Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 400 | Validation error |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not found |
| 409 | Conflict |
| 500 | Server error |

---

## Frontend Error Handling

- 401 → logout + redirect
- 403 → permission denied toast
- 400/422 → inline validation errors
- Network failure → retry toast
- 500 → generic error toast

## Toast System

- Framer Motion animations
- Top-right position
- Stackable
- Auto-dismiss after 4 seconds
- Close button included

### Toast Colors

- Green → success
- Red → error
- Yellow → warning
- Blue → info

---

# 10. Performance and Scalability

## Frontend Optimization

- React.lazy + Suspense
- Debounced search (300ms)
- React.memo for EmployeeCard
- Paginated lists
- Lazy-loaded profile images
- Skeleton loaders everywhere

## Backend Optimization

- Indexes on department, name, email
- Unique email index
- Use `.lean()` for read-only queries
- Use `.select()` for minimal data
- Cache analytics summary for 60 seconds

## Scalability Rules

- Store uploads on Cloudinary or S3
- Config values in environment variables
- Features must remain modular

---

# 11. Documentation Requirements

README must include:

- Project overview
- Feature summary
- Tech stack
- Installation requirements
- Setup instructions
- Environment variable guide
- MongoDB Atlas setup
- Gmail App Password setup
- Full API documentation
- Folder structure explanation
- Deployment instructions

---

# Development Flow

Follow this order:

1. Setup Express server
2. Create schemas
3. Build auth system
4. Build employee CRUD
5. Build analytics
6. Configure Nodemailer
7. Test APIs in Postman
8. Setup React app
9. Setup Context API
10. Build auth pages
11. Build layout
12. Build dashboard
13. Build employee list
14. Build modals
15. Build profile page
16. Build analytics page
17. Build settings/help pages
18. Add animations
19. Build Contact HR modal
20. Add theme toggle
21. Build toast system
22. Add loaders and empty states
23. End-to-end testing

---

# Final Output Required

Deliver:

- Complete frontend
- Complete backend
- Complete admin dashboard
- Organized folder structure
- `.env.example`
- Complete README
- Inline route/controller comments
- Local setup instructions
- Deployment guide

---

# Final Goal

This should become a real production-ready HR platform — not just a portfolio project.

The application must:

- Handle real employee data
- Enforce real permissions
- Send real emails
- Scale properly
- Look polished and modern

The next development team should be able to understand the structure quickly and continue development without needing a walkthrough.
