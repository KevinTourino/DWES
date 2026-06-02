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
    const [loading, setLoading] = useState(false);

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

        setLoading(true);

        if (oldGame[name]) {
            setResults(oldGame[name]);
            setLoading(false);
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
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <div className="search-container">
                <form className="search-form" onSubmit={handleSubmit}>
                    <div className="search-group">
                        <input
                            id="gameName"
                            type="text"
                            value={gameName}
                            onChange={(e) => setGameName(e.target.value)}
                            placeholder="Buscar juego"
                            className="search-input"
                        />
                    </div>

                    <button type="submit" className="search-btn">
                    Juego
                    </button>
                </form>
            </div>
            <div className="card">
                {loading ? (
                    <p className="informacion">Procesando petición...</p>
                ) : results.length > 0 ? (
                    <Games results={results} />
                ) : (
                    <p className="informacion">No hay resultados aún</p>
                )}
            </div>
            
        </div>
    )
}

export default AddGames