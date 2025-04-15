from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаваме заявки от всякакви домейни (може да ограничим само до Vercel ако искаш)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # или ["https://make-some-money.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/matches")
def get_matches():
    return {
        "fixtures": [
            { "home": "Левски", "away": "ЦСКА", "date": "2025-04-16" },
            { "home": "Реал Мадрид", "away": "Барселона", "date": "2025-04-16" },
            { "home": "Байерн", "away": "Борусия Дортмунд", "date": "2025-04-16" },
        ]
    }
