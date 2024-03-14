from .. import app
from flask import render_template

@app.route("/pizzeria/nizzita")
def app3():
    context = {
        1: "Win",
        2: "Loss",
    }
    return render_template("for_loop.html", context=context)

@app.route("/pizzeria/nizzita/menu")
def index():
    menu = {
        "Salami" : "Ingridients : salami,tomato sauce,cheese. Price : 10 euro",

        "Margaritha" : "Ingridients : tomato sauce,cheese,tomatoes. Price : 8 euro",
        
        "Doner Pizza" : "Ingridients : garlic sauce,spicy chicken,onions,mozzarella. Price : 13 euro",
        
       "Cheeseburger Pizza" : "Ingridients : beef,tomato sauce,tomatoes,pickled cucumbers,onions,burger sauce,mozzarella. Price : 12 euro",
        
    }
    return render_template("_menu.html", context=menu) 
