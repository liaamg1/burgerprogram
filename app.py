#här ska vi skapa en rest api till projektet

#Grundkod för att testa att flask fungerar
from flask import Flask, jsonify, request

staticBurgers= [{"name":"BigMacho"},
                {"name":"McMax"},
                {"name":"ChickenMc"},
                {"name":"McSkibidi"}]


app = Flask(__name__)
def frontpage1():
    page = "<h1>Welcome to DonaldsMax</h1>"
    page += "<P><UL>"
    
    for i in staticBurgers:
        page += "<LI>" + i["name"]

    page += "</UL>"
    return page


orders = []  # To store orders
@app.route('/')
def frontpage():
    return frontpage1()

if __name__ == '__main__':
    app.run(debug=True)

