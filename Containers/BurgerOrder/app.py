from flask import Flask, jsonify, request, redirect
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('database.sql')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database and add static burgers
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create table for burgers
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS burgers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL
    )
    ''')

    # Create table for orders
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        burger_name TEXT NOT NULL,
        ingredients TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

# Add static burgers to the database
def init_burgers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM burgers')  # Clear existing burgers for testing
    burgers = [
        {"name": "BigMacho", "ingredients": "Meat,Lettuce,Tomato,Onion,Cheese,Pickles,Ketchup,Mustard,Mayonnaise"},
        {"name": "McMax", "ingredients": "Meat,Lettuce,Tomato,Onion,Cheese,Pickles,Ketchup,Mustard,Mayonnaise"},
        {"name": "ChickenMc", "ingredients": "Meat,Lettuce,Tomato,Onion,Cheese,Pickles,Ketchup,Mustard,Mayonnaise"},
        {"name": "McSkibidi", "ingredients": "Meat,Lettuce,Tomato,Onion,Cheese,Pickles,Ketchup,Mustard,Mayonnaise"}
    ]
    for burger in burgers:
        cursor.execute('INSERT INTO burgers (name, ingredients) VALUES (?, ?)', (burger['name'], burger['ingredients']))
    conn.commit()
    conn.close()

# Call this function to initialize the database and burgers
init_db()
init_burgers()

# Frontpage route
@app.route('/')
def frontpage():
    conn = get_db_connection()
    burgers = conn.execute('SELECT * FROM burgers').fetchall()
    conn.close()

    page = "<h1>Welcome to DonaldsMax</h1>"
    page += "<p><ul>"
    for burger in burgers:
        page += f"<li>{burger['name']}</li>"
    page += "</ul>"
    page += "<br><a href='/order'>Go to Order Menu</a>"
    return page

# Ingredients route to get or update a burger's ingredients
@app.route('/ingredients/<burger_name>', methods=['GET', 'POST'])
def ingredients(burger_name):
    conn = get_db_connection()
    burger = conn.execute('SELECT * FROM burgers WHERE name = ?', (burger_name,)).fetchone()
    if not burger:
        return jsonify({"message": "Burger not found"}), 404

    if request.method == 'POST':
        ingredients1 = request.form.getlist('ingredients')
        ingredients_str = ','.join(ingredients1)
        conn.execute('UPDATE burgers SET ingredients = ? WHERE name = ?', (ingredients_str, burger_name))
        conn.commit()
        conn.close()
        return jsonify({"message": "Ingredients updated successfully!", "burger": {"name": burger_name, "ingredients": ingredients1}})

    default_ingredients = burger['ingredients'].split(',')

    ingredients_page = f"<h1>Ingredients for {burger_name}</h1>"
    ingredients_page += "<form method='POST'>"
    ingredients_page += "<label for='ingredients'>Select ingredients to keep:</label><br>"
    for ingredient in default_ingredients:
        checked = "checked" if ingredient in default_ingredients else ""
        ingredients_page += f"<input type='checkbox' name='ingredients' value='{ingredient}' {checked}>{ingredient}<br>"
    ingredients_page += "<input type='submit' value='Update Ingredients'>"
    ingredients_page += "</form>"
    ingredients_page += "<br><a href='/'>Return to Home Page</a>"
    ingredients_page += "<br><a href='/order'>Go to Order Menu</a>"
    return ingredients_page

# Order route to place an order
@app.route('/order', methods=['GET', 'POST'])
def order():
    conn = get_db_connection()
    burgers = conn.execute('SELECT * FROM burgers').fetchall()

    if request.method == 'POST':
        burger_name = request.form.get('burger')
        ingredients_to_remove = request.form.get('ingredients').split(',')
        burger = conn.execute('SELECT * FROM burgers WHERE name = ?', (burger_name,)).fetchone()

        if burger:
            current_ingredients = burger['ingredients'].split(',')
            updated_ingredients = [ingredient for ingredient in current_ingredients if ingredient not in ingredients_to_remove]
            conn.execute('INSERT INTO orders (burger_name, ingredients) VALUES (?, ?)', (burger_name, ','.join(updated_ingredients)))
            conn.commit()
            conn.close()
            return redirect('/order_confirmation')

    order_page = "<h1>Order Menu</h1>"
    order_page += "<form method='POST'>"
    order_page += "<label for='burger'>Choose your burger:</label><br>"
    for burger in burgers:
        order_page += f"<input type='radio' name='burger' value='{burger['name']}'>{burger['name']}<br>"
        order_page += f"Ingredients: {burger['ingredients']}<br>"
    order_page += "<label for='ingredients'>Remove ingredients (comma separated without spaces):</label><br>"
    order_page += "<input type='text' name='ingredients'><br>"
    order_page += "<input type='submit' value='Order'>"
    order_page += "</form>"
    order_page += "<br><a href='/'>Return to Home Page</a>"
    return order_page

# Order confirmation page after placing an order
@app.route('/order_confirmation', methods=['GET'])
def order_confirmation():
    return "<h1>Order placed successfully!</h1><br><a href='/'>Return to Home Page</a><br><a href='/order'>Place another order</a>"

# Run the app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
