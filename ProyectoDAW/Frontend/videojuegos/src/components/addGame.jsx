import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const AddGames = () => {

    const [token, setToken] = useState(null);

    useEffect(() => {
        axios.post(
            "https://id.twitch.tv/oauth2/token",
            null,
            {
                params: {
                client_id: "58tr57drw2hmvl2jdqdwsv0zwqv5m1",
                client_secret: "bt148hr1kd3em4bzgjo3dp26zg7ed9",
                grant_type: "client_credentials",
                },
            }
            ).then(response => {
            setToken(response.data.access_token);
            console.log(response.data.access_token);
            }).catch(error => {
            console.error(error);
        });
    }, []);

    const games = () => {
        console.log("Games")
        axios.post(
        "https://api.igdb.com/v4/games",
        'search "Zelda"; fields name, rating;',
            {
                headers: {
                "Client-ID": "58tr57drw2hmvl2jdqdwsv0zwqv5m1",
                "Authorization": `Bearer ${token}`,
                },
            }
        );
    };

    return (
        <div>
            <button onClick={games}>Juego</button>
        </div>
    )
}

export default AddGames