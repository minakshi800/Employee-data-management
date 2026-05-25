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
