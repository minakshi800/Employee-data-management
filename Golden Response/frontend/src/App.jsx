import React, { useState } from 'react';
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
