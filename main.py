from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("API_FOOTBALL_KEY")
API_URL = "https://v3.football.api-sports.io/fixtures?date=2025-04-15"

headers = {
    "x-apisports-key": API_KEY
}

@app.get("/matches")
def get_matches():
    response = requests.get(API_URL, headers=headers)
    return response.json()
