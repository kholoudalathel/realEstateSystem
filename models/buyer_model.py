from models.person_model import Person


class Buyer(Person):
    def __init__(self, buyer_id, name, email):
        super().__init__(name, email)
        self.buyer_id = buyer_id

    def get_details(self):
        return f"Buyer ID: {self.buyer_id}, Name: {self.name}, Email: {self.contact}"
