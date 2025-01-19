import { useSpring, animated } from '@react-spring/web';
import PropTypes from 'prop-types';
import '../../app/styles/shared/stats/statsTreats.scss';
import { useEffect } from 'react';
import { backEnd, apiClient } from '../../pages/settings';

function StatTreats(props) {
    const { count, color, image } = props;



    const [animationProps, api] = useSpring(() => ({
        from: { number: 0 },
        to: { number: count },
        config: { duration: 1000 },
    }));

    useEffect(() => {
        api.start({ to: { number: count } });
    }, [count, api]);

    return (
        <div className="treats" style={{ backgroundColor: color }}>
            <img src={backEnd + image} alt="Stat Icon" />
            <animated.span id='out'>
                {animationProps.number.to(val => val.toFixed(0))}
            </animated.span>
        </div>
    );
}

StatTreats.propTypes = {
    image: PropTypes.string.isRequired,
    color: PropTypes.string,
    count: PropTypes.number.isRequired,
};

export default StatTreats;
