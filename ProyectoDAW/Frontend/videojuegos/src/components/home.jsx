import "../css/home.css"

const Home = () => {
  return (
    <div className="game-library">

  <div className="cabecera">
    <h1>Bienvenido a GameLibrary</h1>
    <p>Organiza, gestiona y descubre tu colección de videojuegos</p>

    <div className="cabecera-buttons">
      <button>Ver Biblioteca</button>
      <button>Añadir Juego</button>
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