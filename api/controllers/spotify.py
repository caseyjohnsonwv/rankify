from fastapi import APIRouter, HTTPException
import tekore as tk
from time import time

router = APIRouter()

class MEDIATYPES:
    ARTIST = 'artist'
    ALBUM = 'album'
    TRACK = 'track'

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

@router.post('/spotify/import')
def importMedia(token:dict, type:str, query:str):
    # allow users to import individual tracks or entire albums
    if type not in [MEDIATYPES.ALBUM, MEDIATYPES.TRACK]:
        raise HTTPException(status_code=403, detail="Must import by album or track")
    client = tk.Spotify(build_token(token))
    results = client.search(query, types=(type,), limit=1)
    resource = results[0] if len(results) > 0 else None
    if resource is None:
        raise HTTPException(status_code=404, detail="Media not found")
    media_id = resource.items[0].id
    if type == MEDIATYPES.ALBUM:
        tracks = client.album_tracks(media_id).items
        import_data = [{'uri':track.uri, 'name':track.name, 'preview_url':track.preview_url} for track in tracks]
        return {'resource':import_data}
    elif type == MEDIATYPES.TRACK:
        raise HTTPException(status_code=501, detail="Track import not yet implemented")
