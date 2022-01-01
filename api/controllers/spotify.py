from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import tekore as tk
from time import time
from typing import List, Dict

router = APIRouter()

class MEDIATYPES:
    ARTIST = 'artist'
    ALBUM = 'album'
    TRACK = 'track'

class ImportResponse(BaseModel):
    artist: str
    album: str
    tracks: List[Dict]
    image_url: str

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

@router.post('/spotify/import', response_model=ImportResponse)
def importMedia(token:dict, type:str, query:str):
    # allow users to import individual tracks or entire albums
    client = tk.Spotify(build_token(token))
    results = client.search(query, types=(type,), limit=1)
    resource = results[0] if len(results) > 0 else None
    if resource is None:
        raise HTTPException(status_code=404, detail=f"Media not found for search query {query}")
    media = resource.items[0]
    if type == MEDIATYPES.ALBUM:
        artist = media.artists[0].name
        album_name = media.name
        image_url = media.images[0].url
        tracks = client.album_tracks(media.id).items
        track_data = [{'uri':track.uri, 'name':track.name, 'preview_url':track.preview_url} for track in tracks]
        return {'artist':artist, 'album':album_name, 'tracks':track_data, 'image_url':image_url}
    elif type == MEDIATYPES.TRACK:
        artist = media.artists[0].name
        album_name = media.album.name
        image_url = media.album.images[0].url
        track_data = [{'uri':media.uri, 'name':media.name, 'preview_url':media.preview_url}]
        return {'artist':artist, 'album':album_name, 'tracks':track_data, 'image_url':image_url}
    else:
        raise HTTPException(status_code=403, detail=f"Must import by album or track - you tried {type}")
