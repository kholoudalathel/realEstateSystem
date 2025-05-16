-- Create Landlords Table
CREATE TABLE IF NOT EXISTS landlords (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create Properties Table (Must belong to a landlord)
CREATE TABLE IF NOT EXISTS properties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    location VARCHAR(255) NOT NULL,
    landlord_id INT NOT NULL REFERENCES landlords(id) ON DELETE CASCADE,
    buyer_id INT REFERENCES buyers(id) ON DELETE SET NULL,
    is_sold BOOLEAN DEFAULT FALSE
);

--  Create Buyers Table
CREATE TABLE IF NOT EXISTS buyers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    budget DECIMAL(10,2) NOT NULL CHECK (budget >= 0)
);

-- Create Transactions Table (Records Purchases)
CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    buyer_id INT REFERENCES buyers(id) ON DELETE SET NULL,
    property_id INT REFERENCES properties(id) ON DELETE CASCADE,
    amount DECIMAL(10,2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
