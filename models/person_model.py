from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    @abstractmethod
    def get_details(self):
        pass