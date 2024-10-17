from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# List to save the orders
orders = []

# Frontpage route for kitchen
@app.route('/')
def index():
    return render_template('index.html')

# Route to receive orders
@app.route('/receive-order', methods=['POST'])
def receive_order():
    order_data = request.json  
    burger_name = order_data.get('name') 
    special_wishes = order_data.get('wishes', '') 

    if burger_name:  
        # Append order as a dictionary containing burger name and wishes
        orders.append({'burger': burger_name, 'wishes': special_wishes})
    
    return jsonify({'message': 'Order received'}), 200  

# Route to display orders in the kitchen
@app.route('/display-orders', methods=['GET'])
def display_orders():
    return render_template('orders.html', orders=orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)