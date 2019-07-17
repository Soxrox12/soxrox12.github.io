'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

import numpy as np


#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
#create empty lists for polarity and subjectivity
polarity = []
subjectivity = []
 #iterate through tweets. For each tweet, find the polarity and subjectivity and append it to lists
for tweet in tweetData:
    #create textblob for each tweet
    testimonial = TextBlob(tweet["text"])
    #find polarity and append to polarity list
    polarity.append(testimonial.sentiment.polarity)
    #find subjectivity and append to subjectivity list
    subjectivity.append(testimonial.sentiment.subjectivity)

#set total to 0
total = 0
#loop through polarity list, adding each polarity value to total variable
for i in polarity:
    total += i
#find average polarity by dividing total by length of the polarity list
avgpolarity = total/(len(polarity))
#return avgpolarity

#create totalS variable and set to 0; will add subjectivity values
totalS = 0
#loop through subjectivity list, adding each subjectivity value to totalS variable
for i in subjectivity:
    totalS += i
#find average subjectivity by dividing totalS by the length of the subjectivity list
avgsubjectivity = totalS/(len(subjectivity))
#return avgsubjectivity

#print the average polarity and subjectivity
print("The average polarity is " + str(avgpolarity))
print("The average subjectivity is " + str(avgsubjectivity))

'''
plt.hist(polarity, color = "c", bins = None)
plt.xlabel("Polarity")
plt.ylabel("Number of Tweets")
plt.title("Polarity of Tweets")
plt.grid(True)
plt.show()
plt.savefig("polarity.png")

plt.hist(subjectivity, color = "khaki")
plt.xlabel("Subjectivity")
plt.ylabel("Number of Tweets")
plt.title("Subjectivity of Tweet")
plt.grid(True)
plt.show()
plt.savefig("subjectivity.png")

plt.scatter(polarity, subjectivity)
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.title("Scatterplot of Polarity and Subjectivity")
plt.grid(True)
plt.show()
'''
#create empty string for tweets
tweet_string = ""
#loop through tweets, adding text to tweet_string
for tweet in tweetData:
    tweet_string += tweet["text"]

#create text blob from tweet_string
tweetblob = TextBlob(tweet_string)
#create list of words to filter from wordblob
wordsFilter = ["and", 'or', 'but', 'about', 'the']
#create empty dictionary put filtered words in
filteredDict = dict()

#loop through all words in tweetblob string, filtering unwanted words
for word in tweetblob.words:
    #take out short words
    if len(word) < 3:
        continue
    #take out filtered words
    if word in wordsFilter:
        continue
    #make sure word is actually a word
    if not word.isalpha():
        continue
    #add words that fail all if statements to the filtered dictionary
    filteredDict[word.lower()] = tweetblob.word_counts[word.lower()]

#create a wordcloud


wordcloud = WordCloud(width = 512, height = 512, background_color='white').generate_from_frequencies(filteredDict)
plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

print(tweet_string)
# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)

#if __name__ == '__main__':
    #main()
