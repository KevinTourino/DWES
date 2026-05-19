import { useNavigate } from "react-router-dom";

const Games = ({ results }) => {

    const navigate = useNavigate();

    return (
        <div className="cards">
            {results.map((game) => (
                <div key={game.id} style={{ marginBottom: "20px" }} onClick={() => navigate(`/game/${game.id}`, {state: { game }})}>
                    <h2>{game.name}</h2>

                    <p>{game.summary}</p>

                    <p>
                        {game.first_release_date
                            ? new Date(game.first_release_date * 1000).toLocaleDateString()
                            : "Unknown"}
                    </p>

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

                    <p>
                        {game.platforms?.map((p) => p.name).join(", ")}
                    </p>
                </div>
            ))}
        </div>
    );
};

export default Games;