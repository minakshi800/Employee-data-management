import React from 'react';
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
