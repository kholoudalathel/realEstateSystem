from repository.mongodb_repositories.landlord_mongodb_repository import LandlordMongoRepository
from repository.postgres_repositories.landlord_postgres_repository import LandlordPostgresRepository
from utils.postgres_db_helper import PostgreSQLDatabaseHelper
from utils.mongodb_db_helper import MongoDBDatabaseHelper

class LandlordModule:
    """Handles business logic for landlords."""

    def __init__(self, db_helper):
        self.db_helper = db_helper

    def add_landlord(self, name, email, phone):
        """Registers a new landlord."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            landlord_repository = LandlordPostgresRepository(self.db_helper)
        else:
            landlord_repository = LandlordMongoRepository(self.db_helper)
            # Call repository method
            landlord_id = landlord_repository.add_landlord(name, email, phone)
            if landlord_id:
                print(f"Landlord '{name}' added successfully! Landlord ID: {landlord_id}")
            else:
                print("Failed to add landlord.")

    def list_landlords(self):
        """Displays all landlords."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            landlord_repository = LandlordPostgresRepository(self.db_helper)
        else:
            landlord_repository = LandlordMongoRepository(self.db_helper)

        landlords = landlord_repository.get_all_landlords()

        if landlords is None or landlords.empty:
            print("No landlords found.")
        else:
            print("\nList of Landlords:")
            print(landlords.to_string(index=False))  #Display DataFrame properly

    def get_landlord_details(self, landlord_id):
        """Fetches details of a single landlord."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            landlord_repository = LandlordPostgresRepository(self.db_helper)
        else:
            landlord_repository = LandlordMongoRepository(self.db_helper)

        landlord = landlord_repository.get_landlord_by_id(landlord_id)

        if landlord:
            print("\nLandlord Details:")
            for key, value in landlord.items():
                print(f"{key}: {value}")  # Properly format a dictionary output
        else:
            print("Landlord not found.")


def update_property_count(self, landlord_id, increment=1):
    """Updates the landlord's property count."""
    if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
        landlord_repository = LandlordPostgresRepository(self.db_helper)
    else:
        landlord_repository = LandlordMongoRepository(self.db_helper)

    updated_count = landlord_repository.update_property_count(landlord_id, increment)

    if updated_count > 0:
        print(f"Updated property count for Landlord ID {landlord_id}.")
    else:
        print("Failed to update property count.")