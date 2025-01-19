import { useEffect } from 'react';
import axios from 'axios';
import { backEnd } from '../../settings';
import { useBunsStore } from '../store/storeBun';

const BlockSelector = () => {
    const bunsState = useBunsStore((state) => state.bunsState); // глобальное состояние плюшки
    const selectedBuns = useBunsStore((state) => state.selectedBuns); // выбранная плюшки
    const setBuns = useBunsStore((state) => state.setBuns); // действие для установки плюшки
    const selectBun = useBunsStore((state) => state.selectBun); // действие для выбора плюшки
    const setError = useBunsStore((state) => state.setError); // действие для установки ошибки
    const error = useBunsStore((state) => state.error); // ошибка из состояния

    useEffect(() => {
        axios.get(backEnd + '/api/buns/')
            .then(BunsGet => {
                setBuns(BunsGet.data); // устанавливаем данные плюшки в глобальное состояние
            })
            .catch(error => {
                setError('не удалось загрузить данные', error);
            });
    }, [setBuns, setError]);

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <>
            {bunsState.map(bun => (
                <div
                    key={bun.id}
                    className={`circle-image ${selectedBuns?.name === bun.name ? 'selected' : ''}`} // проверяем выбранную булочку
                    onClick={() => selectBun(bun.name, bun.price)} // выбираем булочку и её цену
                >
                    <img src={bun.img_buns} alt={bun.name} />
                </div>
            ))}
        </>
    );
};

export default BlockSelector;
