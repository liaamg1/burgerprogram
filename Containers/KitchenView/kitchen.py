from flask import Flask, jsonify, request


app = Flask(__name__)

received_orders = []

def receive_order():
    order = request.json

    if not order or 'burger' not in order or 'ingredients' not in order:
        return jsonify({"message": "Invalid order format"}), 400

    Received_orders.append(order)

    print("\nNew Order Received!")
    print(f"Burger: {order['burger']}")
    print(f"Ingredients: {', '.join(order['ingredients'])}")
    print("-" * 30)

    return jsonify({"message": "Order received successfully!"}), 200

def view_orders():
        return jsonify(received_orders)


if __name__ == '__main__':
    app.run(port=5001)