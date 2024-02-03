import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def train():
    return


def analyze(ticker, source):
    sid = SentimentIntensityAnalyzer()
    pos = 0
    neg = 0
    
    ss = sid.polarity_scores(ticker)

    print(ss)

analyze("wow this is bad")