import werkzeug
from flask.scaffold import _endpoint_from_view_func
from werkzeug.utils import cached_property

import flask

flask.helpers._endpoint_from_view_func = _endpoint_from_view_func
werkzeug.cached_property = cached_property

from flask_restplus import Api
from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(bp, version='1.0', title='Empatwi API', default='Root', default_label='Root namespace')