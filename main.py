# main.py
# Entry point, handles menu and user interactions
from repository.buyer_repository import BuyerRepository
from repository.landlord_repository import LandlordRepository
from repository.property_repository import PropertyRepository
from repository.transaction_repository import TransactionRepository


def display_menu():
    print("\nReal Estate Management System")
    print("1. Add Buyer")
    print("2. Add Landlord")
    print("3. Add Property")
    print("4. Add Transaction")
    print("5. View Buyers")
    print("6. View Landlords")
    print("7. View Properties")
    print("8. View Transactions")
    print("9. Exit")


def main():
    buyer_repo = BuyerRepository()
    landlord_repo = LandlordRepository()
    property_repo = PropertyRepository()
    transaction_repo = TransactionRepository()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter buyer name: ")
            email = input("Enter buyer email: ")
            buyer_repo.add_buyer(name, email)
        elif choice == "2":
            name = input("Enter landlord name: ")
            phone = input("Enter landlord phone: ")
            landlord_repo.add_landlord(name, phone)
        elif choice == "3":
            address = input("Enter property address: ")
            try:
                price = float(input("Enter property price: "))
                landlord_id = int(input("Enter landlord ID: "))
                property_repo.add_property(address, price, landlord_id)
            except ValueError:
                print("Invalid input! Please enter valid numbers for price and landlord ID.")
        elif choice == "4":
            try:
                buyer_id = int(input("Enter buyer ID: "))
                property_id = int(input("Enter property ID: "))
                amount = float(input("Enter transaction amount: "))
                transaction_repo.add_transaction(buyer_id, property_id, amount)
            except ValueError:
                print("Invalid input! Please enter valid numbers for buyer ID, property ID, and amount.")
        elif choice == "5":
            print(buyer_repo.get_all_buyers())
        elif choice == "6":
            print(landlord_repo.get_all_landlords())
        elif choice == "7":
            print(property_repo.get_all_properties())
        elif choice == "8":
            print(transaction_repo.get_all_transactions())
        elif choice == "9":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
