import { useLocation } from "react-router-dom";

const GameDetail = () => {

    const location = useLocation();
    const game = location.state?.game;

    return (
        <div>
            <h1>{game.name}</h1>
            <p>{game.summary}</p>
            {game.cover && (
    <img
        src={`https:${game.cover.url.replace("t_thumb", "t_cover_big")}`}
        alt={game.name}
        width="250"
    />
)}

        </div>
    );
};

export default GameDetail;