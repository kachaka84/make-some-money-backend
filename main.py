from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("API_FOOTBALL_KEY")
API_URL = "https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2025-04-15"

headers = {
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
    "x-rapidapi-key": API_KEY
}

@app.get("/matches")
def get_matches():
    try:
        response = requests.get(API_URL, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
