from dotenv import load_dotenv
load_dotenv()

from os import getenv
API_HOST = getenv('API_HOST') or "localhost"
API_PORT = getenv('API_PORT') or "5000"
UI_HOST = getenv("UI_HOST") or "http://localhost:8080"
SPOTIFY_CLIENT_ID = getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = getenv('SPOTIFY_REDIRECT_URI')