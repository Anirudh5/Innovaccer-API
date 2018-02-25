from database import *
import json
from pprint import pprint

def FilterTweet(username=".*", retweetCount=0, favCount=0, language=".*", retweetCountOperator='$gte', favCountOperator='$gte', timestamp="0", timestampOperator='$gte'):
	data = collection.find({"$and": [{"user.screen_name": {"$regex": username}}, {"lang": {"$regex": language}}, {"retweet_count": {retweetCountOperator: retweetCount}}, 
		{"favorite_count": {favCountOperator: favCount}}, {"timestamp_ms": {timestampOperator: timestamp}}]})
	#for document in data:
	#	pprint(document)
	#print data.count()
	return data
	
FilterTweet(username="^p")