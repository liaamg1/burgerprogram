import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="host.docker.internal",
        user="root",
        password="root",
        database="burgardatabase"
    )

def get_burgers():
    # Connect to the database
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    # Query to fetch burgers
    cursor.execute("SELECT * FROM burgers")
    burgers = cursor.fetchall()

    # Convert to list of dictionaries
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
