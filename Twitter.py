import tweepy
import TwitterKeys

from random import randint
from tweepy import OAuthHandler

class Twitter:

  def getDaveTweet(self):
    auth = OAuthHandler(TwitterKeys.consumer_key, TwitterKeys.consumer_secret)
    auth.set_access_token(TwitterKeys.access_token, TwitterKeys.access_secret)

    api = tweepy.API(auth)

    recent_tweets = api.user_timeline(user_id = '190974303', count = 100)
    return recent_tweets[randint(0, 100)].text
