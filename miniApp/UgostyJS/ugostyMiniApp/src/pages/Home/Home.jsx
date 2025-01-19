import Stories from "../../features/Stories"

import '../../app/styles/features/TimeAccount.scss'
import { Link } from "react-router-dom"


export default function Home() {
  return (
    <>
      <Stories />

      <div className="accountAc">
        
        <Link to="/alexey">Алёша</Link>

      </div>
    </>

  )
}
