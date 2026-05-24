import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Navigate } from "react-router-dom"
import '../css/cards.css'
import Games from "./Game";
import axios from "axios";

const AddGames = () => {

    const [gameName, setGameName] = useState("");
    const [oldGame, setOldGame] = useState({});
    const [results, setResults] = useState([]);

    const navigate = useNavigate()

    useEffect(() => {
        const token = sessionStorage.getItem("access")

        if (!token) {
            navigate("/login")
        }
    }, [navigate])

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
            <div className="card-list">
                {results.length > 0 ? 
                    (<Games results={results} />) 
                    : 
                    (<p>No hay resultados aún</p>)
                }
            </div>
            
        </div>
    )
}

export default AddGames