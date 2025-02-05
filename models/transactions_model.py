class Transaction:
    def __init__(self, transaction_id, buyer_id, property_id, amount):
        self.transaction_id = transaction_id
        self.buyer_id = buyer_id
        self.property_id = property_id
        self.amount = amount

    def get_details(self):
        return f"Transaction ID: {self.transaction_id}, Buyer ID: {self.buyer_id}, Property ID: {self.property_id}, Amount: {self.amount}"
