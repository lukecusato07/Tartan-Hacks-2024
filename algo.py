import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def train():
    return

def scrape_twitter(ticker):

def pull_data(ticker, source):
    data = ["bad"] * 100 + ["good"] * 800
    if source == "twitter":
        data = scrape_twitter(ticker)
    elif source == "reddit":
        pass
    else:
        data = []

    return data

def get_sentiment(data):
    sid = SentimentIntensityAnalyzer()
    pos = 0
    neg = 0
    result = 0

    for val in data:
        ss = sid.polarity_scores(val)
        if ss['pos'] > .5 or ss['neg'] < .5:
            pos += 1
        else:
            neg += 1

    if pos > neg:
        result = 1

    return result

def analyze(ticker, source):
    data = pull_data(ticker, source)
    final = -1
    if data.size() > 0:
        final =  get_sentiment(data)
    
    return final


print(analyze("aapl",0))