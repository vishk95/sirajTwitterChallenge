import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Mars')

import csv
with open('twitter.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['Tweet', 'label'])
 
	for tweet in public_tweets: 
		if (TextBlob(tweet.text).sentiment.polarity < 0):
			pol='Negative'

		else:
			pol='Positive'

		filewriter.writerow([tweet.text.encode('utf-8'), pol])
	
