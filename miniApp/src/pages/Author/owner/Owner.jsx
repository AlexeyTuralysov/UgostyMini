import React from 'react'
import './../../../app/styles/shared/buttons/button.scss'
import './../../../app/styles/OwnerPanel/OwnerPanel.scss'
import { useNavigate } from 'react-router-dom';

export default function Owner({ author }) {
    const navigate = useNavigate();

    return (
        <div className='OwnerPanel'>

            <div className='chid-owner'>
                <button className="button button--edit" onClick={() => navigate(`/${author}/edit`)}>
                    Редактирование
                </button>


                <button className="button button--edit" onClick={() => navigate(`/${author}/donations`)}>
                    Выплаты
                </button>
            </div>





        </div>
    )
}
