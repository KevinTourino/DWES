import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Games from "./Game";
import axios from "axios";

const AddGames = () => {

    const [gameName, setGameName] = useState("");
    const [oldGame, setOldGame] = useState({});
    const [results, setResults] = useState([]);

    const handleSubmit = async (e) => {
         e.preventDefault();

        const name = gameName.trim();

        if (name.length === 0) {
            setResults([]);
            return;
        }

        if (oldGame[name]) {
            setResults(oldGame[name]);
            return;
        }

        try {
            const res = await axios.get(
                `http://localhost:8000/games/?name=${name}`
            );

            setResults(res.data);

            setOldGame((prev) => ({
                ...prev,
                [name]: res.data
            }));

        } catch (error) {
            console.error("Error fetching games:", error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" value={gameName} onChange={(e) => setGameName(e.target.value)} placeholder="Buscar juego" />
                <button type="submit">Juego</button>
            </form>

            {results.length > 0 ? 
                (<Games results={results} />) 
                : 
                (<p>No hay resultados aún</p>)
            }
        </div>
    )
}

export default AddGames