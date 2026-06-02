import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import '../css/library.css';

const Library = () => {
    const navigate = useNavigate();

    const [totalGames, setTotalGames] = useState(0);
    const [games, setGames] = useState([]);
    const [search, setSearch] = useState("");

    const onTotalGames = (e) => {
        setTotalGames(e.target.value);
    }

    const handleAddGame = () => {
        navigate("/addGame");
    };

    useEffect(() => {
        const token = sessionStorage.getItem("access");

        fetch("http://localhost:8000/biblioteca/juegos/", {
            headers: {
            Authorization: `Bearer ${token}`
            }
        })
            .then(res => res.json())
            .then(data => {
            setGames(data);
            console.log(data)
            setTotalGames(data.length);
        });
        }, []);


        const filteredGames = games.filter((game) =>
            game.titulo.toLowerCase().includes(search.toLowerCase())
        );

    return (
        <div>
            <div className="library-header">
                <div className="library-info">
                    <p className="library-title">Mi Biblioteca</p>
                    <p className="library-subtitle">{totalGames} videojuegos en tu colección</p>
                </div>
                <button className="btn-add" onClick={handleAddGame}>Añadir Juego</button>
            </div>
            <div className="filter">
                <div className="search-box">
                    <input
                        type="text"
                        placeholder="Buscar juego..."
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                    />
                </div>
                <button className="filter-btn">Filtros</button>
            </div>

            <div className="card-list">
    {totalGames === 0 ? (
        <div className="sin-juegos">
    <div className="sin-juegos-icon">🎮</div>

    <h2>Tu biblioteca está vacía</h2>

    <p>
        Aún no has añadido ningún juego a tu colección
    </p>

    <button onClick={handleAddGame}>
        Añadir primer juego
    </button>
</div>
    ) : (
        filteredGames.map((game) => (
            <div
                key={game.id || game.titulo}
                style={{ marginBottom: "20px", cursor: "pointer" }}
                onClick={() => navigate(`/game/${game.id}`)}
            >
                <h2>{game.titulo}</h2>

                {game.imagen && (
                    <img
                        src={game.imagen}
                        alt={game.titulo}
                        width="250"
                    />
                )}

                <p>
                    {game.generos?.join(", ")}
                </p>
            </div>
        ))
    )}
</div>
        </div>
    )
}

export default Library