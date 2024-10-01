#här ska vi skapa en rest api till projektet

#Grundkod för att testa att flask fungerar
from flask import Flask, jsonify, request

app = Flask(__name__)

burgers = [
    {"id": 1, "name": "Cheeseburger", "price": 5.99, "description": "A delicious cheeseburger."},
    {"id": 2, "name": "Bacon Burger", "price": 6.99, "description": "A juicy burger topped with crispy bacon."},
    {"id": 3, "name": "Veggie Burger", "price": 4.99, "description": "A hearty veggie burger."}
]

orders = []  # To store orders

@app.route('/api/burgers', methods=['GET'])
def get_burgers():
    return jsonify(burgers)

if __name__ == '__main__':
    app.run(debug=True)

