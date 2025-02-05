from utils.db_helper import DatabaseHelper


class BuyerRepository:
    def __init__(self):
        self.db_helper = DatabaseHelper()

    def add_buyer(self, name, email):
        query = "INSERT INTO buyers (name, email) VALUES (%s, %s)"
        self.db_helper.execute_query(query, (name, email))

    def get_all_buyers(self):
        query = "SELECT * FROM buyers;"
        return self.db_helper.fetch_all(query)