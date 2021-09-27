import time
from repositories.twitter.tweet_acquisition_repository import TweetAcquisitionRepository
from repositories.csv_treatment_repository import CsvTreatmentRepository
from repositories.learning.preprocessing_repository import PreprocessingRepository
from repositories.learning.model_application_repository import ModelApplicationRepository

tweet_acquisition_repository = TweetAcquisitionRepository()

class SearchService():

    def search(self, keyword):
        tweet_acquisition_repository.stream_tweets(keyword)
        time.sleep(1.5)
        # TODO: Subir o df remove duplicates no banco do crowdsourcing
        df = CsvTreatmentRepository().remove_raw_stream_duplicates()
        clean_df = PreprocessingRepository().apply_preprocessing(df)
        positive, negative = ModelApplicationRepository().model_application(clean_df)
        return positive, negative