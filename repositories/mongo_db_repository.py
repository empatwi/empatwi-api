import pandas as pd
import json

from db import db, col, mongo

class MongoDbRepository():

    def mongo_import(self, df):
        payload = json.loads(df.to_json(orient='records'))
        return col.insert(payload)