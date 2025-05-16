class Property:
    def __init__(self, property_id, address, price, landlord_id):
        self.property_id = property_id
        self.address = address
        self.price = price
        self.landlord_id = landlord_id

    def get_details(self):
        return f"Property ID: {self.property_id}, Address: {self.address}, Price: {self.price}, Landlord ID: {self.landlord_id}"

