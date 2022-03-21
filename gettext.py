import tweepy
import pandas as pd

# Replace the following strings with your own keys and secrets
TOKEN =  '1381861403401723904-tU1igc3IcyP1PEcG20d2gXcBQuIUXZ'
TOKEN_SECRET = 'ux0rfRBle3Tx6Gi1XtLWo8DhZSrTaHGcTccTl2iipZmeo'
CONSUMER_KEY ='zLT5oOnJyWPjc8SrJa4AZ4P9d'
CONSUMER_SECRET = 'aJQbQqXbDILewAsBK2zOaASJmG1uXD6V9X7m0Sn4c8aBp9HQOs'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TOKEN,TOKEN_SECRET)

api = tweepy.API(auth)
cursor= tweepy.Cursor(api.search_tweets( q="Bitcoin"),tweet_mode="extended").item(1)
for tweet in cursor:
    print(tweet.full_text)