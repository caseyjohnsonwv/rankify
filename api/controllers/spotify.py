from fastapi import APIRouter
import tekore as tk
from time import time

router = APIRouter()

def build_token(token):
    token = token.get('token', token)
    _token = {
        'access_token' : token['_access_token'],
        'token_type' : token['_token_type'],
        'expires_in' : token['_expires_at'] - int(time()),
        'refresh_token' : token['_refresh_token'],
    }
    creds = tk.Credentials(*tk.config_from_environment())
    return tk.Token(_token, creds)

@router.post('/spotify/search')
def searchSpotify(token:dict, query:str):
    client = tk.Spotify(build_token(token))
    results = client.search(query)
    return {'results':results}

@router.post('/spotify/song/sample')
def getSongSample():
    pass

@router.post('/spotify/song/import')
def importSong():
    pass

@router.post('/spotify/album/import')
def importAlbum():
    pass

@router.post('/spotify/playlist/import')
def importPlaylist():
    pass

@router.post('/spotify/playlist/export')
def exportPlaylist():
    pass
