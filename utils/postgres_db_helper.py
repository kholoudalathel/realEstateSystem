import psycopg2
import pandas as pd
from utils.error_msgs import POSTGRES_DB_CONNECTION_ERROR, QUERY_EXECUTION_ERROR

class PostgreSQLDatabaseHelper:
    """Handles PostgreSQL database connections and queries."""

    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        """Initialize and connect to the database."""
        try:
            self.connection = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port
            )
            self.cursor = self.connection.cursor()
            print("Database connection successful.")
        except psycopg2.Error as e:
            print(POSTGRES_DB_CONNECTION_ERROR.format(e))
            self.connection = None
            self.cursor = None

    def execute_query(self, query, params=None, fetch=False, single_value=False):

        if not self.connection or not self.cursor:
            print(POSTGRES_DB_CONNECTION_ERROR)
            return None
        try:
            self.cursor.execute(query, params)

            if fetch:
                results = self.cursor.fetchall()
                return results
            self.connection.commit()
            return self.cursor.rowcount()

        except psycopg2.Error as e:
            print(QUERY_EXECUTION_ERROR.format(e))
            self.connection.rollback()
            return None

    def close_connection(self):
        """Closes the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def __del__(self):
        """Ensure database connection is closed when the object is deleted."""
        self.close_connection()
