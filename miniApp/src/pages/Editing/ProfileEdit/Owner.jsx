
import PropTypes from 'prop-types';

const Owner = (props) => {


    return (
        <div className='edit-profile'>
            <h3>Редактировать профиль</h3>
            <form>
                <label>Никнейм:{props.nickname}</label>

                <button type="submit">Сохранить</button>
            </form>
        </div>
    )
}

Owner.propTypes = {
    nickname: PropTypes.string.isRequired
};

export default Owner;
