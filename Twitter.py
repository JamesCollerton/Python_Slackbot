import tweepy
import twitter_keys

from random import randint
from tweepy import OAuthHandler

class Twitter:

  def getDaveTweet(self):
    auth = OAuthHandler(twitter_keys.consumer_key, twitter_keys.consumer_secret)
    auth.set_access_token(twitter_keys.access_token, twitter_keys.access_secret)
     
    api = tweepy.API(auth)

    recent_tweets = api.user_timeline(user_id = '190974303', count = 100)
    return recent_tweets[randint(0, 100)].text

