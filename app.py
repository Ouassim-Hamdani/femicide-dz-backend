from fastapi import FastAPI
from db import DBHandler
from utils import convert_ids
# Startup code
app = FastAPI()

db = DBHandler()



@app.get("/")
async def health_check():
    return {"status": "ok"}


@app.get("/victims")
async def get_victims():
    victims = db.get_victims()
    return convert_ids(victims)


@app.get("/memos")
async def get_memos():
    memos = db.get_memos()
    return convert_ids(memos)


@app.get("/year")
async def get_year():
    return {"year": 2025}