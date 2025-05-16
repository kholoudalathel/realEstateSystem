import os
from utils.postgres_db_helper import PostgreSQLDatabaseHelper
from utils.mongodb_db_helper import MongoDBDatabaseHelper
from modules.buyer_module import BuyerModule
from modules.landlord_module import LandlordModule
from modules.property_module import PropertyModule
from modules.transaction_module import TransactionModule
from utils.error_msgs import MISSING_ENV_VARIABLE_ERROR
from utils.error_msgs import INVALID_DATABASE_TYPE_ERROR
from utils.enums import DatabaseType

def check_required_env_vars(database_type):
    """Ensure all required environment variables are set based on the database type."""
    if database_type == DatabaseType.POSTGRESQL.value:
        required_vars = ["POSTGRES_DB_NAME", "POSTGRES_DB_USER", "POSTGRES_DB_PASSWORD", "POSTGRES_DB_HOST", "POSTGRES_DB_PORT"]
    elif database_type == DatabaseType.MONGODB.value:
        required_vars = ["MONGO_DB_URI", "MONGO_DB_NAME"]
    else:
        raise Exception(INVALID_DATABASE_TYPE_ERROR)

    for var in required_vars:
        if not os.getenv(var):
            print(MISSING_ENV_VARIABLE_ERROR.format(var))
            exit(1)  # Exit the program if a required env variable is missing

def main():
    """Main function to run the real estate management system."""

    # Ensure `DATABASE_TYPE` is set and normalized
    database_type = os.getenv("DATABASE_TYPE", "").strip().lower()
    if not database_type:
        print("DATABASE_TYPE is missing! Please set it to 'postgresql' or 'mongodb'.")
        exit(1)

    check_required_env_vars(database_type)

    # Postgres helper implementation

    if database_type == DatabaseType.POSTGRESQL.value:
        postgres_db_helper = PostgreSQLDatabaseHelper(
            db_name=os.getenv("POSTGRES_DB_NAME"),
            db_user=os.getenv("POSTGRES_DB_USER"),
            db_password=os.getenv("POSTGRES_DB_PASSWORD"),
            db_host=os.getenv("POSTGRES_DB_HOST"),
            db_port=os.getenv("POSTGRES_DB_PORT")
        )
        # Pass postgres_db_helper when creating module objects
        buyer_module = BuyerModule(postgres_db_helper)
        landlord_module = LandlordModule(postgres_db_helper)
        property_module = PropertyModule(postgres_db_helper)
        transaction_module = TransactionModule(postgres_db_helper)

    elif database_type == DatabaseType.MONGODB.value:

        mongo_uri = os.getenv("MONGO_DB_URI")
        mongo_db_name = os.getenv("MONGO_DB_NAME")

        # Create a MongoDB helper object
        mongodb_db_helper = MongoDBDatabaseHelper(mongo_uri, mongo_db_name)

        # Pass mongodb_db_helper when creating module objects
        buyer_module = BuyerModule(mongodb_db_helper)
        landlord_module = LandlordModule(mongodb_db_helper)
        property_module = PropertyModule(mongodb_db_helper)
        transaction_module = TransactionModule(mongodb_db_helper)
    else:
        raise Exception(INVALID_DATABASE_TYPE_ERROR)

    while True:
        print("\nReal Estate Management System")
        print("1. Add Buyer")
        print("2. List Buyers")
        print("3. Add Landlord")
        print("4. List Landlords")
        print("5. Add Property")
        print("6. List Properties")
        print("7. Buy Property")
        print("8. List Transactions")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter buyer name: ")
            email = input("Enter buyer email: ")
            budget = float(input("Enter buyer's budget: "))
            buyer_module.add_buyer(name, email, budget)
        elif choice == "2":
            buyer_module.list_buyers()
        elif choice == "3":
            name = input("Enter landlord name: ")
            email = input("Enter landlord email: ")
            phone = input("Enter landlord phone number: ")
            landlord_module.add_landlord(name, email, phone)
        elif choice == "4":
            landlord_module.list_landlords()
        elif choice == "5":
            landlord_id = input("Enter Landlord ID: ")
            name = input("Enter Property Name: ")
            price = float(input("Enter Property Price: "))
            location = input("Enter Property Location: ")
            property_module.add_property(name, price, location, landlord_id)
        elif choice == "6":
            property_module.list_properties()
        elif choice == "7":
            buyer_id = input("Enter Buyer ID: ")
            property_id = input("Enter Property ID: ")
            amount = float(input("Enter purchase amount: "))
            transaction_module.buy_property(buyer_id, property_id, amount)
        elif choice == "8":
            transaction_module.list_transactions()
        elif choice == "9":
            print("Exiting system. Goodbye!")
            break



if __name__ == "__main__":
    main()