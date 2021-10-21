import pandas as pd
import json

from pandas import errors
from decouple import config
from db import crowdsourcing_col, aux_col, aux_db

class MongoDbRepository():

    def crowdsourcing_mongo_import(self, df):
        payload = json.loads(df.to_json(orient='records'))
        return crowdsourcing_col.insert(payload)

    def search_result_mongo_import(self, created_at, tweet_content, keyword, user_location, entities):
        result = {
            "created_at": created_at,
            "tweet_content": tweet_content,
            "keyword": keyword,
            "user_location": user_location,
            "entities": entities
        }
        aux_col.insert(result)

    def read_mongo_into_dataframe(self, keyword):
        cursor = aux_db[config('AUX_MONGODB_ATLAS_COLLECTION')].find({'keyword': keyword})
        df = pd.DataFrame(list(cursor))
        if df.empty:
            return errors.EmptyDataError
        else:
            df = df.drop(columns='_id', axis=1)
            return df

    def clear_mongo_aux(self, keyword):
        aux_db[config('AUX_MONGODB_ATLAS_COLLECTION')].remove({'keyword': keyword})