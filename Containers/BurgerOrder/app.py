from flask import Flask, jsonify, request, render_template
from burger_data import get_burgers, display_burgers

app = Flask(__name__)
# Introduktion
@app.route('/')
def frontpage():
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def display_burgers():
    burgers = get_burgers()
    return render_template('burgers.html',burger=burgers)

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
