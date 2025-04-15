from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def predict_result(home, away):
    home = home.lower()
    away = away.lower()
    if "реал" in home or "байерн" in home:
        return "1"
    elif "цска" in away or "барселона" in away:
        return "2"
    else:
        return "X"

@app.get("/matches")
def get_matches():
    matches = [
        {"home": "Левски", "away": "ЦСКА", "date": "2025-04-16"},
        {"home": "Реал Мадрид", "away": "Барселона", "date": "2025-04-16"},
        {"home": "Байерн", "away": "Борусия Дортмунд", "date": "2025-04-16"},
        {"home": "Лудогорец", "away": "Берое", "date": "2025-04-16"}
    ]
    for match in matches:
        match["prediction"] = predict_result(match["home"], match["away"])
    return matches
