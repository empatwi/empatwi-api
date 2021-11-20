from tweepy.streaming import StreamListener
from ..mongo_db_repository import MongoDbRepository

class StreamListener(StreamListener):
    """
    Stream listener class to handle call functions
    to Tweepy stream methods
    """

    def __init__(self, keyword):
        super(StreamListener, self).__init__()
        self.keyword = keyword

    def on_status(self, status):
        """
        Method to handle streamed tweets content and save
        them into a csv file

        - If the stream contains "retweeted_status" or "quoted_status",
        status.text property does not return the tweet's full content.
        So the below validation was added to get the full content
        despite of being an original tweet, a retweet or a quoted tweet.

        - The tweet is only written on the csv file if it does not
        contain strings as "https://" or "http://" because we want
        to avoid tweets with URLs and media such as videos, GIFs and
        images.
        """
        if status.entities["urls"] == []:
            if hasattr(status, "retweeted_status"):
                try:
                    tweet_content = str(status.retweeted_status.extended_tweet["full_text"])
                except AttributeError:
                    tweet_content = str(status.retweeted_status.text)
            elif hasattr(status, "quoted_status"):
                try:
                    tweet_content = str(status.quoted_status.extended_tweet["full_text"])
                except AttributeError:
                    tweet_content = str(status.quoted_status.text)
            else:
                try:
                    tweet_content = str(status.extended_tweet["full_text"])
                except AttributeError:
                    tweet_content = str(status.text)

            user_location = str(status.user.location)
            created_at = str(status.created_at)
            entities = str(status.entities)
          
            if not ("https://" or "http://") in tweet_content:
                print(tweet_content)
                MongoDbRepository().search_result_mongo_import(created_at, tweet_content, self.keyword, user_location, entities)
            
    def on_error(self, status_code):
        if status_code == 420:
            return False