import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Перед каждым запросом добавляем заголовок Authorization, если токен сохранён
axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Перехватываем ответы для автоматического обновления токена
axiosInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = localStorage.getItem('refreshToken');
      try {
        const response = await axios.post('http://localhost:8000/api/auth/token/refresh/', { refresh: refreshToken });
        localStorage.setItem('accessToken', response.data.access);
        axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
        return axiosInstance(originalRequest);
      } catch (err) {
        // Если обновление токена не удалось, перенаправляем на страницу логина
        window.location.href = '/login';
        return Promise.reject(err);
      }
    }
    return Promise.reject(error);
  }
);

export default axiosInstance; 
// 2023-01-21: Record JWT refresh timing vs axios queue (staging)

// 2023-02-02: Align frontend env base URL (CI runner)

// 2023-02-12: Stub docker compose service links (prod checklist)

// 2023-02-23: Clarify JWT refresh timing vs axios queue (CI runner)

// 2023-03-06: Capture Redux task normalization (demo box)

// 2023-03-21: Tighten DRF pagination cursor vs offset (demo box)
