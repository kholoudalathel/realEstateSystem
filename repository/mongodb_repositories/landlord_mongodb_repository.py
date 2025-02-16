
from utils.mongodb_db_helper import MongoDBDatabaseHelper
from bson import ObjectId  # Needed for MongoDB ObjectId conversion
import pandas as pd

class LandlordMongoRepository:

    def __init__(self, db_helper: MongoDBDatabaseHelper):
        self.db_helper = db_helper
        self.collection = "landlords"

    def add_landlord(self, name, email, phone):
        """Adds a new landlord to the database."""
        data = {"name": name, "email": email, "phone": phone}
        return self.db_helper.insert_one(self.collection, data)

    def get_all_landlords(self):
        """Retrieves all landlords and returns them as a Pandas DataFrame."""
        landlords = self.db_helper.find(self.collection)  # Gets raw list of dictionaries
        return pd.DataFrame(landlords) if landlords else None  # Converts to DataFrame if data exists

    def get_landlord_by_id(self, landlord_id):
        """Retrieves a landlord by ID and returns as a dictionary."""
        try:
            object_id = ObjectId(landlord_id)  # Convert string ID to ObjectId
        except Exception:
            return None  # Handle invalid ID format
        return self.db_helper.find_one(self.collection, {"_id": object_id})

    def update_property_count(self, landlord_id, increment=1):
        """Increments or decrements the total property count of the landlord."""
        try:
            object_id = ObjectId(landlord_id)  # Convert string ID to ObjectId
        except Exception:
            return 0  # Return 0 if invalid ID format

        result = self.db_helper.update_one(
            self.collection,
            {"_id": object_id},
            {"$inc": {"total_properties": increment}}  #  Increments or decrements count
        )
        return result  # Returns modified count







