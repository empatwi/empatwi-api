import werkzeug
import time

from werkzeug.utils import cached_property
werkzeug.cached_property = cached_property

from api import api
from flask_restplus import Resource, fields, Namespace
from flask import request
from pandas import errors
from parsers.search_result_parser import SearchResultParser

search_ns = Namespace('search', description='Tweet search related operations')
search_fields = api.model('Search', {'keyword': fields.String(required=True)})

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
        try:
            return SearchResultParser().search_result_parser(keyword), 200
        except errors.EmptyDataError:
            return 404
        except:
            return 500

@search_ns.route('/trending-topics')
class SearchTrendingTopics(Resource):
    @search_ns.doc(responses={
        200: 'OK',
        400: 'BAD REQUEST',
        500: 'INTERNAL SERVER ERROR'
    })
    @search_ns.doc(description='Searches for current trending topics')
    def get(self):
        try:
            return SearchResultParser().trending_topics_parser(23424768), 200
        except:
            return 500