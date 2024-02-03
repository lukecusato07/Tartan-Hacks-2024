'''<script async src="https://cse.google.com/cse.js?cx=e3bff4e8fad4e4527">
</script>
<div class="gcse-search"></div>
'''

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from requests import get
from lxml.html import fromstring
import cssselect
from urllib.parse import urlencode, urlparse, parse_qs
from googleapiclient.discovery import build




def train():
    return

def scrape_google(ticker):
    titles = []
    service = build("customsearch", "v1", developerKey="AIzaSyB-_9fmxeuHTgwLFDqNeC5dMqoNYUpgrqg")
    res = service.cse().list(q=ticker, cx="e3bff4e8fad4e4527", num=10).execute()
    results = res['items']
    for result in results:
        titles.append(result['title'])
    return titles

def pull_data(ticker, source):
    data = ["bad"] * 100 + ["good"] * 800
    if source == "google":
        query = ticker + "+ stock"
        data = scrape_google(query)
    elif source == "reddit":
        pass
    else:
        data = []

    return data

def get_sentiment(data):
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    pos = 0
    neg = 0
    result = 0

    for val in data:
        ss = sid.polarity_scores(val)
        if(ss['neu'] > .5):
            pass
        elif ss['pos'] > .5 or ss['neg'] < .5:
            pos += 1
        else:
            neg += 1

    if pos > neg:
        result = 1

    return result

def analyze(ticker, source):
    data = pull_data(ticker, source)
    final = -1
    if len(data) > 0:
        final =  get_sentiment(data)
    
    return final

print(analyze("apple",'google'))