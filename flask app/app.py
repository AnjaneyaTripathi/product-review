# py -3 -m venv tw  
# flask run

from flask import Flask
from flask import request
from flask import render_template
from tweets import QueryTwitter

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
        return QueryTwitter(query)