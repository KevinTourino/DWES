import '../css/header.css'
import Logo from '../assets/ArcadeStoreLogo.png'

const Header = () => {
  return (
    <header className="header">
      <div className="left">
        <div className="logo">
          <img src={Logo} alt="ArcadeStore Logo" />
        </div>
        <div>
          <h1 className="title">ArcadeStore</h1>
          <p className="subtitle">Tu biblioteca personal de videojuegos</p>
        </div>
      </div>

      <div className="right">
        <button className="add-button">
          + Añadir
        </button>
        <div className="profile">
          👤
        </div>
      </div>

    </header>
  )
}

export default Header