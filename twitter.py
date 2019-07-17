import json

#open json file, tag as 'r' for read only
tweetFile = open("tweets_small.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet id: ", tweetData[0]["id"])

print("Tweet id: ", tweetData[0]["text"])

for i in range(len(tweetData)):
    print("Tweet: ", tweetData[i]["text"])

for tweet in tweetData:
    print("Tweet: ", tweet["text"])
