from fastapi import FastAPI
from livekit import api
import os

app = FastAPI()

@app.get("/token")
def get_token():
    token = api.AccessToken(
        os.environ["LIVEKIT_API_KEY"],
        os.environ["LIVEKIT_API_SECRET"]
    ).with_identity("orb-ui").with_grants(
        api.VideoGrants(
            room_join=True,
            room="aanya-room"
        )
    ).to_jwt()

    return {
        "token": token,
        "url": os.environ["LIVEKIT_URL"]
    }
