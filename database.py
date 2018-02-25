from pymongo import MongoClient
client = MongoClient()
db = client['twitter-db']
collection = db['tweets']