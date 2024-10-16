import mysql.connector

db_connection = mysql.connector.connect(
    host="host.docker.internal",
    user="root",
    password="root",
    database="burgardatabase"
)

cursor = db_connection.cursor()

# Create the burgers table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS burgers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(5,2) NOT NULL,
    is_vegetarian BOOLEAN DEFAULT FALSE
);
"""
cursor.execute(create_table_query)

# Clear existing burgers to ensure only four specific ones are present
cursor.execute("DELETE FROM burgers")

# Insert predefined burgers
insert_burgers_query = """
INSERT INTO burgers (name, description, price, is_vegetarian)
VALUES
    ('BigMacho', 'The biggest burger in town', 9.99, FALSE),
    ('McMax', 'The most popular burger', 9.95, FALSE),
    ('ChickenMc', 'The best chicken burger', 8.95, FALSE),
    ('McSkibidi', 'The most unique Skibidi burger in town', 10.99, FALSE);
"""
cursor.execute(insert_burgers_query)

# Fetch and display burgers
cursor.execute("SELECT * FROM burgers")
burgers = cursor.fetchall()

db_connection.commit()

for burger in burgers:
    print(burger)

cursor.close()
db_connection.close()
