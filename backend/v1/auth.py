from fastapi import APIRouter
import requests
import os

from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/v1",
)

@router.get("/auth")
def get_access_token():
    data = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
    }

    response = requests.post('https://api.intra.42.fr/oauth/token', data=data)
    return response.json()["access_token"]

@router.get("/auth/callback")
def get_callback():
    return {"message": "Hello World"}