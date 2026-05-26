import React, { useEffect, useState } from 'react';
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
