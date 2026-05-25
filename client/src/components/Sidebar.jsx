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
