from repository.mongodb_repositories.buyer_mongodb_repository import BuyerMongoRepository
from repository.postgres_repositories.buyer_postgres_repository import BuyerPostgresRepository
from utils.postgres_db_helper import PostgreSQLDatabaseHelper

class BuyerModule:
    """Handles buyer-related logic."""
    def __init__(self, db_helper):
        self.db_helper = db_helper

    def add_buyer(self, name, email, budget):
        """Adds a new buyer to the system."""
        # Determine which repository to use
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            buyer_repository = BuyerPostgresRepository(self.db_helper)
        else:
            buyer_repository = BuyerMongoRepository(self.db_helper)
        # Call repository method
        buyer_id = buyer_repository.add_buyer(name, email, budget)

        if buyer_id:
            print(f"Buyer '{name}' added successfully! Buyer ID: {buyer_id}")
        else:
            print("Failed to add buyer.")

    def list_buyers(self):
        """Lists all buyers in the system."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            buyer_repository = BuyerPostgresRepository(self.db_helper)
        else:
            buyer_repository = BuyerMongoRepository(self.db_helper)
        #call repository method
        buyers_df = buyer_repository.get_all_buyers()
        #display the results
        if buyers_df is None or buyers_df.empty:
            print("No buyers found.")
        else:
            print("\n List of Buyers:")
            print(buyers_df.to_string(index=False))  # Display DataFrame properly

    def get_buyer_details(self, buyer_id):
        """Fetches details of a single buyer."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            buyer_repository = BuyerPostgresRepository(self.db_helper)
        else:
            buyer_repository = BuyerMongoRepository(self.db_helper)
        # call repository method
        buyer = buyer_repository.get_buyer_by_id(buyer_id)
        # Print the buyer details (if found)
        if buyer:
            print("\n Buyer Details:")
            for key, value in buyer.items():
                print(f"{key}: {value}") #since this is a dictionary
            return buyer
        else:
            print("Buyer not found.")
            return None

    def get_buyer_budget(self, buyer_id):
        """Fetches details of a single buyer."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            buyer_repository = BuyerPostgresRepository(self.db_helper)
        else:
            buyer_repository = BuyerMongoRepository(self.db_helper)
        budget = buyer_repository.get_buyer_budget(buyer_id)
        if budget is not None:
            print(f"Buyer's budget: ${budget}")
        else:
            print("Buyer not found or budget not available.")
    def update_buyer_budget(self, buyer_id, new_budget):
        """Updates details of a single buyer."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            buyer_repository = BuyerPostgresRepository(self.db_helper)
        else:
            buyer_repository = BuyerMongoRepository(self.db_helper)

        modified_count = buyer_repository.update_buyer_budget(buyer_id, new_budget)
        if modified_count > 0:
            print(f"Buyer's budget is updated to: ${new_budget}")
        else:
            print("Buyer not found.")

    def delete_buyer(self, buyer_id):
        """Deletes a single buyer."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            buyer_repository = BuyerPostgresRepository(self.db_helper)
        else:
            buyer_repository = BuyerMongoRepository(self.db_helper)

        deleted_count = buyer_repository.delete_buyer(buyer_id)
        if deleted_count > 0:
            print(f"Buyer's budget is deleted to: ${deleted_count}")
        else:
            print("Failed to delete.")




