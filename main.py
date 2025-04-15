from fastapi import FastAPI

app = FastAPI()

@app.get("/matches")
def get_matches():
    return {
        "fixtures": [
            {"home": "Левски", "away": "ЦСКА", "date": "2025-04-16"},
            {"home": "Реал Мадрид", "away": "Барселона", "date": "2025-04-16"},
            {"home": "Байерн", "away": "Борусия Дортмунд", "date": "2025-04-16"}
        ]
    }
