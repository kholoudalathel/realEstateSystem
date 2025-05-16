

import psycopg2

class DatabaseHelper:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname="real_estate_db",
                user="postgres",  # Replace with your PostgreSQL username
                password="Kholoudd322",  # Replace with your PostgreSQL password
                host="localhost",
                port="5432"
            )
            self.cursor = self.connection.cursor()
            print("Database connection successful.")
        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            self.connection = None
            self.cursor = None

    def execute_query(self, query, params=None):
        if not self.connection:
            print("No database connection available.")
            return False
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return True
        except psycopg2.Error as e:
            print(f"Query execution error: {e}")
            self.connection.rollback()
            return False

    def fetch_all(self, query, params=None):
        if not self.connection:
            print("No database connection available.")
            return []
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Data fetching error: {e}")
            return []

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed.")