import React, { useState } from 'react';
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
