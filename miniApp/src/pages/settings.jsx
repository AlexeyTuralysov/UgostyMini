
import axios from "axios";
import { refreshToken } from "../services/auth/RefreshToken";

export const baseUrl = 'https://e823-46-48-232-152.ngrok-free.app';
export const backEnd = 'http://localhost:8000';

export const paymentUrl = 'http://localhost:2000';

//export const paymentUrl = 'http://localhost:2000/donate';
export const apiClient = axios.create({
    baseURL: 'http://localhost:8000/',
    headers: {

    }
});


apiClient.interceptors.request.use(
    async (config) =>{
        const token = localStorage.getItem('token');
        if(token){
            config.headers['Authorization'] = `Bearer ${token}`
        }
        return config;

    },
    (er)=>{
        return Promise.reject(er)
    }
    
);

apiClient.interceptors.response.use(
    (response) => {
      return response;  // Если ответ успешен, возвращаем его
    },
    async (error) => {
      const originalRequest = error.config;  // Сохраняем оригинальный запрос
  
      // Если ошибка 401 и запрос ещё не повторялся
      if (error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;  // Помечаем запрос как повторный
  
        try {
          const newAccessToken = await refreshToken();  // Пытаемся обновить токен
          localStorage.setItem('token', newAccessToken);  // Сохраняем новый access токен
  
          // Обновляем заголовки для повторного запроса
          apiClient.defaults.headers['Authorization'] = `Bearer ${newAccessToken}`;
          originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;
  
          return apiClient(originalRequest);  // Повторяем оригинальный запрос
        } catch (refreshError) {
          console.error('Ошибка обновления токена:', refreshError);
          return Promise.reject(refreshError);  // Если не удалось обновить токен
        }
      }
  
      return Promise.reject(error);  // Если ошибка не 401, просто передаем её дальше
    }
  );

export default apiClient;

