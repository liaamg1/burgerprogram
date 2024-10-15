from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive-order', methods=['GET'])  # Ensure POST method is specified
def receive_order():
    order_data = request.json
    burger_name = order_data.get('name')
    print(f"Order received for: {burger_name}")
    return jsonify({'message': f"Order for {burger_name} received!"})

if __name__ == '__main__':
    app.run(port=5001)
