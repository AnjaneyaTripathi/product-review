from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
from transformers import AutoModel, BertTokenizerFast
import shutil


def load_model():
    task='sentiment'
    MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
    try:
        shutil.rmtree('./cardiffnlp')
    except:
        print('Working directory is clean.')
    tokenizer = AutoTokenizer.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment', from_tf = True)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained(MODEL)
    return tokenizer, model

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def evaluate(text):
    result = [0,0,0]
    sentiments = []
    tokenizer, model = load_model()
    for i in range(len(text)):
        text[i] = preprocess(text[i])
        encoded_input = tokenizer(text[i], return_tensors='pt')
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        res = np.argmax(scores)
        print(res)
        sentiments.append(res)
        result[res] += 1
        print(scores)
    print(result)
    return result,sentiments

