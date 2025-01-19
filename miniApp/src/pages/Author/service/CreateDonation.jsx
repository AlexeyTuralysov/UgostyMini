import PropTypes from 'prop-types';
import axios from 'axios';
import { useState } from 'react';
import { paymentUrl } from '../../settings';
import Inputusertag from '../../../shared/inputs/Inputusertag';
import TextAreaProps from '../../../shared/inputs/TextAreaProps';
import "../../../app/styles/shared/buttons/button.scss";


const CreateDonation = ({ userId, nickname, items, onPaymentSuccess, onPaymentError, sumPrice }) => {
    const [nicknameState, setNicknameState] = useState(nickname);

    const [socialLink, setsocialLink] = useState('');
    const [customText, setCustomText] = useState('');


    const handleSubmit = async (event) => {
        event.preventDefault();

        const donationPay = {
            donation_profile_id: userId,
            //nickname: nicknameState,
            social_media: socialLink,
            donation_message: customText,
            items
        };
        console.log('Отправляемые данные:', donationPay);

        try {
            const response = await axios.post(`${paymentUrl}/donate/`, donationPay);
            console.log(response.data);
            window.location.assign(response.data.confirmation_url);

            if (onPaymentSuccess) {
                onPaymentSuccess(response.data);
            }
        } catch (error) {
            console.error('ошибка платежа:', error);
            if (onPaymentError) {
                onPaymentError(error);
            }
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <Inputusertag
                custom_text="Имя или ваш @тег соцсети"
                value={socialLink}
                onChange={(e) => {
                    setsocialLink(e.target.value);
                   
                }}
            />
            <TextAreaProps
                custom_text='Похлебай чаю...'
                value={customText}
                onChange={(e) => {
                    setCustomText(e.target.value);
                    
                }}
            />
            <button className='button button--pay' type="submit">Угостить {sumPrice} ₽</button>
        </form>
    );
};



export default CreateDonation;
