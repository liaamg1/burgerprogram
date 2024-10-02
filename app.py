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
    page += "<p><ul>"
    
    for i in staticBurgers:
        page += "<li>" + i["name"] + "</li>"

    page += "</ul>"
    page += "<br><a href='/order'>Go to Order Menu</a>"
    return page


orders = []  # To store orders

@app.route('/')
def frontpage():
    return frontpage1()




@app.route('/ingredients/<burger_name>', methods=['GET', 'POST'])
def ingredients(burger_name):
    burger = next((b for b in staticBurgers if b["name"] == burger_name), None)
    if not burger:
        return jsonify({"message": "Burger not found"}), 404

    if request.method == 'POST':
        ingredients = request.form.getlist('ingredients')
        burger['ingredients'] = ingredients
        return jsonify({"message": "Ingredients updated successfully!", "burger": burger})

    ingredients_page = f"<h1>Ingredients for {burger_name}</h1>"
    ingredients_page += "<form method='POST'>"
    ingredients_page += "<label for='ingredients'>Select ingredients to keep:</label><br>"
    default_ingredients = ["Lettuce", "Tomato", "Onion", "Cheese", "Pickles"]
    for ingredient in default_ingredients:
        checked = "checked" if ingredient in burger.get('ingredients', default_ingredients) else ""
        ingredients_page += f"<input type='checkbox' name='ingredients' value='{ingredient}' {checked}>{ingredient}<br>"
    ingredients_page += "<input type='submit' value='Update Ingredients'>"
    ingredients_page += "</form>"
    ingredients_page += "<br><a href='/'>Return to Home Page</a>"
    ingredients_page += "<br><a href='/order'>Go to Order Menu</a>"
    return ingredients_page

# Update the order route to include a link to the ingredients page
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        burger_name = request.form.get('burger')
        ingredients_to_remove = request.form.get('ingredients').split(',')
        burger = next((b for b in staticBurgers if b["name"] == burger_name), None)
        if burger:
            current_ingredients = burger.get('ingredients', ["Lettuce", "Tomato", "Onion", "Cheese", "Pickles"])
            updated_ingredients = [ingredient for ingredient in current_ingredients if ingredient not in ingredients_to_remove]
            order = {"burger": burger_name, "ingredients": updated_ingredients}
            orders.append(order)
            return jsonify({"message": "Order placed successfully!", "order": order})

    order_page = "<h1>Order Menu</h1>"
    order_page += "<form method='POST'>"
    order_page += "<label for='burger'>Choose your burger:</label><br>"
    for burger in staticBurgers:
        order_page += f"<input type='radio' name='burger' value='{burger['name']}' onclick='showIngredients(\"{burger['name']}\")'>{burger['name']}<br>"
        if 'ingredients' in burger:
            order_page += f"Ingredients: {', '.join(burger['ingredients'])}<br>"
    order_page += "<div id='ingredientsList'></div>"
    order_page += "<label for='ingredients'>Remove ingredients (comma separated):</label><br>"
    order_page += "<input type='text' name='ingredients'><br>"
    order_page += "<input type='submit' value='Order'>"
    order_page += "</form>"
    order_page += "<br><a href='/'>Return to Home Page</a>"
    order_page += """
    <script>
        function showIngredients(burgerName) {
            var ingredients = {
                "BigMacho": ["Lettuce", "Tomato", "Onion", "Cheese", "Pickles"],
                "McMax": ["Lettuce", "Tomato", "Onion", "Cheese", "Pickles"],
                "ChickenMc": ["Lettuce", "Tomato", "Onion", "Cheese", "Pickles"],
                "McSkibidi": ["Lettuce", "Tomato", "Onion", "Cheese", "Pickles"]
            };
            var ingredientsList = ingredients[burgerName];
            var ingredientsDiv = document.getElementById('ingredientsList');
            ingredientsDiv.innerHTML = "<p>Ingredients: " + ingredientsList.join(', ') + "</p>";
        }
    </script>
    """
    return order_page





if __name__ == '__main__':
    app.run(debug=True)
    

