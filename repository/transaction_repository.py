from utils.db_helper import DatabaseHelper


class TransactionRepository:
    def __init__(self):
        self.db_helper = DatabaseHelper()

    def add_transaction(self, buyer_id, property_id, amount):
        query = "INSERT INTO transactions (buyer_id, property_id, amount) VALUES (%s, %s, %s)"
        self.db_helper.execute_query(query, (buyer_id, property_id, amount))

    def get_all_transactions(self):
        query = "SELECT * FROM transactions;"
        return self.db_helper.fetch_all(query)