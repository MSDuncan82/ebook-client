from pymongo import MongoClient


def download_profile(user_id):

    client = MongoClient("mongodb://mongo:27017")

    db = client.connections
    col = db["connections"]

    result = col.find_one({"_id": user_id})

    return result
