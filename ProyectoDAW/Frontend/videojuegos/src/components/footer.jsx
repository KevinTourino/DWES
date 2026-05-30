import { useNavigate } from 'react-router-dom'
import Logo from '../assets/ArcadeStoreLogo.png'
import "../css/footer.css"

const Footer = () => {
  const navigate = useNavigate()

  return (
    <footer className="footer">

      <div className="footer-left">
        <span onClick={() => navigate('/')} className="footer-link">
          Home
        </span>
      </div>

      <div className="footer-center">
        <img src={Logo} alt="ArcadeStore Logo" />
        <p>Gracias por visitar ArcadeStore</p>
      </div>

      <div className="footer-right">
        <p className="credits">feat by Hangar94</p>
      </div>

    </footer>
  )
}

export default Footer