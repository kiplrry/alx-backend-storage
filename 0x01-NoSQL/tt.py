from pymongo import MongoClient

client = MongoClient()
db = client.logs
logs = db.nginx