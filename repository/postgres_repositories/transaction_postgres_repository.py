import pandas as pd
from utils.error_msgs import TRANSACTION_ERROR

class TransactionPostgresRepository:
    """Handles database operations for transactions in PostgreSQL."""
    def __init__(self, db_helper):
        self.db_helper = db_helper

    def create_transaction(self, buyer_id, property_id, amount):
        """Records a property purchase transaction and returns the transaction ID."""
        try:
            query = """
            INSERT INTO transactions (buyer_id, property_id, amount)
            VALUES (%s, %s, %s) RETURNING id
            """
            return self.db_helper.execute_query(query, (buyer_id, property_id, amount), fetch=True)
        except Exception as e:
            print(TRANSACTION_ERROR.format(e))
            return None

    def get_all_transactions(self):
        """Fetches all transaction records and returns them as a Pandas DataFrame."""
        query = """
        SELECT t.id, b.name AS buyer_name, p.name AS property_name, t.amount, t.transaction_date
        FROM transactions t
        JOIN buyers b ON t.buyer_id = b.id
        JOIN properties p ON t.property_id = p.id
        """
        transactions = self.db_helper.execute_query(query, fetch=True)

        return pd.DataFrame(transactions) if transactions else None  # Converts to DataFrame if data exists
