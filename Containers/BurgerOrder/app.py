from flask import Flask, render_template, request, jsonify
from burger_data import get_burgers
import requests  # Import requests for sending the order to kitchen.py

app = Flask(__name__)

@app.route('/')
def frontpage():
    return render_template('index.html')

@app.route('/order', methods=['GET'])
def display_burgers():
    burgers = get_burgers()  # Get the list of burgers
    return render_template('burgers.html', burgers=burgers)

@app.route('/send-order', methods=['POST'])
def send_order():
    burger_name = request.args.get('name')

    # Send the order to kitchen.py (assuming it's running at port 5001)
    response = requests.get('http://localhost:5001/receive-order', params={'name': burger_name})

    return jsonify({'message': response.json().get('message')}), response.status_code

@app.route('/order_confirmation', methods=['GET'])
def order_confirmation():
    return render_template("orderconfirmation.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
