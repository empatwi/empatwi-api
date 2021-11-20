import time
from pandas import errors
from repositories.twitter.tweet_acquisition_repository import TweetAcquisitionRepository
from repositories.learning.preprocessing_repository import PreprocessingRepository
from repositories.learning.model_application_repository import ModelApplicationRepository
from repositories.mongo_db_repository import MongoDbRepository

tweet_acquisition_repository = TweetAcquisitionRepository()

class SearchService():

    def search(self, keyword):
        tweet_acquisition_repository.stream_tweets(keyword)
        time.sleep(5)
        try:
            df = MongoDbRepository().read_mongo_into_dataframe(keyword)
            MongoDbRepository().crowdsourcing_mongo_import(df)
            clean_df = PreprocessingRepository().apply_preprocessing(df)
            MongoDbRepository().clear_mongo_aux(keyword)
            positive, negative, positives_explained, negatives_explained = ModelApplicationRepository().model_application(clean_df)
            return positive, negative, positives_explained, negatives_explained
        except:
            raise errors.EmptyDataError
        
    def trending_topics(self, woeid):
        return tweet_acquisition_repository.get_trending_topics(woeid)