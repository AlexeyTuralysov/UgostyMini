import PropTypes from "prop-types"
//import "../../../app/styles/substrate/substrate.scss"
import "../../../app/styles/shared/substrate/substrate_new.scss"

export default function Message({ socialName, message, date, pay }) {
    return (
        <div className="sub-message">
            {socialName? (
                <span>{socialName}</span>
            ):(
                <span>Анонимно</span>
            )}
           

            <p>{message}</p>

            <div className="date">{date}</div>
            <div className="pay">+{pay} ₽</div>

        </div>
    )
}


Message.propTypes = {
    id: PropTypes.number.isRequired,
    socialName: PropTypes.string.isRequired,
    message: PropTypes.string.isRequired,
    date: PropTypes.string.isRequired

};

