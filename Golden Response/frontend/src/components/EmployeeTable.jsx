import React, { startTransition, useDeferredValue, useState } from 'react';
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
