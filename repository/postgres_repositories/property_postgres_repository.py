import pandas as pd
from utils.error_msgs import PROPERTY_RETRIEVAL_ERROR
from utils.enums import PropertyStatus

class PropertyPostgresRepository:
    """Handles database operations for properties in PostgreSQL."""

    def __init__(self, db_helper):
        self.db_helper = db_helper

    def add_property(self, name, price, location, landlord_id):
        """Adds a new property and links it to a landlord, returning the inserted property ID."""
        query = """
        INSERT INTO properties (name, price, location, landlord_id, is_sold)
        VALUES (%s, %s, %s, %s, %s) RETURNING id
        """
        return self.db_helper.execute_query(
            query,
            (name, price, location, landlord_id, PropertyStatus.AVAILABLE.value),
            fetch=True
        )

    def get_properties_by_landlord(self, landlord_id):
        """Fetches properties owned by a specific landlord and returns them as a DataFrame."""
        query = "SELECT id, name, price, location, is_sold FROM properties WHERE landlord_id = %s"
        properties = self.db_helper.execute_query(query, (landlord_id,), fetch=True)

        return pd.DataFrame(properties) if properties else None  # Converts to DataFrame if data exists

    def get_all_properties(self):
        """Fetches all properties in the system and returns them as a DataFrame."""
        query = "SELECT id, name, price, location, is_sold FROM properties"
        properties = self.db_helper.execute_query(query, fetch=True)

        return pd.DataFrame(properties) if properties else None  # Converts to DataFrame if data exists

    def is_property_sold(self, property_id):
        """Checks if a property is sold and returns a boolean."""
        query = "SELECT is_sold FROM properties WHERE id = %s"
        result = self.db_helper.execute_query(query, (property_id,), fetch=True)

        return result[0]["is_sold"] == PropertyStatus.SOLD.value if result else False  # Ensures correct return type

    def mark_property_as_sold(self, property_id, buyer_id):
        """Marks a property as sold and assigns it to the buyer, returning the number of affected rows."""
        query = "UPDATE properties SET is_sold = %s, buyer_id = %s WHERE id = %s"
        return self.db_helper.execute_query(query, (PropertyStatus.SOLD.value, buyer_id, property_id), fetch=False)
