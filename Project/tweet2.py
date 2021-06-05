import configuration
import tweepy
import numpy as np
import pandas as pd
import time
from google_trans_new import google_translator
from os.path import join, dirname, realpath
from wordcloud import WordCloud,STOPWORDS
from bert import evaluate
import matplotlib.pyplot as plt

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
    tweet_text = []
    for tweet in limit_handler(tweepy.Cursor(api.search,q=search_string).items(10)):
        tweet_list.append(tweet)

    newlist = sorted(tweet_list,key=lambda x: x.retweet_count, reverse=True)
    translator = google_translator() 
    for i in range(len(newlist)):
        newlist[i].text = translator.translate(newlist[i].text,lang_tgt='en')
        tweet_text.append(newlist[i].text)  #* For NLP
    return newlist,tweet_text                 #* 10 Most retweets


def convert_df(tweet_list):
    id_list = [tweet.id for tweet in tweet_list]
    tweet_df = pd.DataFrame(id_list,columns=['id'])
    tweet_df["text"] = [tweet.text for tweet in tweet_list]
    tweet_df["retweet_count"]= [tweet.retweet_count for tweet in tweet_list]
    tweet_df["date"]= [tweet.created_at for tweet in tweet_list]
    tweet_df["source"]= [tweet.source for tweet in tweet_list]
    tweet_df["len"]= [len(tweet.text) for tweet in tweet_list]
    tweet_df["likes"]= [tweet.favorite_count for tweet in tweet_list]
    tweet_df["location"]= [tweet.author.location for tweet in tweet_list]
    return tweet_df

def freq_words(str):
    str = str.split()		
    str2 = []
    for i in str:
        if i not in str2:
            str2.append(i)
    return str2

def word_cloud(list):   ##! Problem
    val = ''
    for x in list:
        val += (x)
    stopwords = set(STOPWORDS)
    comment_words = ''
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens)+" "
    s = freq_words(comment_words)
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate(comment_words)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()
    wordcloud.to_file('cloud.png')


def add_sentiment(tweets):
    '''
    index 0: negative
    index 1: neutral
    index 2: positive
    find the max value and the corresponing index indicates the sentimant
    '''
    stats = evaluate(tweets)
    return stats

def geolocation(tweet_df):
    pass