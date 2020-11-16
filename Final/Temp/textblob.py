#py2.7
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


blob = TextBlob(open("poe.txt").read())
for item in blob.sentences:
    if item.sentiment.polarity > 0:
        print "Positive Sentences"
        print item.replace('\n', ' ')
        print item.sentiment.polarity
        print item.sentiment.subjectivity

