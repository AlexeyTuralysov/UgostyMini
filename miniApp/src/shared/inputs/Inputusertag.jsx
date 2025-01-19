import PropTypes from 'prop-types';
import './../../app/styles/widgets/inputs/input.scss'


const Inputusertag =(props) => {
  return  <input className='input' type="text" name="user-tag" placeholder={props.custom_text}  
   value={props.value} onChange={props.onChange} />
  
}

Inputusertag.propTypes = {
  custom_text: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired 
};
export default Inputusertag;