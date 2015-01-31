import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

#fuctions to create and manipulate the word-score dict object, which matches words to their corresponding sentiment
#score value.

def parseafinn(afinn="AFINN-111.txt"):
    terms=[line for line in open(afinn)]
    scores={} #initialize empty dictionary object
    for line in terms:
        word,score=line.split("\t")
        scores[word]=int(score) #convert each word's score to an integer and assign it to that word in the dict
    return scores

def printscores():
    scores=parseafinn()
    print scores.items() #Print every (term,score) pair in the dict scores
