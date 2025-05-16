from enum import Enum

class DatabaseType(Enum):
    POSTGRESQL = "postgresql"
    MONGODB = "mongodb"

class PropertyStatus(Enum):
    AVAILABLE = "Available"
    SOLD = "Sold"