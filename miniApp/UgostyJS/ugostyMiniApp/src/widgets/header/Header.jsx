import { Outlet } from 'react-router-dom'
import '../../app/styles/widgets/header/hedaer.scss'

export default function Header() {
  return (
    <div className='header'>

    

      <video width="100" autoPlay loop muted  >

        
        <source src="/src/assets/img/header/0001-0250.webm" type="video/webm"></source>
        Ваш браузер не поддерживает элемент видео.
      </video>
    <Outlet/>
    </div>
  )
}
