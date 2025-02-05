from utils.db_helper import DatabaseHelper


class LandlordRepository:
    def __init__(self):
        self.db_helper = DatabaseHelper()

    def add_landlord(self, name, phone):
        query = "INSERT INTO landlords (name, phone) VALUES (%s, %s)"
        self.db_helper.execute_query(query, (name, phone))

    def get_all_landlords(self):
        query = "SELECT * FROM landlords;"
        return self.db_helper.fetch_all(query)
