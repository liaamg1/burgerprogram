# kitchenView.py (running on port 5001)
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Kitchen View</h1><br><a href='/kitchenView'>View Orders</a>"

@app.route('/orders', methods=['POST'])
def orders():
    pass
if __name__ == '__main__':
    app.run(port=5001, debug=True)
