# EDMS Client

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
