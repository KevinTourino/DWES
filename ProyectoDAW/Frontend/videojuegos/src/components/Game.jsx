import { useNavigate } from "react-router-dom";

const Games = ({ results }) => {

    const navigate = useNavigate();

    return (
        <div className="cards">
            {results.map((game) => (
                <div key={game.id} style={{ marginBottom: "20px" }} onClick={() => navigate(`/game/${game.id}`)}>
                    <h2>{game.name}</h2>
                    {game.cover && (
                        <img
    src={`https:${game.cover.url.replace("t_thumb", "t_cover_big")}`}
    alt={game.name}
    width="250"
  />
                    )}
                    <p>
                        {game.genres?.map((g) => g.name).join(", ")}
                    </p>
                </div>
            ))}
        </div>
    );
};

export default Games;