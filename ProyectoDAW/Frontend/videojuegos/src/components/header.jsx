import '../css/header.css'
import Logo from '../assets/ArcadeStoreLogo.png'
import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

const Header = () => {
  const navigate = useNavigate()
  const [isLogged, setIsLogged] = useState(false)

  useEffect(() => {
    const update = () => {
      const token = sessionStorage.getItem('access')
      setIsLogged(!!token && token !== 'null' && token !== 'undefined')
    }

    update()

    window.addEventListener('authChange', update)

    return () => window.removeEventListener('authChange', update)
  }, [])

  const handleLogout = () => {
    sessionStorage.removeItem('access')
    setIsLogged(false)
    navigate('/')
  }

    const home = () => {
    navigate('/')
  }

  return (
    <header className="header">
      <div className="left">
        <div className="logo" onClick={home}>
          <img src={Logo} alt="ArcadeStore Logo" />
        </div>
        <div onClick={home}>
          <h1 className="title">ArcadeStore</h1>
          <p className="subtitle">Tu biblioteca personal de videojuegos</p>
        </div>
      </div>

      <div className="right">
        <button
          className="add-button"
          onClick={() => {
            if (isLogged) {
              navigate('/addGame')
            } else {
              navigate('/login')
            }
          }}
        >
          {isLogged ? '+ Añadir' : 'Iniciar sesión'}
        </button>

        <div className="profile" title="Cerrar Sesión" onClick={handleLogout}>
          👤
        </div>
      </div>
    </header>
  )
}

export default Header