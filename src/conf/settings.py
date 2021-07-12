from pymongo import MongoClient


mongo_client = MongoClient('mongodb://root:example@127.0.0.1:27017')
mongo_client = mongo_client.Agenda
print("CONNECTED TO MONGO")