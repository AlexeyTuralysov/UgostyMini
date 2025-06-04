import { useEffect } from 'react';
import axios from 'axios';
import { backEnd } from '../../settings';
import { useBunsStore } from '../store/storeBun';

const BlockSelector = () => {
    const bunsState = useBunsStore((state) => state.bunsState);
    const selectedBuns = useBunsStore((state) => state.selectedBuns);
    const setBuns = useBunsStore((state) => state.setBuns);
    const selectBun = useBunsStore((state) => state.selectBun);
    const setError = useBunsStore((state) => state.setError);
    const error = useBunsStore((state) => state.error);

    useEffect(() => {
        axios.get(backEnd + '/api/buns/')
            .then(BunsGet => {
                setBuns(BunsGet.data);
            })
            .catch(error => {
                setError('Не удалось загрузить данные: ' + error.message);
            });
    }, [setBuns, setError]);

    if (error) {
        return <div>{error}</div>;
    }

    if (!Array.isArray(bunsState)) {
        return <div>Загрузка...</div>; // или <Loader />
    }

    return (
        <>
            {bunsState.map(bun => (
                <div
                    key={bun.id}
                    className={`circle-image ${selectedBuns?.name === bun.name ? 'selected' : ''}`}
                    onClick={() => selectBun(bun.name, bun.price)}
                >
                    <img src={bun.img_buns} alt={bun.name} />
                </div>
            ))}
        </>
    );
};

export default BlockSelector;