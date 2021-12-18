from fastapi import APIRouter
from pydantic import BaseModel
import tekore as tk

class OAuthInitiatedResponse(BaseModel):
    # auth url from spotify to redirect for oauth
    spotify_url:str

router = APIRouter()
conf = tk.config_from_environment()
CREDS = tk.Credentials(*conf)

@router.get('/auth', response_model=OAuthInitiatedResponse)
def initiate_oauth():
    scope = tk.scope.read + tk.scope.write
    auth = tk.UserAuth(CREDS, scope)
    # frontend will receive tokens in callback
    return {'spotify_url':auth.url}