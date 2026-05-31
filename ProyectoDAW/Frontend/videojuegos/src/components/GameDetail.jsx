import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import "../css/GameDetail.css";

const GameDetail = () => {
    const { id } = useParams();

    const navigate = useNavigate();

    const [game, setGame] = useState(null);

    const [selectedPlatforms, setSelectedPlatforms] = useState([]);

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
        return <div className="cargando">
                    <p className="loading">Cargando...</p>
                </div>
    }

    const addPlatform = (platform) => {

    const exists = selectedPlatforms.find(
        (p) => p.name === platform.name
    );

    if (exists) return;

    setSelectedPlatforms((prev) => [
        ...prev,
        {
            name: platform.name,
            owned: false,
            status: "jugando",
        },
    ]);
};


const handleStatusChange = (index, value) => {

    setSelectedPlatforms(
        selectedPlatforms.map((platform, i) =>
            i === index
                ? { ...platform, status: value }
                : platform
        )
    );
};



const saveGameToLibrary = async () => {
    try {
        const token = sessionStorage.getItem("access");

        // Construir objeto plataformas
        const plataformas = selectedPlatforms.reduce((acc, p) => {
            acc[p.name] = p.status;
            return acc;
        }, {});

        // Construir payload final
        const payload = {
            videojuego: {
                nombre: game.name,
                anio_lanzamiento: game.first_release_date
                    ? new Date(game.first_release_date * 1000)
                        .toISOString()
                        .split("T")[0]
                    : null,
                descripcion: game.summary || "",
                coverUrl: game.cover?.url
                    ? `https:${game.cover.url.replace("t_thumb", "t_cover_big")}`
                    : null,
                generos: game.genres?.map(g => g.name) || []
            },
            plataformas: plataformas
        };

        await axios.post(
            "http://localhost:8000/addGame/",
            payload,
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                }
            }
        );

        alert("Juego añadido a la biblioteca");
        navigate("/library");

    } catch (error) {
        console.error("Error guardando juego:", error);
        alert("Error al añadir juego a la biblioteca");
    }
};

const removePlatform = (index) => {
    setSelectedPlatforms((prev) =>
        prev.filter((_, i) => i !== index)
    );
};

    return (
        <div className="gameDetailContainer">
            <button class="addLibraryButton" onClick={saveGameToLibrary}>
    Añadir a biblioteca
</button>

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

<div className="platformSection">

    <div className="infoBox">
        <span>Añade las plataformas en las que los tengas</span>

        <div className="platformTags">

    {game.platforms?.map((platform, index) => (
        <button
            key={index}
            className="platformTag"
            onClick={() => addPlatform(platform)}
        >
            {platform.name}
        </button>
    ))}

</div>
    </div>

</div>
<div className="platform-list">

    {selectedPlatforms.map((platform, index) => (

        <div
            key={index}
            className="platform-item"
        >

            <h3>{platform.name}</h3>

            <button
                className="removeButton"
                onClick={() => removePlatform(index)}
            >
                Eliminar
            </button>

            <select
                value={platform.status}
                onChange={(e) =>
                    handleStatusChange(index, e.target.value)
                }
            >
                <option value="jugando">
                    Jugando
                </option>

                <option value="pendiente">
                    Pendiente
                </option>

                <option value="abandonado">
                    Abandonado
                </option>

                <option value="completado">
                    Completado
                </option>
            </select>

        </div>

    ))}

</div>
            </div>

        </div>
    );
};

export default GameDetail;