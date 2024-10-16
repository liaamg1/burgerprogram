from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Example data to store orders
orders = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive-order', methods=['POST'])
def receive_order():
    order_data = request.json  # Capture the incoming data
    burger_name = order_data.get('name')  # Extract the burger name
    if burger_name:  # Check if burger_name is not None
        orders.append(burger_name)  # Store the order
    return jsonify({'message': 'Order received'}), 200  # A simple response

@app.route('/get-orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/display-orders', methods=['GET'])
def display_orders():
    return render_template('orders.html', orders=orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
