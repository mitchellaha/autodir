from pymongo import MongoClient
from config import MONGO_SRV


MDB_CLIENT = MongoClient(MONGO_SRV)