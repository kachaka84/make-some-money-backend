from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("API_FOOTBALL_KEY")
API_URL = "https://google.com"

headers = {}

@app.get("/matches")
def get_matches():
    try:
        response = requests.get(API_URL, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
