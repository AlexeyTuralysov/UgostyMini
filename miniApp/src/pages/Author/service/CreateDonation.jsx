import PropTypes from 'prop-types';
import axios from 'axios';
import { useState,useEffect } from 'react';
import { paymentUrl } from '../../settings';
import Inputusertag from '../../../shared/inputs/Inputusertag';
import TextAreaProps from '../../../shared/inputs/TextAreaProps';
import "../../../app/styles/shared/buttons/button.scss";


const CreateDonation = ({ userId, nickname, items, onPaymentSuccess, onPaymentError, sumPrice }) => {
    const [nicknameState, setNicknameState] = useState(nickname);

    const [socialLink, setsocialLink] = useState('');
    const [customText, setCustomText] = useState('');

    const [userIdDonater, setUserId] = useState(0);
    const tg = window.Telegram?.WebApp;

    useEffect(() => {


        if (tg) {
            tg.ready();
            const user = tg.initDataUnsafe?.user;
            if (user?.id) {
                setUserId(user.id);
            } else {
                console.error("User ID not found in initDataUnsafe");
            }
        } else {
            console.error("Telegram WebApp not available");
        }
    }, []);


    {/*
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

    */}


    const sendInvoice = async () => {
        if (!userIdDonater) {
            alert("Не удалось определить Telegram пользователя");
            return;
        }

        const response = await fetch("/bot/create-invoice", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id: userIdDonater, pay_total: sumPrice * 100 }),
        });

        const data = await response.json();
        if (data.ok) {

            //window.open("https://t.me/ugostyMiniApp_bot", "_blank");
            window.close()
        } else {
            alert("Ошибка при создании инвойса");
        }
    };

  

    return (
        <form>
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
            <button onClick={sendInvoice} className='button button--pay' type="submit">Угостить {sumPrice} ₽</button>
        </form>
    );
};



export default CreateDonation;
