import { createContext, startTransition, useContext, useEffect, useState } from 'react';

import {
  clearAccessToken,
  fetchCurrentUser,
  fetchEmployeeById,
  fetchEmployees,
  fetchOverview,
  getStoredAccessToken,
  loginUser as loginRequest,
  logoutUser as logoutRequest,
  registerUser as registerRequest,
  restoreSession,
  sendContactHr,
  setAccessToken
} from '../lib/api';

const AppContext = createContext(null);

const emptyAnalytics = {
  totalEmployees: 0,
  departmentDistribution: [],
  salarySummary: {
    averageSalary: 0,
    totalSalary: 0,
    maxSalary: 0,
    minSalary: 0
  },
  monthlyHiring: [],
  attendanceSummary: [],
  recentActivity: []
};

const getStoredTheme = () => {
  if (typeof window === 'undefined') {
    return 'light';
  }

  return window.localStorage.getItem('edms-theme') || 'light';
};

const buildPersonalAnalytics = (employee) => {
  if (!employee) {
    return emptyAnalytics;
  }

  const attendanceBuckets = (employee.attendance || []).reduce(
    (totals, entry) => ({
      ...totals,
      [entry.status]: (totals[entry.status] || 0) + 1
    }),
    {}
  );

  const attendanceSummary = Object.entries(attendanceBuckets).map(([status, count]) => ({
    status,
    count
  }));

  const joinedAt = employee.joiningDate ? new Date(employee.joiningDate) : null;
  const monthlyHiring = joinedAt
    ? [
        {
          _id: {
            year: joinedAt.getFullYear(),
            month: joinedAt.getMonth() + 1
          },
          hires: 1
        }
      ]
    : [];

  return {
    totalEmployees: 1,
    departmentDistribution: employee.department
      ? [{ department: employee.department, count: 1 }]
      : [],
    salarySummary: {
      averageSalary: employee.salary || 0,
      totalSalary: employee.salary || 0,
      maxSalary: employee.salary || 0,
      minSalary: employee.salary || 0
    },
    monthlyHiring,
    attendanceSummary,
    recentActivity: [
      {
        _id: employee._id,
        firstName: employee.firstName,
        lastName: employee.lastName,
        employeeId: employee.employeeId,
        department: employee.department,
        updatedAt: employee.updatedAt || employee.createdAt || new Date().toISOString()
      }
    ]
  };
};

