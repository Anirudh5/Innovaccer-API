from tweepy import StreamListener, OAuthHandler, Stream

CONSUMER_KEY='Your key here'
CONSUMER_SECRET='Your key here'
ACCESS_TOKEN_KEY='Your key here'
ACCESS_TOKEN_SECRET='Your key here'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
