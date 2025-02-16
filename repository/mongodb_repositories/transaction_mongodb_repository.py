from utils.mongodb_db_helper import MongoDBDatabaseHelper
import pandas as pd
from bson import ObjectId

class TransactionMongoRepository:
    """Handles transaction-related database operations in MongoDB."""

    def __init__(self, db_helper: MongoDBDatabaseHelper):
        """Initialize repository with an existing MongoDB helper."""
        self.db_helper = db_helper
        self.collection = "transactions"

    def create_transaction(self, buyer_id, property_id, amount):
        """Records a property purchase transaction and returns the inserted transaction ID."""
        try:
            buyer_object_id = ObjectId(buyer_id)
            property_object_id = ObjectId(property_id)
        except Exception:
            return None

        data = {
            "buyer_id": buyer_object_id,
            "property_id": property_object_id,
            "amount": amount,
            "transaction_date": pd.Timestamp.now()
        }
        return self.db_helper.insert_one(self.collection, data)

    def get_all_transactions(self):
        """Fetches all transaction records and returns them as a Pandas DataFrame."""
        transactions = self.db_helper.find(self.collection)
        return pd.DataFrame(transactions) if transactions else None  # Converts to DataFrame if data exists
