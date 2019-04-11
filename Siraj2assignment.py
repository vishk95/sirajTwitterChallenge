import tweepy
from textblob import TextBlob

consumer_key = 'vLAzTkrQD6OiY3o2ZLE7nkzrA'
consumer_secret = 'UWkNBN7m0S95MShyUX36ekeDasUGGwZSzoHOVrP94PcBK3IJBu'

access_token = '448924543-N32fjI9BMaSyJ9xUARk02dAnWaE5wjuGgbWhkzXK'
access_token_secret = 'GlGnQAwWh5WIpYO3KBkPsPwdRk1uDC240zJoQ6UUf9IJ9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Black hole')

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
	