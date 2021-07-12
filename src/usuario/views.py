import sys
print(sys.path)
from .models import Usuario
from conf.settings import mongo_client
from bson.json_util import dumps, loads
import copy
import json


class User:

    @staticmethod
    async def create(data: Usuario) -> Usuario:
        query_data = dict(data)
        query = mongo_client.Usuario.insert_one(copy.deepcopy(query_data))
        return data