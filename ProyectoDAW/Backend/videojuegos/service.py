import requests

TWITCH_CLIENT_ID = "z6df31rwkpqbup1pkxwoy140hpyqnf"
TWITCH_SECRET = "n5xlyk7m6ie5urju64dwv1t00vb784"


def get_twitch_token():
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": TWITCH_CLIENT_ID,
        "client_secret": TWITCH_SECRET,
        "grant_type": "client_credentials"
    }
    r = requests.post(url, params=params)
    return r.json()["access_token"]


def fetch_igdb_games(game_name):
    token = get_twitch_token()

    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }

    query = f'''
    fields name, rating, summary, first_release_date, cover.url, genres.name, platforms.name;
    search "{game_name}";
    limit 12;
    '''
    r = requests.post(url, headers=headers, data=query)
    return r.json()

def fetch_igdb_games_id(id):
    token = get_twitch_token()

    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }

    query = f'''
    fields name, rating, summary, first_release_date, cover.url, genres.name, platforms.name;
    where id = {id};
    limit 1;
    '''

    r = requests.post(url, headers=headers, data=query)
    return r.json()