# Databasen som används i projektet
# Vi kommer behöva koppla denna databas till vårt projekt till main filen
# Vi kan också använda oss av json filer för att spara data istället för en SQL databas

import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="burgardatabase"
)

cursor = db_connection.cursor()

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

insert_burgers_query = """
INSERT INTO burgers (name, description, price, is_vegetarian)
VALUES
    ('BigMacho', 'The biggest burger in town', 9.99, FALSE),
    ('McMax', 'The most popular burger', 9.95, FALSE),
    ('ChickenMc', 'The best chicken burger', 8.95, FALSE),
    ('McSkibidi', 'The most unique Skibidi burger in town', 10.99, FALSE);
"""

cursor.execute(insert_burgers_query)

cursor.execute("SELECT * FROM burgers")
burgers = cursor.fetchall()

for burger in burgers:
    print(burger)

db_connection.commit()

cursor.close()
db_connection.close()
