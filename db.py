
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
    
    
class DBHandler:
    def __init__(self):
        load_dotenv()
        self.client = MongoClient(os.environ["URI"], server_api=ServerApi('1'))
        
        try:
            self.client.admin.command('ping')
            print("Successfully connected to MongoDB!")
        except Exception as e:
            print("Failed to connect to MongoDB.")
            raise e
        self.db = self.client[os.environ["DB_NAME"]]
        self.collection_victims = self.db["victims"]
        self.collection_memos = self.db["memos"]
    
    
    def add_victim(self, name,age,date,city,province,description):
        self.collection_victims.insert_one({
            "name": name,
            "age": age,
            "date": date,
            "city": city,
            "province": province,
            "description": description
        })
        
    def add_memo(self,name,age,date,city,province,description,image,memorial):
        self.collection_memos.insert_one({
            "name": name,
            "age": age,
            "date": date,
            "city": city,
            "province": province,
            "description": description,
            "image": image,
            "memorial": memorial
        })
        
        
    def get_victims(self):
        return list(self.collection_victims.find({}))
    def get_memos(self):
        return list(self.collection_memos.find({}))
    

    def close(self):
        self.client.close()