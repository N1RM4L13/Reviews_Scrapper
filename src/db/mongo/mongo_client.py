from typing import Union, Any, Mapping

from motor import MotorClient
import motor.motor_asyncio

class MongoClient:
    @classmethod
    def get_client(cls):
        motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

    @classmethod
    def get_client(cls):
        client = MotorClient()
        return client


