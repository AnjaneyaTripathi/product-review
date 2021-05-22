import configuration
import tweepy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time
import sys
import os
from os.path import join, dirname, realpath
from wordcloud import WordCloud,STOPWORDS

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(60*15)
            continue
        except StopIteration:
            break

def QueryTwitter(search_string):
    key = configuration.consumer_key
    secret = configuration.consumer_secret
    access_token = configuration.access_token
    access_secret = configuration.access_secret

    auth = tweepy.OAuthHandler(consumer_key=key,consumer_secret=secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True)

    tweet_list = []
    for tweet in limit_handler(tweepy.Cursor(api.search,q=search_string).items(10)):
        tweet_list.append(tweet)
    return tweet_list

def convert_df(tweet_list):
    id_list = [tweet.id for tweet in tweet_list]
    tweet_df = pd.DataFrame(id_list,columns=['id'])
    tweet_df["text"] = [tweet.text for tweet in tweet_list]
    tweet_df["retweet_count"]= [tweet.retweet_count for tweet in tweet_list]
    return tweet_df

def word_cloud(tweet_df):   ##! Problem
    stopwords = set(STOPWORDS)
    words =' '.join([text for text in tweet_df.text]) 
    wordcloud = WordCloud(stopwords=stopwords, background_color="white")
    wordcloud.generate(words)
    path = "C:\\Users\\ADMIN\\Desktop\\Swetha\\Academics\\NLP project\\tw\\static\\wordcloud.jpg"
    wordcloud.to_file(path)
    plt.imsave(path,wordcloud)
    return path

def data_preprocess():
    ##* Remove emojis,special char etc.
    pass

def add_sentiment():
    pass

def create_maps(tweet_df): ##* Pass the processed df with the sentiments
    ## TODO: Top 10 tweets
    ## TODO: Date Vs Sentiment
    ## TODO: Overall sentiment
    ## TODO: Geo Location
    pass
