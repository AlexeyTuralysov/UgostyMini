import PropTypes from 'prop-types';
import './../../app/styles/widgets/inputs/TextArea.scss'

const TextAreaProps=(props) =>  {
  return (
    <textarea name="" placeholder={props.custom_text} value={props.value} onChange={props.onChange} id=""></textarea>
  )
}

TextAreaProps.propTypes = {
  custom_text: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired
};

export default TextAreaProps;