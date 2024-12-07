import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] > 0:
        return "Positive"
    elif sentiment_score['compound'] < 0:
        return "Negative"
    else:
        return "Neutral"

text = input("Enter text: ")
sentiment = analyze_sentiment(text)
print(f"Sentiment: {sentiment}")
