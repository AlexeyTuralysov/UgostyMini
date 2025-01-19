import axios from "axios";

export const refreshToken = async () => {
    try {
      const response = await axios.post('http://localhost:8000/api/token/refresh/', {
        refresh: localStorage.getItem('refresh_token'),
      });
      localStorage.setItem('token', response.data.access);

      return response.data.access;

    } catch (error) {

      console.error('Ошибка перезаписывания токена:', error);
      throw error;
      
    }
  };