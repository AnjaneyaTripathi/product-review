# Scripts\activate
# flask run

from tweets import add_sentiment, convert_df
from flask import Flask, session
import json
from flask_session import Session
from flask import request
from flask import render_template
import pandas as pd
from tweets import QueryTwitter,convert_df,word_cloud,add_sentiment

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"
app.static_folder = 'static'

# session configuraiton -- filesystem interface
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


@app.route('/')
def first_page():
    return render_template('index.html')

@app.route('/tweetRetrieve',methods=['GET','POST'])
def get_tweets():
    if request.method=='POST':
        session['query'] =  request.form['key']
    print("Query=",session.get('query'))
    tweet_list =  QueryTwitter(session.get('query'))
    convert_df(tweet_list)
    return render_template('dashboard.html')

@app.route('/retweets')
def get_retweets():
    tweet_df = pd.read_csv('tweets_df.csv')
    tweet_df = tweet_df.drop(['id','len','likes'],axis=1)
    tweet_df = tweet_df[:10]
    return render_template('retweet.html',  tables=[tweet_df.to_html(classes='data steelBlueCols', header="true")])


@app.route('/sentiment')
def get_sentiment():
    tweet_df = pd.read_csv('tweets_df.csv')
    nlp_list = tweet_df.text.tolist()
    legend = 'Sentiment Analysis'
    stats = add_sentiment(nlp_list)
    labels = ["Negative","Neutral","Positive"]
    return render_template('sentiment.html', values=stats, labels=labels, legend=legend)

@app.route('/wordmap')
def get_wordmap():
    tweet_df = pd.read_csv('tweets_df.csv')
    nlp_list = tweet_df.text.tolist()
    word_cloud(nlp_list)
    return render_template('wordmap.html')