'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
def averagepolarity(polarity):
    total = 0
    for i in polarity:
        total + i
    totalpolarity = total/(len(polarity))
    return totalpolarity

def get_sentiment(polarity, subjectivity):
    polarity = []
    subjectivity = []

    for tweet in tweetData:
        testimonial = TextBlob(tweet["text"])
        polarity.append(testimonial.sentiment.polarity)
        subjectivity.append(testimonial.sentiment.polarity)

def main():
    get_sentiment(polarity)
    averagepolarity(polarity)
    averagepolarity = averagepolarity(polarity)
    print(averagepolarity)


# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)

if __name__ == '__main__':
    main()
