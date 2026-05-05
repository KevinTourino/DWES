const Games = ({ results }) => {
    return (
        <div>
            {results.map((game) => (
                <div key={game.id} style={{ marginBottom: "20px" }}>
                    <h2>{game.name}</h2>

                    <p>{game.summary}</p>

                    <p>
                        {game.first_release_date
                            ? new Date(game.first_release_date * 1000).toLocaleDateString()
                            : "Unknown"}
                    </p>

                    {game.cover && (
                        <img
                            src={game.cover.url}
                            alt={game.name}
                            width="150"
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