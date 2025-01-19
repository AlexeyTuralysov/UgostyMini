
import PropTypes from 'prop-types';


import { declineFirstname, detectGender } from 'lvovich';
import { inclineLastname } from 'lvovich';

export function Greeting({ name }) {

  const detectLanguage = (name) => {
    const cyrillicPattern = /[а-яА-ЯЁё]/;
    return cyrillicPattern.test(name) ? 'ru' : 'en';
  };

  const language = detectLanguage(name);
  let result;

  if (language === 'ru') {
      result = inclineLastname(name, 'accusative');
  } else if (language === 'en') {
      result = name.endsWith('s') ? `${name}'` : `${name}'s`; 
  } else {
      result = name; 
  }

  return (
    <h3 >Угости {result}</h3>
  );
}

Greeting.propTypes = {
  name: PropTypes.string.isRequired,
};

export default Greeting;
