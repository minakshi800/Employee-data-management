import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:4000';
const ACCESS_TOKEN_KEY = 'edms-access-token';

const readStoredToken = () => {
  if (typeof window === 'undefined') {
    return '';
  }

  return window.localStorage.getItem(ACCESS_TOKEN_KEY) || '';
};

let accessToken = readStoredToken();
let refreshPromise = null;

const api = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true
});

const refreshClient = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true
});

export const getStoredAccessToken = () => accessToken;

export const setAccessToken = (token) => {
  accessToken = token || '';

  if (typeof window !== 'undefined') {
    if (accessToken) {
      window.localStorage.setItem(ACCESS_TOKEN_KEY, accessToken);
    } else {
      window.localStorage.removeItem(ACCESS_TOKEN_KEY);
    }
  }
};

export const clearAccessToken = () => {
  setAccessToken('');
};

const refreshSession = async () => {
  if (!refreshPromise) {
    refreshPromise = refreshClient
      .post('/api/auth/refresh', {})
      .then((response) => {
        const nextToken = response.data?.data?.accessToken || '';
        setAccessToken(nextToken);
        return nextToken;
      })
      .finally(() => {
        refreshPromise = null;
      });
  }

  return refreshPromise;
};

api.interceptors.request.use((config) => {
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config || {};
    const shouldAttemptRefresh =
      error.response?.status === 401 &&
      !originalRequest._retry &&
      !originalRequest.skipAuthRefresh &&
      Boolean(accessToken);

    if (!shouldAttemptRefresh) {
      return Promise.reject(error);
    }

    originalRequest._retry = true;

    try {
      const nextToken = await refreshSession();

      if (!nextToken) {
        clearAccessToken();
        return Promise.reject(error);
      }

      originalRequest.headers = {
        ...(originalRequest.headers || {}),
        Authorization: `Bearer ${nextToken}`
      };

      return api(originalRequest);
    } catch (refreshError) {
      clearAccessToken();
      return Promise.reject(refreshError);
    }
  }
);

export const loginUser = (payload) =>
  api.post('/api/auth/login', payload, {
    skipAuthRefresh: true
  });

export const registerUser = (payload) =>
  api.post('/api/auth/register', payload, {
    skipAuthRefresh: true
  });

export const logoutUser = () => api.post('/api/auth/logout');
export const restoreSession = () => refreshSession();
export const fetchOverview = () => api.get('/api/analytics/overview');
export const fetchEmployees = () => api.get('/api/employees?limit=50');
export const fetchEmployeeById = (employeeId) => api.get(`/api/employees/${employeeId}`);
export const fetchCurrentUser = () => api.get('/api/auth/me');
export const sendContactHr = (payload) => api.post('/api/notifications/contact-hr', payload);

export default api;
