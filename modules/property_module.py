from repository.mongodb_repositories.property_mongodb_repository import PropertyMongoRepository
from repository.postgres_repositories.property_postgres_repository import PropertyPostgresRepository
from utils.postgres_db_helper import PostgreSQLDatabaseHelper
from utils.mongodb_db_helper import MongoDBDatabaseHelper

class PropertyModule:
    """Handles business logic for properties."""

    def __init__(self, db_helper):
        self.db_helper = db_helper

    def add_property(self, name, price, location, landlord_id):
        """Allows a landlord to add a new property."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            property_repository = PropertyPostgresRepository(self.db_helper)
        else:
            property_repository = PropertyMongoRepository(self.db_helper)

        property_id = property_repository.add_property(name, price, location, landlord_id)

        if property_id:
            print(f"Property '{name}' added successfully under Landlord ID {landlord_id}.")
        else:
            print("Failed to add property.")

    def list_properties(self):
        """Lists all properties in the system."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            property_repository = PropertyPostgresRepository(self.db_helper)
        else:
            property_repository = PropertyMongoRepository(self.db_helper)

        properties = property_repository.get_all_properties()

        if properties is None or properties.empty:
            print("No properties found.")
        else:
            print("\nAll Properties:")
            print(properties.to_string(index=False))  # Properly format DataFrame output

    def list_properties_by_landlord(self, landlord_id):
        """Lists properties owned by a specific landlord."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            property_repository = PropertyPostgresRepository(self.db_helper)
        else:
            property_repository = PropertyMongoRepository(self.db_helper)

        properties = property_repository.get_properties_by_landlord(landlord_id)

        if properties is None or properties.empty:
            print(f"No properties found for Landlord ID {landlord_id}.")
        else:
            print(f"\nProperties owned by Landlord ID {landlord_id}:")
            print(properties.to_string(index=False))

    def check_if_property_sold(self, property_id):
        """Checks if a property is sold."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            property_repository = PropertyPostgresRepository(self.db_helper)
        else:
            property_repository = PropertyMongoRepository(self.db_helper)

        is_sold = property_repository.is_property_sold(property_id)

        if is_sold:
            print(f"Property ID {property_id} has already been sold.")
        else:
            print(f"Property ID {property_id} is available for sale.")
