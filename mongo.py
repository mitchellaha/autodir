import os

from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()



MDB_CLIENT = MongoClient(os.getenv("MONGO_SRV"))
tcrDB = MDB_CLIENT.tcr
customersCOL = tcrDB.customers_grid

def get_customers():
    filter = { "Status": { "$ne": "I" } }
    projection = { "CustomerName": 1, "CustomerID": 1, "_id": 0}
    query = customersCOL.find(filter=filter, projection=projection)
    return [customer for customer in query]