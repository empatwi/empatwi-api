import werkzeug
import time

from werkzeug.utils import cached_property
werkzeug.cached_property = cached_property

from api import api
from flask_restplus import Resource, fields, Namespace
from flask import request
from repositories.twitter.tweet_acquisition_repository import TweetAcquisitionRepository
from repositories.csv_treatment_repository import CsvTreatmentRepository

search_ns = Namespace('search', description='Tweet search related operations')
search_fields = api.model('Search', {'keyword': fields.String(required=True)})

tweet_acquisition_repository = TweetAcquisitionRepository()

@search_ns.route('/')
@search_ns.expect(search_fields, validate=True)
class Search(Resource):
    @search_ns.doc(responses={
        200: 'OK',
        400: 'BAD REQUEST',
        500: 'INTERNAL SERVER ERROR'
    })
    @search_ns.doc(description='Searches for keyword on Twitter through stream listener')
    def post(self):
        payload = request.get_json()
        keyword = payload['keyword']
        tweet_acquisition_repository.stream_tweets(keyword)
        time.sleep(0.5)
        CsvTreatmentRepository().remove_raw_stream_duplicates()
        return 200