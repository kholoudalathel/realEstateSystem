from repository.mongodb_repositories.transaction_mongodb_repository import TransactionMongoRepository
from repository.postgres_repositories.transaction_postgres_repository import TransactionPostgresRepository
from repository.mongodb_repositories.buyer_mongodb_repository import BuyerMongoRepository
from repository.postgres_repositories.buyer_postgres_repository import BuyerPostgresRepository
from repository.mongodb_repositories.property_mongodb_repository import PropertyMongoRepository
from repository.postgres_repositories.property_postgres_repository import PropertyPostgresRepository
from utils.postgres_db_helper import PostgreSQLDatabaseHelper
from utils.mongodb_db_helper import MongoDBDatabaseHelper
from utils.error_msgs import PROPERTY_ALREADY_SOLD_ERROR

class TransactionModule:
    """Handles business logic for buying and selling properties."""

    def __init__(self, db_helper):
        self.db_helper = db_helper

    def buy_property(self, buyer_id, property_id, amount):
        """Handles property purchase, budget check, and ownership transfer."""

        # Determine which repository to use
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            transaction_repository = TransactionPostgresRepository(self.db_helper)
            buyer_repository = BuyerPostgresRepository(self.db_helper)
            property_repository = PropertyPostgresRepository(self.db_helper)
        else:
            transaction_repository = TransactionMongoRepository(self.db_helper)
            buyer_repository = BuyerMongoRepository(self.db_helper)
            property_repository = PropertyMongoRepository(self.db_helper)

        # Check if the property is already sold
        if property_repository.is_property_sold(property_id):
            print(PROPERTY_ALREADY_SOLD_ERROR)
            return

        # Get buyer's current budget
        buyer_budget = buyer_repository.get_buyer_budget(buyer_id)

        if buyer_budget is None:
            print("Buyer ID not found.")
            return

        buyer_budget = float(buyer_budget)

        # Check if the buyer has enough money
        if buyer_budget < amount:
            print(f"Transaction failed! Buyer only has ${buyer_budget}, but needs ${amount}.")
            return

        # Deduct the amount from the buyer's budget
        new_budget = buyer_budget - amount
        updated_budget = buyer_repository.update_buyer_budget(buyer_id, new_budget)

        if updated_budget == 0:
            print("Failed to update buyer's budget. Transaction aborted.")
            return

        # Record the transaction
        transaction_id = transaction_repository.create_transaction(buyer_id, property_id, amount)

        if transaction_id:
            # Assign property ownership to buyer
            updated_property = property_repository.mark_property_as_sold(property_id, buyer_id)

            if updated_property > 0:
                print(f"Purchase successful! Buyer now owns Property ID {property_id}. Remaining budget: ${new_budget}")
            else:
                print("Failed to update property ownership. Transaction may not be recorded correctly.")
        else:
            print("Transaction failed. Please try again.")

    def list_transactions(self):
        """Lists all transactions."""
        if isinstance(self.db_helper, PostgreSQLDatabaseHelper):
            transaction_repository = TransactionPostgresRepository(self.db_helper)
        else:
            transaction_repository = TransactionMongoRepository(self.db_helper)

        transactions = transaction_repository.get_all_transactions()

        if transactions is None or transactions.empty:
            print("No transactions found.")
        else:
            print("\nTransaction History:")
            print(transactions.to_string(index=False))
