import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";

import "../css/GameDetail.css";

const GameDetail = () => {
    const { id } = useParams();

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
        return <p className="loading">Cargando...</p>;
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

    const handleOwnedChange = (index) => {

    setSelectedPlatforms(
        selectedPlatforms.map((platform, i) =>
            i === index
                ? { ...platform, owned: !platform.owned }
                : platform
        )
    );
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

        await axios.post(
            "http://localhost:8000/biblioteca/add/",
            {
                videojuego_id: game.id
            },
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        );

        alert("Juego añadido a la biblioteca");

    } catch (error) {
        console.error(error);
    }
};

    return (
        <div className="gameDetailContainer">
            <button onClick={saveGameToLibrary}>
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

            <label>
                En Posesión

                <input
                    type="checkbox"
                    checked={platform.owned}
                    onChange={() => handleOwnedChange(index)}
                />
            </label>

            <select
                value={platform.status}
                onChange={(e) =>
                    handleStatusChange(index, e.target.value)
                }
            >
                <option value="jugando">
                    Jugando
                </option>

                <option value="abandonado">
                    Abandonado
                </option>

                <option value="espera">
                    En espera
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