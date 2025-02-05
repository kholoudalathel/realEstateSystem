from models.person_model import Person


class Landlord(Person):
    def __init__(self, landlord_id, name, phone):
        super().__init__(name, phone)
        self.landlord_id = landlord_id

    def get_details(self):
        return f"Landlord ID: {self.landlord_id}, Name: {self.name}, Phone: {self.contact}"