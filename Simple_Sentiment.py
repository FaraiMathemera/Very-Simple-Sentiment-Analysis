import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'KEY'
consumer_secret= 'SECRET KEY'

access_token='ACCESS KEY'
access_token_secret='ACCESS SECRET KEY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 2 - Retrieve Tweets
public_tweets = api.search('Cape Town')


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 3 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
