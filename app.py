from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import DBHandler
from utils import convert_ids
# Startup code
app = FastAPI()

db = DBHandler()

origins = [
    "http://localhost:3000",
    "https://femicide.net", 
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies to be sent with cross-origin requests
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],     # Allow all headers in the request
)




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