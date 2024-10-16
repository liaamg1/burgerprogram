from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Example data to store orders
orders = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive-order', methods=['POST'])
def receive_order():
    order_data = request.json
    burger_name = order_data.get('name')
    orders.append(burger_name)  # Store the order
    print(f"Order received for: {burger_name}")
    return jsonify({'message': f"Order for {burger_name} received!"})

@app.route('/get-orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
