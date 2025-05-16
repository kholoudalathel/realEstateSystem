from utils.db_helper import DatabaseHelper


class PropertyRepository:
    def __init__(self):
        self.db_helper = DatabaseHelper()

    def add_property(self, address, price, landlord_id):
        query = "INSERT INTO properties (address, price, landlord_id) VALUES (%s, %s, %s)"
        self.db_helper.execute_query(query, (address, price, landlord_id))

    def get_all_properties(self):
        query = "SELECT * FROM properties;"
        return self.db_helper.fetch_all(query)