export const AppProvider = ({ children }) => {
  const [theme, setTheme] = useState(getStoredTheme);
  const [employees, setEmployees] = useState([]);
  const [analytics, setAnalytics] = useState(emptyAnalytics);
  const [currentUser, setCurrentUser] = useState(null);
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [isProfileOpen, setIsProfileOpen] = useState(false);
  const [isContactOpen, setIsContactOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [notice, setNotice] = useState('');

  useEffect(() => {
    document.documentElement.classList.toggle('dark', theme === 'dark');
    window.localStorage.setItem('edms-theme', theme);
  }, [theme]);

  const clearWorkspace = () => {
    startTransition(() => {
      setCurrentUser(null);
      setEmployees([]);
      setAnalytics(emptyAnalytics);
      setSelectedEmployee(null);
      setIsProfileOpen(false);
      setIsContactOpen(false);
    });
  };

  const loadRoleBasedData = async (sessionUser) => {
    if (!sessionUser) {
      return;
    }

    if (sessionUser.role === 'employee') {
      let employeeRecord = sessionUser.employee || null;

      if (employeeRecord?._id) {
        try {
          const employeeResponse = await fetchEmployeeById(employeeRecord._id);
          employeeRecord = employeeResponse.data?.data?.employee || employeeRecord;
        } catch (_error) {
          employeeRecord = sessionUser.employee || null;
        }
      }

      const hydratedUser = {
        ...sessionUser,
        employee: employeeRecord
      };

      startTransition(() => {
        setCurrentUser(hydratedUser);
        setEmployees(employeeRecord ? [employeeRecord] : []);
        setAnalytics(buildPersonalAnalytics(employeeRecord));
      });

      return;
    }

    const [overviewResponse, employeesResponse] = await Promise.all([
      fetchOverview(),
      fetchEmployees()
    ]);

    startTransition(() => {
      setCurrentUser(sessionUser);
      setAnalytics(overviewResponse.data?.data || emptyAnalytics);
      setEmployees(employeesResponse.data?.data?.items || []);
    });
  };

  const initializeSession = async () => {
    setIsLoading(true);

    try {
      if (!getStoredAccessToken()) {
        try {
          const refreshResponse = await restoreSession();
          const refreshedToken = refreshResponse?.data?.data?.accessToken || refreshResponse;

          if (refreshedToken) {
            setAccessToken(refreshedToken);
          }
        } catch (_error) {
          clearAccessToken();
          clearWorkspace();
          setNotice('');
          setIsLoading(false);
          return;
        }
      }

      const userResponse = await fetchCurrentUser();
      const sessionUser = userResponse.data?.data?.user || null;

      if (!sessionUser) {
        throw new Error('Session could not be restored');
      }

      setNotice('');
      try {
        await loadRoleBasedData(sessionUser);
      } catch (error) {
        startTransition(() => {
          setCurrentUser(sessionUser);
          setEmployees(sessionUser.employee ? [sessionUser.employee] : []);
          setAnalytics(
            sessionUser.role === 'employee'
              ? buildPersonalAnalytics(sessionUser.employee)
              : emptyAnalytics
          );
        });
        setNotice(
          error.response?.data?.message ||
            'Your session is active, but some workspace data could not be loaded.'
        );
      }
    } catch (error) {
      clearAccessToken();
      clearWorkspace();
      setNotice(error.response?.data?.message || 'Your session has expired. Please sign in again.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    initializeSession();
  }, []);

  const toggleTheme = () => {
    setTheme((currentTheme) => (currentTheme === 'light' ? 'dark' : 'light'));
  };

  const openEmployee = (employee) => {
    setSelectedEmployee(employee);
    setIsProfileOpen(true);
  };

  const closeEmployee = () => {
    setIsProfileOpen(false);
  };

  const openContactModal = () => setIsContactOpen(true);
  const closeContactModal = () => setIsContactOpen(false);
  const clearNotice = () => setNotice('');

  const loginUser = async (payload) => {
    try {
      const response = await loginRequest(payload);
      const token = response.data?.data?.tokens?.accessToken || '';
      setAccessToken(token);
      await initializeSession();
      return { success: true };
    } catch (error) {
      clearAccessToken();
      clearWorkspace();
      return {
        success: false,
        message: error.response?.data?.message || 'Unable to sign in with those credentials.',
        details: error.response?.data?.details || []
      };
    }
  };

  const registerUser = async (payload) => {
    try {
      const response = await registerRequest(payload);
      const token = response.data?.data?.tokens?.accessToken || '';
      setAccessToken(token);
      await initializeSession();
      return { success: true };
    } catch (error) {
      clearAccessToken();
      clearWorkspace();
      return {
        success: false,
        message: error.response?.data?.message || 'Unable to create your account right now.',
        details: error.response?.data?.details || []
      };
    }
  };

  const logoutUser = async () => {
    try {
      await logoutRequest();
    } catch (_error) {
      // Clear the local session even if the server-side logout call fails.
    }

    clearAccessToken();
    clearWorkspace();
    setNotice('You have been signed out.');
  };

  const submitContactRequest = async (payload) => {
    try {
      const response = await sendContactHr(payload);
      setNotice(response.data?.message || 'HR request submitted successfully.');
      return { success: true, preview: false };
    } catch (error) {
      const message = error.response?.data?.message || 'Unable to send the request right now.';
      setNotice(message);
      return { success: false, preview: false, message };
    }
  };

  const canManageEmployees = ['admin', 'hr'].includes(currentUser?.role || '');

  return (
    <AppContext.Provider
      value={{
        analytics,
        canManageEmployees,
        clearNotice,
        closeContactModal,
        closeEmployee,
        currentUser,
        employees,
        initializeSession,
        isAuthenticated: Boolean(currentUser),
        isContactOpen,
        isLoading,
        isProfileOpen,
        loginUser,
        logoutUser,
        notice,
        openContactModal,
        openEmployee,
        registerUser,
        selectedEmployee,
        submitContactRequest,
        theme,
        toggleTheme
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => {
  const context = useContext(AppContext);

  if (!context) {
    throw new Error('useAppContext must be used within an AppProvider');
  }

  return context;
};
