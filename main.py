from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разреши достъп от Vercel
origins = [
    "https://make-some-money.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/matches")
def get_matches():
    return {
        "fixtures": [
            {
                "home": "Левски",
                "away": "ЦСКА",
                "date": "2025-04-16",
                "time": "18:30",
                "prediction": "Под 2.5 гола"
            },
            {
                "home": "Реал Мадрид",
                "away": "Барселона",
                "date": "2025-04-16",
                "time": "21:00",
                "prediction": "Над 2.5 гола"
            },
            {
                "home": "Байерн",
                "away": "Борусия Дортмунд",
                "date": "2025-04-16",
                "time": "19:45",
                "prediction": "3.5+ гола"
            }
        ]
    }
