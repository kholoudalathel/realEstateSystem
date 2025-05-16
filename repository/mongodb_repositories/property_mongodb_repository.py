from utils.mongodb_db_helper import MongoDBDatabaseHelper
import pandas as pd
from bson import ObjectId
from utils.enums import PropertyStatus

class PropertyMongoRepository:
    """Handles property-related database operations in MongoDB."""

    def __init__(self, db_helper: MongoDBDatabaseHelper):
        """Initialize repository with an existing MongoDB helper."""
        self.db_helper = db_helper
        self.collection = "properties"

    def add_property(self, name, price, location, landlord_id):
        """Adds a new property and links it to a landlord, returning the inserted property ID."""
        try:
            object_id = ObjectId(landlord_id)
        except Exception:
            return None

        data = {
            "name": name,
            "price": price,
            "location": location,
            "landlord_id": object_id,
            "is_sold": PropertyStatus.AVAILABLE.value,
            "buyer_id": None
        }
        return self.db_helper.insert_one(self.collection, data)

    def get_properties_by_landlord(self, landlord_id):
        """Fetches properties owned by a specific landlord and returns them as a DataFrame."""
        try:
            object_id = ObjectId(landlord_id)
        except Exception:
            return None

        properties = self.db_helper.find(self.collection, {"landlord_id": object_id})
        return pd.DataFrame(properties) if properties else None  # Converts to DataFrame if data exists

    def get_all_properties(self):
        """Fetches all properties in the system and returns them as a DataFrame."""
        properties = self.db_helper.find(self.collection)
        return pd.DataFrame(properties) if properties else None  # Converts to DataFrame if data exists

    def is_property_sold(self, property_id):
        """Checks if a property is sold and returns a boolean."""
        try:
            object_id = ObjectId(property_id)
        except Exception:
            return False

        property_record = self.db_helper.find_one(self.collection, {"_id": object_id})
        return property_record["is_sold"] == PropertyStatus.SOLD.value if property_record else False

    def mark_property_as_sold(self, property_id, buyer_id):
        """Marks a property as sold and assigns it to the buyer, returning the number of modified documents."""
        try:
            property_object_id = ObjectId(property_id)
            buyer_object_id = ObjectId(buyer_id)
        except Exception:
            return 0

        return self.db_helper.update_one(
            self.collection,
            {"_id": property_object_id},
            {"is_sold": PropertyStatus.SOLD.value, "buyer_id": buyer_object_id}
        )
