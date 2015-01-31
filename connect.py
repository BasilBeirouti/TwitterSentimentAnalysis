__author__ = 'basilbeirouti'

import json
import tweepy

def getapi():
    consumer_key="sT3ezd7gqJl9tJDwbuucFJPnS"
    consumer_secret="9gxhm4yGQFC5lnh03yH2KmiOYZ6dkSsFdog6i0pwZan621IICg"
    access_token="3003051230-VRAiMwErEEHLVBhYkzajEmtZLZDjNnUeT38z8TX"
    access_token_secret="XBRc2iRkEiyBmf5ig6Nr84QbeMyIJOZ4snhBewMIXGXTK"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

# you can run the print command below, which should print your username if the connection is successful

# print(api.me().name)

# If the application settings are set for "Read and Write" then this line should tweet out the message
# to your account's timeline. The "Read and Write" setting is on https://dev.twitter.com/apps

#api.update_status(status='Updating using OAuth authentication via Tweepy!')


