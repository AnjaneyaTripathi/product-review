import configuration
import tweepy
import numpy as np
import pandas as pd
import time
import sys

def limit_handled(cursor):
    while True:
        try:
        	#time.sleep(1)
        	yield cursor.next()

        except tweepy.RateLimitError:
            time.sleep(60*15)
            continue

        except StopIteration:
        	break


def QueryTwitter(search_string):
	#Fetching the Configuration Settings
	key = configuration.consumer_key
	secret = configuration.consumer_secret
	access_token = configuration.access_token
	access_secret = configuration.access_secret

	#Authenticating ::
	#Receiving Access Tokens
	auth = tweepy.OAuthHandler(consumer_key=key,consumer_secret=secret)
	auth.set_access_token(access_token, access_secret)

	#Instantiating the API with our Access Token
	api = tweepy.API(auth)

	tweet_list = []
	for tweet in limit_handled(tweepy.Cursor(api.search,q=search_string).items(50)):
		tweet_list.append(tweet.text)

	return tweet_list[0]
