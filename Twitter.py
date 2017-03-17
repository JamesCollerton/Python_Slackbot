import tweepy
import Keys

from random import randint
from tweepy import OAuthHandler

class Twitter:

  def getDaveTweet(self):
    """
    Sets up the connection to the twitter API using the keys
    in the Keys.py ignored file and then gets a random tweet
    from the last 100.
    """
    auth = OAuthHandler(Keys.twitter_consumer_key, Keys.twitter_consumer_secret)
    auth.set_access_token(Keys.twitter_access_token, Keys.twitter_access_secret)

    api = tweepy.API(auth)

    recent_tweets = api.user_timeline(user_id = '190974303', count = 100)
    return recent_tweets[randint(0, 100)].text
