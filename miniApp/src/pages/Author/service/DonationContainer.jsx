import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import CreateDonation from './CreateDonation';
import { Greeting } from '../../../entities/thecase/getNameInDative';
import BlockSelector from './BlockSelection';
import QuantityInput from './QuantityInput';

import { useBunsStore } from '../store/storeBun';

const DonationContainer = (props) => {

    const selectedBuns = useBunsStore((state) => state.selectedBuns); // выбранная плюшек
    const countBun = useBunsStore((state) => state.countBun); // количество плюшек
  
    const [totalPrice, setTotalPrice] = useState(0); // Общая сумма
    const [items, setItems] = useState([]); // массив элементов для пожертвования




  


    // Вычисление общей стоимости и обновление списка элементов
    useEffect(() => {
        if (selectedBuns) {
            setTotalPrice(selectedBuns.price * countBun); 
            setItems([
                {
                    bun_name: selectedBuns.name, 
                    quantity: countBun, 
                }
            ]);
        }
    }, [selectedBuns, countBun]);




    return (
        <div className='substrate block-donation'>
            <div className='substrate block-items-donation'>
                <div className='block-items-donation child-item'>
                   
                    <BlockSelector/>
                </div>

                
                <QuantityInput />
            </div>

           
            <Greeting name={props.nickname} />

            <div className='forms-donate'>
                <CreateDonation
                    nickname={props.nickname}
                    userId={props.userId}
                    items={items}
                    onPaymentSuccess={() => alert('платеж прошел')}
                    onPaymentError={() => alert('ошибка при оплате!')}
                    sumPrice={totalPrice} 
                />
            </div>
        </div>
    );
};

DonationContainer.propTypes = {
    nickname: PropTypes.string.isRequired,
    userId: PropTypes.number,
};

export default DonationContainer;
