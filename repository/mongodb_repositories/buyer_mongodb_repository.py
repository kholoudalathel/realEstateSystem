from utils.mongodb_db_helper import MongoDBDatabaseHelper
from bson import ObjectId  # Needed for MongoDB ObjectId conversion
import pandas as pd

class BuyerMongoRepository:
    """Handles buyer-related database operations in MongoDB."""
    def __init__(self, db_helper: MongoDBDatabaseHelper):
        self.db_helper = db_helper
        self.collection = "buyers"

    def add_buyer(self, name, email, budget):
        """Adds a new buyer to the database."""
        data = {"name": name, "email": email, "budget": budget}
        return self.db_helper.insert_one(self.collection, data)

    def get_all_buyers(self):
        """Gets all buyers as a pandas dataframe from the database."""
        buyers = self.db_helper.find(self.collection)
        return pd.DataFrame(buyers) if buyers else None

    def get_buyer_by_id(self, id):
        """Gets a buyer by ID from the database."""
        try:
            object_id = ObjectId(id)  #Convert to ObjectId
        except Exception:
            return None

        return self.db_helper.find_one(self.collection, {"_id": object_id})

    def get_buyer_budget(self, id):
        """Gets a buyer's budget from the database."""
        try:
            object_id = ObjectId(id)  #Convert to ObjectId
        except Exception:
            return None

        buyer = self.db_helper.find_one(self.collection, {"_id": object_id})
        return buyer.get("budget") if buyer else None  # we use .get() to avoid errors

    def update_buyer_budget(self, id, budget):
        """Updates a buyer's budget in the database."""
        try:
            object_id = ObjectId(id)
        except Exception:
            return 0
        return self.db_helper.update_one(self.collection, {"_id": object_id},{"budget": budget})

    def delete_buyer(self, id):
        """Deletes a buyer from the database."""
        try:
            object_id = ObjectId(id)
        except Exception:
            return 0

        return self.db_helper.delete_one(self.collection, {"_id": object_id})
