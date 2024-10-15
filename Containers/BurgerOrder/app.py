from flask import Flask, jsonify, request, render_template
from burger_data import get_burgers

app = Flask(__name__)
@app.route('/')
def frontpage():
    pass
@app.route('/order', methods=['GET', 'POST'])
def order():
    pass


# Order confirmation page after placing an order
@app.route('/order_confirmation', methods=['GET'])
def order_confirmation():
    return render_template("orderconfirmation.html")

#Create custom error messages:

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Run the app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
