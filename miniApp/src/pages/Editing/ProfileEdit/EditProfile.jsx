import { useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import getNameFromJwt from '../../../services/auth/authService';

export default function EditProfile() {
  const { author } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const jwt = localStorage.getItem('token');
    const userName = getNameFromJwt(jwt);

    if (userName !== author) {
      navigate('/'); // Перенаправление, если пользователь не владелец профиля
    }
  }, [author, navigate]);

  return (
    <div className='content'>
      <h1>Редакт</h1>
    </div>
  );
}
