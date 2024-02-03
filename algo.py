
'''<script async src="https://cse.google.com/cse.js?cx=e3bff4e8fad4e4527">
</script>
<div class="gcse-search"></div>
'''

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from googleapiclient.discovery import build
from newsapi import NewsApiClient


def scrape_news(ticker):
    data = []
    newsapi = NewsApiClient(api_key='2c8d1b7bc85044e2974985132597e395')
    everything = newsapi.get_everything(q=ticker, language='en')

    for article in everything['articles']:
        data.append(article['title'])

    return data

def scrape_google(ticker):
    titles = []
    service = build("customsearch", "v1", developerKey="AIzaSyB-_9fmxeuHTgwLFDqNeC5dMqoNYUpgrqg")
    res = service.cse().list(q=ticker, cx="e3bff4e8fad4e4527", num=10).execute()
    results = res['items']
    for result in results:
        titles.append(result['title'])
    return titles

def scrape_twitter(ticker):
    pass

def pull_data(ticker, source):
    query = ticker + "+ stock"
    if source == "google":
        data = scrape_google(query)
    elif source == "twitter":
        data = scrape_twitter(query)
    elif source == "news":
        data = scrape_news(query)
    else:
        data = []

    return data

def get_sentiment(data):
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    result = 0

    for val in data:
        ss = sid.polarity_scores(val)
        result += ss['pos']

    result = result/len(data)

    return result

def analyze(ticker, source):
    data = pull_data(ticker, source)
    final = -1
    if len(data) > 0:
        final =  get_sentiment(data)
    
    return final