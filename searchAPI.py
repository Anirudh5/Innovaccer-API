from twitterAuth import *
from database import *
import json

class MyListener(StreamListener):
	def on_data(self, data):
		result = collection.insert_one(json.loads(data))
		return True

	def on_error(self, status):
		print "error"
		print status

def Search(title):
	l = MyListener()
	stream = Stream(auth, l)
	stream.filter(track=[title])

#Following is just a test case
#Search("modi")
