from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# list to save the orders
orders = []


# frontpage route for kitchen
@app.route('/')
def index():
    return render_template('index.html')


# route to receive orders
@app.route('/receive-order', methods=['POST'])
def receive_order():
    order_data = request.json  
    burger_name = order_data.get('name') 
    ingredients = order_data.get('ingredients', []) 
    if burger_name:  
        order_details = f"{burger_name} with ingredients: {', '.join(ingredients)}"
        orders.append(burger_name)  
    return jsonify({'message': 'Order received'}), 200  # A simple response


# route to display orders in the kitchen
@app.route('/display-orders', methods=['GET'])
def display_orders():
    return render_template('orders.html', orders=orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
