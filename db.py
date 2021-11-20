import pymongo
from decouple import config

crowdsourcing_mongo = pymongo.MongoClient(config('MONGODB_ATLAS_CONNECTION_STRING_DEVELOPMENT'), connect=False)
crowdsourcing_db = pymongo.database.Database(crowdsourcing_mongo, config('MONGODB_ATLAS_DEV_NAME'))
crowdsourcing_col = pymongo.collection.Collection(crowdsourcing_db, config('MONGODB_ATLAS_COLLECTION_NAME'))

aux_mongo = pymongo.MongoClient(config('AUX_MONGODB_ATLAS_CONNECTION_STRING_DEVELOPMENT'), connect=False)
aux_db = pymongo.database.Database(aux_mongo, config('AUX_MONGODB_ATLAS_DEV_NAME'))
aux_col = pymongo.collection.Collection(aux_db, config('AUX_MONGODB_ATLAS_COLLECTION'))