import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";

import "../css/GameDetail.css";

const GameDetail = () => {
    const { id } = useParams();

    const [game, setGame] = useState(null);

    useEffect(() => {
        const fetchGame = async () => {
            try {
                const res = await axios.get(
                    `http://localhost:8000/games/${id}/`
                );

                setGame(res.data[0]);
            } catch (error) {
                console.error("Error fetching game:", error);
            }
        };

        fetchGame();
    }, [id]);

    if (!game) {
        return <p className="loading">Cargando...</p>;
    }

    return (
        <div className="gameDetailContainer">

            <div className="gameDetailCard">

                {/* TITLE */}
                <h1 className="gameTitle">
                    {game.name}
                </h1>

                {/* MAIN CONTENT */}
                <div className="gameMain">

                    {/* LEFT */}
                    <div className="gameLeft">

                        {game.cover?.url && (
                            <img
                                className="gameCover"
                                src={`https:${game.cover.url.replace(
                                    "t_thumb",
                                    "t_cover_big"
                                )}`}
                                alt={game.name}
                            />
                        )}

                    </div>

                    {/* RIGHT */}
                    <div className="gameRight">

                        {/* DESCRIPTION */}
                        <p className="gameSummary">
                            {game.summary || "Sin descripción disponible"}
                        </p>

                        {/* INFO ROW */}
                        <div className="gameInfoGrid">

                            {/* RATING */}
                            <div className="infoBox">
                                <span>⭐ Rating</span>

                                <p>
                                    {game.rating
                                        ? game.rating.toFixed(1)
                                        : "N/A"}
                                </p>
                            </div>

                            {/* RELEASE DATE */}
                            <div className="infoBox">
                                <span>📅 Lanzamiento</span>

                                <p>
                                    {game.first_release_date
                                        ? new Date(
                                            game.first_release_date * 1000
                                        ).toLocaleDateString()
                                        : "Desconocido"}
                                </p>
                            </div>

                            {/* GENRES */}
                            <div className="infoBox">
                                <span>🎮 Géneros</span>

                                <p>
                                    {game.genres?.map(g => g.name).join(", ") || "N/A"}
                                </p>
                            </div>

                        </div>

                    </div>

                </div>
                {/* PLATFORMS */}
<div className="platformSection">

    <div className="infoBox">
        <span>Añade las plataformas en las que los tengas</span>

        <div className="platformTags">

            {game.platforms?.map((platform, index) => (
        <button
            key={index}
            className="platformTag"
        >
            {platform.name}
        </button>
    ))}

        </div>
    </div>

</div>

            </div>

        </div>
    );
};

export default GameDetail;