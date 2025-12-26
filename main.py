from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from livekit import api
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://sad790.github.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/token")
def get_token(
    user_id: str = Query(...),   # 👈 unique per user
):
    room_name = f"aanya-room-{user_id}"

    token = (
        api.AccessToken(
            os.environ["LIVEKIT_API_KEY"],
            os.environ["LIVEKIT_API_SECRET"],
        )
        .with_identity(user_id)     # 👈 unique identity
        .with_grants(
            api.VideoGrants(
                room_join=True,
                room=room_name
            )
        )
        .to_jwt()
    )

    return {
        "token": token,
        "url": os.environ["LIVEKIT_URL"],
        "room": room_name
    }
