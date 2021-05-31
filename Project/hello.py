# Scripts\activate 
# flask run

from tweets import add_sentiment, convert_df
from flask import Flask
from flask import request
from flask import render_template
from tweets import QueryTwitter,convert_df,word_cloud,add_sentiment

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"
app.static_folder = 'static'

@app.route('/')
def first_page():
    return render_template('index.html')


@app.route('/tweetRetrieve',methods=['GET','POST'])
def get_tweets():
    if request.method=='POST':
        query = request.form['key']
        tweet_list,nlp_list =  QueryTwitter(query)
        tweet_df = convert_df(tweet_list)
        tweet_df = tweet_df.drop(['id','len','likes'],axis=1)
        stats = add_sentiment(nlp_list)
    #return render_template('dashboard.html',  tables=[tweet_df.to_html(classes='data steelBlueCols', header="true")])
    #path = word_cloud(tweet_df)
    return stats