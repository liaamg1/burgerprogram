from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

received_orders = []

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/kitchenView', methods=['GET'])
def kitchen_view():
    conn = get_db_connection()
    orders = conn.execute('SELECT * FROM orders').fetchall()
    conn.close()

    kitchen_page = "<h1>Kitchen View</h1>"
    kitchen_page += "<ul>"
    for order in orders:
        kitchen_page += f"<li>Burger: {order['burger_name']}, Ingredients: {order['ingredients']}</li>"
    kitchen_page += "</ul>"
    kitchen_page += "<br><a href='/'>Return to Home Page</a>"
    return kitchen_page

if __name__ == '__main__':
    app.run(port=5001)