import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import '../css/library.css';

const Library = () => {

    const [totalGames, setTotalGames] = useState(5);

    const onTotalGames = (e) => {
        setTotalGames(e.target.value);
    }

    return (
        <div>
            <div class="library-header">
                <div class="library-info">
                    <p class="library-title">Mi Biblioteca</p>
                    <p class="library-subtitle">{totalGames} videojuegos en tu colección</p>
                </div>
                <button class="btn-add">Añadir Juego</button>
            </div>
            <div class="filter">
                <div class="search-box">
                    <input type="text" placeholder="Buscar juego..." />
                </div>
                <button class="filter-btn">Filtros</button>
            </div>

            <div class="card-list">

            </div>
        </div>
    )
}

export default Library