import pymongo

class Database:
    DATABASE = None
    URI = "http://127.0.0.1:27017"

    @staticmethod
    def initialize():
        #client = pymongo.MongoClient(Database.URI)
        client = pymongo.MongoClient('localhost',27017)
        Database.DATABASE = client['User'] # Database

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def findone(collection,data):
        Database.DATABASE[collection].find_one(data)

    @staticmethod
    def find(collection):
        return Database.DATABASE[collection].find()
