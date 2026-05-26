# EDMS Server

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
