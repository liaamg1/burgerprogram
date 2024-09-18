#här ska vi skapa en rest api till projektet

#Grundkod för att testa att flask fungerar
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
