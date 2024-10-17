from flask import Flask, render_template, request, jsonify
from burger_data import get_burgers
import requests

app = Flask(__name__)

# Frontpage route
@app.route('/')
def frontpage():
    return render_template('index.html')

# Displays the burgers
@app.route('/order', methods=['GET'])
def display_burgers():
    burgers = get_burgers()
    return render_template('burgers.html', burgers=burgers)

# Example data to store orders
@app.route('/send-order', methods=['POST'])
def send_order():
    order_data = request.get_json()
    burger_name = order_data.get('name')
    special_wishes = order_data.get('wishes')  # Get special wishes

    response = requests.post('http://kitchenview:5001/receive-order', json={
        'name': burger_name,
        'wishes': special_wishes  # Send special wishes to kitchen view
    })

    return jsonify(response.json()), response.status_code

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Error handling
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True) 