import "../css/home.css"
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  const goToLibrary = () => {
    const token = sessionStorage.getItem("access");

    if (!token) {
        const goLogin = window.confirm(
            "Necesitas iniciar sesión. ¿Quieres ir al login?"
        );

        if (goLogin) {
            navigate("/login");
        }

        return;
    }

    navigate("/library");
  };

  const goToAddGame = () => {
    const token = sessionStorage.getItem("access");

    if (!token) {
        const goLogin = window.confirm(
            "Necesitas iniciar sesión. ¿Quieres ir al login?"
        );

        if (goLogin) {
            navigate("/login");
        }

        return;
    }

    navigate("/addGame");
  };


  return (
    <div className="game-library">

  <div className="cabecera">
    <h1>Bienvenido a GameLibrary</h1>
    <p>Organiza, gestiona y descubre tu colección de videojuegos</p>

    <div className="cabecera-buttons">
      <button onClick={goToLibrary}>
          Ver Biblioteca
      </button>

      <button onClick={goToAddGame}>
          Añadir Juego
      </button>
    </div>
  </div>

  {/* STATS */}
  <div className="stats">
    <div className="stat-card">
      <div className="stat-icon">📚</div>
      <div className="stat-info">
        <h3>127</h3>
        <p>Juegos en biblioteca</p>
      </div>
    </div>

    <div className="stat-card">
      <div className="stat-icon">🏆</div>
      <div className="stat-info">
        <h3>43</h3>
        <p>Completados</p>
      </div>
    </div>

    <div className="stat-card">
      <div className="stat-icon">⭐</div>
      <div className="stat-info">
        <h3>8.4</h3>
        <p>Puntuación media</p>
      </div>
    </div>
  </div>

  {/* RECIENTES */}
  <div className="recent">
    <h2>Juegos Recientes</h2>

    <div className="recent-list">

      <div className="recent-item">
        <div className="game-left">
          <div className="game-img">IMG</div>
          <div className="game-text">
            <h4>Nombre del Juego</h4>
            <span>Plataforma · Género</span>
          </div>
        </div>
        <div className="rating">9.1 ⭐</div>
      </div>

    </div>
  </div>

</div>
  );
}

export default Home