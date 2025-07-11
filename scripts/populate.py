from db import DBHandler
from utils import convert_ids
import json
db = DBHandler()


def populate_victims_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for idx,victim in enumerate(data):
            db.add_victim(
                name=victim["name"],
                age=victim["age"],
                date=victim["date"],
                city=victim['city'],
                province=victim['province'],
                description=victim["description"]
            )
            print(f"Added victim {idx + 1}: {victim['name']}")
    print("Database populated with victims from JSON file.")
    
    
def populate_memos_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for idx,memo in enumerate(data):
            db.add_memo(
                name=memo["name"],
                age=memo["age"],
                date=memo["date"],
                city=memo['city'],
                province=memo['province'],
                description=memo["description"],
                image=memo["image"],
                memorial=memo["memorialText"]
            )
            print(f"Added memo {idx + 1}: {memo['name']}")
    print("Database populated with memos from JSON file.")
    
    
populate_memos_from_json("data/memo.json")