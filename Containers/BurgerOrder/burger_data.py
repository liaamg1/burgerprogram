import psycopg2

#Function to get a database connection
def get_db_connection():
    return psycopg2.connect(
        host="db",
        user="postgres",  # Updated for PostgreSQL
        password="hello",
        database="burgardatabase"
    )

#Function to get burgers from the database
def get_burgers():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    # Create the burgers table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS burgers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        price NUMERIC(5, 2) NOT NULL,
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
        ('BigMacho', 'Lettuce, Bacon, BigMacho-sauce', 9.99, FALSE),
        ('McMax', 'Cheese, Bacon, lettuce', 9.95, FALSE),
        ('ChickenMc', 'Cheese, BBQ-Sauce, Bacon', 8.95, FALSE),
        ('McSkibidi', 'Cheese, Lettuce, Tomato, Mayonaise', 10.99, FALSE)
    ON CONFLICT (name) DO NOTHING;  -- Avoid duplicates on insert
    """
    cursor.execute(insert_burgers_query)

    # Fetch and return burgers
    cursor.execute("SELECT * FROM burgers")
    burgers = cursor.fetchall()

    db_connection.commit()

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