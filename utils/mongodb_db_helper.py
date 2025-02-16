
from pymongo import MongoClient
from pymongo import errors
from utils.error_msgs import MONGO_DB_CONNECTION_ERROR

class MongoDBDatabaseHelper:
    def __init__(self, uri, db_name):
        """Initialize MongoDB connection"""
        self.uri = uri
        self.db_name = db_name
        if not self.uri or not self.db_name:
            raise ValueError("error: MONGO_URI or DATABASE_NAME is missing!")
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            print(f"Connected to MongoDB at {uri}, using database: {db_name}")
        except errors.PyMongoError as e:
            print(MONGO_DB_CONNECTION_ERROR)

    def insert_one(self, collection, document):
        """Insert a single document into the collection"""
        result = self.db[collection].insert_one(document)
        # print(f"Inserted {result.inserted_id} into {collection}")
        return result.inserted_id

    def insert_many(self, collection, documents):
        """Insert multiple documents into the collection and return inserted IDs as a DataFrame."""
        result = self.db[collection].insert_many(documents)
        return result.inserted_ids if result.inserted_ids else None

    def find_one(self, collection, query):
        """Find one document in the collection."""
        try:
            return self.db[collection].find_one(query)  #Returns dictionary or None
        except errors.PyMongoError as e:
            print(f"Error finding document: {e}") #might put this in error msgs file later
            return None

    def find(self, collection, query=None):
        """Find multiple documents and return it as a list of dictionaries"""
        query = query or {}
        try:
            cursor = self.db[collection].find(query)
            return list(cursor)
        except errors.PyMongoError as e:
            print(f"Error finding document: {e}")
            return []

    def update_one(self, collection, query, new_values):
        """Update one document in the collection"""
        try:
            result = self.db[collection].update_one(query, {"$set": new_values})
            return result.modified_count
        except errors.PyMongoError as e:
            print(f"Error updating document: {e}")
            return 0

    def delete_one(self, collection, query):
        """Delete one document in the collection"""
        try:
            result = self.db[collection].delete_one(query)
            return result.deleted_count
        except errors.PyMongoError as e:
            print(f"Error deleting document: {e}")
            return 0

    def close_connection(self):
        """Close the database connection safely"""
        if hasattr(self, "client") and self.client:
            self.client.close()
            print("MongoDB connection closed")
        else:
            print("No active MongoDB connection to close!")
