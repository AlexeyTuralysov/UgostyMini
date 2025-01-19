import { Navigate, useParams } from 'react-router-dom';
import getNameFromJwt from './authService';

function ProtectedRoute({ children }) {
  const { author } = useParams();
  const jwt = localStorage.getItem('token');
  const currentUser = getNameFromJwt(jwt);

  if (currentUser !== author) {
    return <Navigate to="/" replace />; // Перенаправление на главную страницу, если пользователь не владелец
  }

  return children; // Рендерим дочерние элементы, если проверка пройдена
}

export default ProtectedRoute;
