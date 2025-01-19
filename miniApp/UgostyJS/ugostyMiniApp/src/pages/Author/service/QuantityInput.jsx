
import '../../../app/styles/widgets/inputs/TextArea.scss'
import { useBunsStore } from '../store/storeBun';
import { useState } from 'react';

export default function QuantityInput() {
    const countBun = useBunsStore((state) => state.countBun); // получаем текущее количество плюшек
    const setCount = useBunsStore((state) => state.setCount); // получаем функцию для установки плюшек

    const [inputValue, setInputValue] = useState(countBun.toString());

    const min = 0;
    const max = 99;

    const handleChange = (event) => {
        const value = event.target.value;

        // если поле пустое временно сохраняем пустую строку
        if (value === "") {
            setCount("");
            return;
        }

        
        const newValue = parseInt(value, 10);
        if (!isNaN(newValue) && newValue >= min && newValue <= max) {
            setInputValue(value); 
            setCount(newValue);  
        }
    };

    return (
        <input

            className="count input_number"
            type="number"
            value={countBun}
            onChange={handleChange} 
            min={min}
            max={max}
            placeholder="Введите количество"
        />
    );
}
