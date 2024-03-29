import time
import tweepy

from .twitter_settings import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from .stream_listener import StreamListener
from tweepy import OAuthHandler, Stream

class TweetAcquisitionRepository():

    def stream_tweets(self, keyword):
        """ Streams tweets for 10 seconds
        """
        stream_listener = StreamListener(keyword)
        auth = OAuthHandler(API_KEY, API_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, stream_listener)
        stream.filter(track=[keyword], languages=["pt"], is_async=True)
        time.sleep(10)
        stream.disconnect()

    def get_trending_topics(self, woeid):
        auth = OAuthHandler(API_KEY, API_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        trends = api.trends_place(id=woeid)
        return trends