from flask_app import app
from flask_app.models.recipe_model import Recipe
from flask import render_template, session, request, redirect

@app.route ('/recipes', methods = ['GET'])
def get_recipes():
    return render_template("recipes.html")

@app.route ('/recipes/new', methods = ['GET'])
def display_recipe_form():
    return render_template ("recipe_form.html")
    #note that all of our GET routs will eventually require the session validation 
    
@app.route('/recipe/new/', methods = ['POST'])
def create_recipe():
    if Recipe.validate_recipe(request.form) == True:
        data = {
            **request.form,
            "user_id" : session['user_id']
        } 
        Recipe.create_one(data)
        return redirect('/recipes')
    else:
        return redirect('/recipes/new')
