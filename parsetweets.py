__author__ = 'basilbeirouti'

import connect as cn
import term_sentiment as ts
import datetime as dt
import time

#presumed default query. Will add functions to change these later
q='bitcoin'
lang='en'
count=100

#returns the terms dictionary, each key-value pair consists of a word (string) it's corresponding score (integer)
termsdict=ts.parseafinn()

#returns the score of a single word by checking termsdict. If the word is not included, returns 0.
def scoreword(word):
    if termsdict.has_key(word):
        return termsdict.get(word)
    else:
        return 0

#scores an entire tweet by calling scoreword on each individual word in the tweet
def scoretweet(tweet):
    wordarray=tweet.split()
    score=0
    for word in wordarray:
        score=score+scoreword(word)
    return score

#performs a query with the parameters at top of file, returns tweets - SearchResults type object defined in tweepy
def gettweets():
    api=cn.getapi()
    tweets=api.search(q="bitcoin",lang=lang,count=count)
    return tweets

#extracts and returns the actual text of each tweet in an array of strings
def gettweettext():
    tweets=gettweets()
    textarray=[]
    for tweet in tweets:
        textarray.append(tweet.text)
    return textarray

#extracts and returns an array of tweetinfo, tweetinfo is a 2-element array containing a tweet text and its score
def twsc_array():
    textarray=gettweettext()
    scorearray=[]
    for text in textarray:
        scorearray.append(scoretweet(text))
    return zip(textarray,scorearray)

#returns array of integers corresponding to score
def getscorearray():
    zipped=twsc_array()
    scorearray=[element[1] for element in zipped]
    return scorearray

#sums up the score from a single batch of tweets. The number in the batch will be equal to "count" variable
def getbatchscore():
    batchscore=sum(getscorearray())
    return batchscore

#obtains a batch of tweets, prints the current time + tab character + batchscore
def timestampscore():
    print str(time.time())+'\t' + str(getbatchscore())

#prints tweet batch score (100 tweets) and the time (in seconds since epoch) every 60 seconds continuously
#commands to run from terminal and write output to a file called output.txt:
# cd ~/GitHub/assignment1_modified
#python parsetweets.py > output.txt

def main():
    while True:
        timestampscore()
        time.sleep(60)

if __name__ == '__main__':
    main()





