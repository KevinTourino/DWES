import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import "../css/GameDetail.css";

const GameLibrary = () => {
    const { id } = useParams();
    const navigate = useNavigate();

    const [game, setGame] = useState(null);

    useEffect(() => {
        const fetchGame = async () => {
            try {
                const token = sessionStorage.getItem("access");

                const res = await axios.get(
                    `http://localhost:8000/videojuegos/${id}/`,
                    {
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    }
                );

                setGame(res.data);

            } catch (error) {
                console.error("Error fetching game:", error);
            }
        };

        fetchGame();
    }, [id]);

    if (!game) {
        return (
            <div className="cargando">
                <p className="loading">Cargando...</p>
            </div>
        );
    }

    return (
        <div className="gameDetailContainer">

            <div className="gameDetailCard">

                {/* TITLE */}
                <h1 className="gameTitle">
                    {game.nombre}
                </h1>

                {/* MAIN */}
                <div className="gameMain">

                    {/* LEFT */}
                    <div className="gameLeft">

                        {game.coverUrl && (
                            <img
                                className="gameCover"
                                src={game.coverUrl}
                                alt={game.nombre}
                            />
                        )}

                    </div>

                    {/* RIGHT */}
                    <div className="gameRight">

                        <p className="gameSummary">
                            {game.descripcion || "Sin descripción disponible"}
                        </p>

                        <div className="gameInfoGrid">

                            <div className="infoBox">
                                <span>🎮 Géneros</span>
                                <p>
                                    {game.generos?.join(", ") || "N/A"}
                                </p>
                            </div>

                            <div className="infoBox">
                                <span>🕹 Plataforma</span>
                                <p>
                                    {game.plataforma || "N/A"}
                                </p>
                            </div>

                            <div className="infoBox">
                                <span>📌 Estado</span>
                                <p>
                                    {game.estado || "N/A"}
                                </p>
                            </div>

                        </div>

                    </div>
                </div>

                {/* FECHA */}
                <div className="infoBox">
                    <span>📅 Añadido</span>
                    <p>
                        {game.fecha_agregado
                            ? new Date(game.fecha_agregado).toLocaleDateString()
                            : "N/A"}
                    </p>
                </div>

                {/* BOTÓN */}
                <button
                    className="backButton"
                    onClick={() => navigate("/library")}
                >
                    Volver a la biblioteca
                </button>

            </div>
        </div>
    );
};

export default GameLibrary;