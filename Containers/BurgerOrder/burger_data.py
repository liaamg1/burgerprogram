import mysql.connector

# Function to get a database connection
def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="hello",
        database="burgardatabase"
    )

# Function to get burgers from the database
def get_burgers():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM burgers")
    burgers = cursor.fetchall()

    burger_list = []
    for burger in burgers:
        id, name, description, price, is_vegetarian = burger
        burger_list.append({
            'id': id,
            'name': name,
            'description': description,
            'price': price,
            'is_vegetarian': is_vegetarian
        })

    cursor.close()
    db_connection.close()

    return burger_list
