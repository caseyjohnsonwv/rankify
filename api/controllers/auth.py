from fastapi import APIRouter, Depends
import tekore as tk

def get_user_auth_instance(state=None):
    scope = tk.scope.read + tk.scope.write
    creds = tk.Credentials(*tk.config_from_environment())
    auth = tk.UserAuth(creds, scope)
    if state:
        auth.state = state
    return auth

router = APIRouter()

@router.get('/auth')
def initiate_oauth():
    # get redirect url for oauth - frontend stores state in session
    auth = get_user_auth_instance()
    return {'spotify_url':auth.url, 'state':auth.state}

@router.get('/auth/callback')
def complete_oauth(code:str, state:str):
    # complete oauth with spotify code + state from user session
    auth = get_user_auth_instance(state)
    token = auth.request_token(code, state)
    return {'token':token}
