from .twitter_settings import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from .stream_listener import StreamListener
from tweepy import OAuthHandler, Stream

class TweetAcquisitionRepository():

    def stream_tweets(self, keyword):
        stream_listener = StreamListener(keyword)
        auth = OAuthHandler(API_KEY, API_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, stream_listener)
        stream.filter(track=[keyword], languages=["pt"])