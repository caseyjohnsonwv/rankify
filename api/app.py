import uvicorn, env
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import auth, spotify

app = FastAPI()
app.include_router(auth.router)
app.include_router(spotify.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host=env.API_HOST,
        port=int(env.API_PORT),
        reload=True if env.API_HOST == 'localhost' else False,
    )
