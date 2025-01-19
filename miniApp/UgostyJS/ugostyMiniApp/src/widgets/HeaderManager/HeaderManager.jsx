import '../../app/styles/widgets/HeaderManager/HeaderManagerStyle.scss'
import { Outlet } from 'react-router-dom';
import { NavLink } from "react-router-dom";
import getNameFromJwt from '../../services/auth/authService';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import { faPenToSquare,faMoneyBill } from '@fortawesome/free-solid-svg-icons';

export default function HeaderManager() {
    const jwt = localStorage.getItem('token');
    const name = getNameFromJwt(jwt);

    return (
        <>
            <div className="sidebar">
             
                <NavLink 
                    to={`/${name}/donations`}
                    className={({ isActive }) => isActive ? 'active' : ''}
                >
                     <FontAwesomeIcon className='svg' icon={faMoneyBill} />
                    
                </NavLink>

                <NavLink 
                    to={`/${name}/edit`}
                    className={({ isActive }) => isActive ? 'active' : ''}
                >
                   
                    <FontAwesomeIcon className='svg' icon={faPenToSquare} />
                    
                </NavLink>
            </div>
          
            <Outlet />
        </>
    );
}
