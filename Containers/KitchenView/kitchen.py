# kitchenView.py (running on port 5001)
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Kitchen View</h1><br><a href='/kitchenView'>View Orders</a>"

@app.route('/kitchenView', methods=['GET'])
def kitchen_view():
    try:
        # Get orders from the main app running on port 5000
        response = requests.get('http://127.0.0.1:5000/orders')
        orders = response.json()

        kitchen_page = "<h1>Kitchen View</h1>"
        if orders:
            kitchen_page += "<ul>"
            for order in orders:
                kitchen_page += f"<li>Burger: {order['burger']}, Ingredients: {', '.join(order['ingredients'])}</li>"
            kitchen_page += "</ul>"
        else:
            kitchen_page += "<p>No orders have been placed yet.</p>"
    except Exception as e:
        kitchen_page = f"<p>Error fetching orders: {e}</p>"

    kitchen_page += "<br><a href='/'>Return to Home Page</a>"
    return kitchen_page

if __name__ == '__main__':
    app.run(port=5001, debug=True)
