import tweepy
from textblob import TextBlob

consumer_key = '1mH1dGHI5OHQZFJEYRncFSWNP'
consumer_secret = 'GZEu1pR6UvSuuW2sO6JyBaegbTPPkeXMGiEFfZNLqVuUaL70le'

access_token = '3104899826-IsgnoKKElfaJbEIhtUZ8hPbfmuUAsu0A35XP5EW'
acces_token_secret = '05N6fDHfWecIdXj8DRrEsGT1fHzr9o1b0lA7W96gs5ALs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

