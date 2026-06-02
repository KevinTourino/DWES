import "../css/home.css"
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

const Home = () => {
  const navigate = useNavigate();

  const [stats, setStats] = useState({
    total_juegos: 0,
    total_completados: 0,
    ultimos_juegos: []
  });


  useEffect(() => {
  fetch("http://localhost:8000/biblioteca/estadisticas/")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      setStats(data);
    })
    .catch((error) =>
      console.error("Error obteniendo estadísticas:", error)
    );
}, []);

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
        <h3>{stats.total_juegos}</h3>
        <p>Juegos en biblioteca</p>
      </div>
    </div>

    <div className="stat-card">
      <div className="stat-icon">🏆</div>
      <div className="stat-info">
        <h3>{stats.total_completados}</h3>
        <p>Completados</p>
      </div>
    </div>
  </div>

  {/* RECIENTES */}
<div className="recent">
  <h2>Juegos Recientes</h2>

  <div className="recent-list">

    {stats?.ultimos_juegos?.length > 0 ? (
      stats.ultimos_juegos.map((juego, index) => (
        <div className="recent-item" key={index}>
          <div className="game-left">

            <img
              className="game-img"
              src={juego.coverUrl}
              alt={juego.nombre}
            />

            <div className="game-text">
              <h4>{juego.nombre}</h4>

              <span>
                {juego.generos?.join(" · ")}
              </span>

            </div>
          </div>
        </div>
      ))
    ) : (
      <p>No hay juegos recientes</p>
    )}

  </div>
</div>

</div>
  );
}

export default Home