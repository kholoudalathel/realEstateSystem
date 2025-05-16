import pandas as pd
from utils.error_msgs import BUYER_RETRIEVAL_ERROR

class BuyerPostgresRepository:
    """Handles database operations for buyers."""

    def __init__(self, db_helper):
        self.db_helper = db_helper

    def add_buyer(self, name, email, budget):
        """Adds a new buyer with an initial budget."""
        query = """
        INSERT INTO buyers (name, email, budget)
        VALUES (%s, %s, %s) RETURNING id
        """
        return self.db_helper.execute_query(query, (name, email, budget), fetch=True)

    def get_all_buyers(self):
        """Fetches all buyers as a DataFrame."""
        query = "SELECT id, name, email, budget FROM buyers"
        buyers = self.db_helper.execute_query(query, fetch=True)

        return pd.DataFrame(buyers) if buyers else None

    def get_buyer_by_id(self, buyer_id):
        """Fetches a single buyer by ID."""
        query = "SELECT id, name, email, budget FROM buyers WHERE id = %s"
        buyers = self.db_helper.execute_query(query, (buyer_id,), fetch=True)
        return buyers[0] if buyers else None #Returns dictionary like MongoDB repo

    def get_buyer_budget(self, buyer_id):
        """Fetches the budget of a buyer."""
        query = "SELECT budget FROM buyers WHERE id = %s"
        result = self.db_helper.execute_query(query, (buyer_id,), fetch=True)
        return result[0]["budget"] if result else None

    def update_buyer_budget(self, buyer_id, new_budget):
        """Updates a buyer's budget."""
        if new_budget < 0:
            print("Budget cannot be negative!")
            return 0
        query = "UPDATE buyers SET budget = %s WHERE id = %s"
        return self.db_helper.execute_query(query, (new_budget, buyer_id), fetch=False)

    def delete_buyer(self, buyer_id):
        """Deletes a buyer and returns the number of deleted records."""
        query = "DELETE FROM buyers WHERE id = %s"
        return self.db_helper.execute_query(query, (buyer_id,), fetch=False)