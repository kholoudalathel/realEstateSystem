import pandas as pd
from utils.error_msgs import LANDLORD_RETRIEVAL_ERROR

class LandlordPostgresRepository:
    """Handles database operations for landlords."""

    def __init__(self, db_helper):
        self.db_helper = db_helper


    def add_landlord(self, name, email, phone):
        """Adds a new landlord to the database and returns the inserted ID."""
        query = """
        INSERT INTO landlords (name, email, phone)
        VALUES (%s, %s, %s) RETURNING id
        """
        return self.db_helper.execute_query(query, (name, email, phone), fetch=True)

    def get_all_landlords(self):
        """Fetches all landlords and returns them as a Pandas DataFrame."""
        query = "SELECT id, name, email, phone, total_properties FROM landlords"
        landlords = self.db_helper.execute_query(query, fetch=True)

        return pd.DataFrame(landlords) if landlords else None  # Converts to DataFrame if data exists

    def get_landlord_by_id(self, landlord_id):
        """Fetches a single landlord by ID and returns as a dictionary."""
        query = "SELECT id, name, email, phone, total_properties FROM landlords WHERE id = %s"
        landlords = self.db_helper.execute_query(query, (landlord_id,), fetch=True)

        return landlords[0] if landlords else None  # Returns dictionary like MongoDB repository

    def update_property_count(self, landlord_id):
        """Updates the total number of properties a landlord owns and returns the number of affected rows."""
        query = """
        UPDATE landlords 
        SET total_properties = (SELECT COUNT(*) FROM properties WHERE landlord_id = %s) 
        WHERE id = %s
        """
        return self.db_helper.execute_query(query, (landlord_id, landlord_id), fetch=False)  # Returns affected row count