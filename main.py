from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random
import datetime

app = FastAPI(
    title="Daily Quote API",
    description="A simple API that returns a random motivational/funny quote every day.",
    version="1.0.0",
)

# لیست جملات
QUOTES = [
    "Believe you can and you're halfway there. 💪",
    "Code, eat, sleep, repeat. 😎",
    "Success is not in what you have, but who you are.",
    "Why fix bugs when you can call them 'features'? 🐞✨",
    "Every expert was once a beginner.",
    "The best way to predict the future is to invent it.",
    "Coffee first, then code. ☕💻",
    "Move fast and break things… then git commit -m 'fix' 😂",
]

@app.get("/quote")
async def get_quote():
    today = datetime.date.today().isoformat()
    quote = random.choice(QUOTES)
    return JSONResponse(
        content={
            "date": today,
            "quote": quote,
            "author": "Daily Quote API",
        }
    )

@app.get("/")
async def root():
    return {"message": "Welcome to Daily Quote API 🚀 | Use /quote to get your daily motivation!"}
