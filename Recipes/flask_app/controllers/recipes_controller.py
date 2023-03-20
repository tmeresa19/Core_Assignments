from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.recipes_model import Recipe


@app.route( '/recipes', methods=['GET'])
def get_all_recipes():
     list_of_recipes = Recipe.get_all()
     return render_template("home_recipes.html", list_of_recipes=list_of_recipes)

@app.route('/recipe/new', methods=['GET'])
def display_recipe_form():
     if 'full_name' in session:
          current_user=session['full_name']
          return render_template("recipe_form.html")
     else:
          return redirect("/recipes")


@app.route('/recipe/new', methods=['POST'])
def create_recipe():
     new_recipe = {
          "name": request.form['recipe_name'],
          "description": request.form['recipe_description'],
          "instructions": request.form['recipe_instructions'],
          "user_id": session['user_id']
     }
     print(new_recipe)
     Recipe.create_one(new_recipe)
     
     return redirect('/recipes')


@app.route('/recipe/<int:id>', methods=['GET'])
def display_recipe_view(id):
     recipe = {
          "id": id
     }
     
     current_recipe = Recipe.get_one(recipe)
     
     if 'full_name' in session:
          current_user = session['full_name']
     return render_template("view_recipe.html", current_user=current_user, current_recipe=current_recipe)


@app.route('/recipe/edit/<int:id>', methods=['GET'])
def display_edit_recipe(id):
     recipe = {
          "id": id
     }
     current_recipe = Recipe.get_one(recipe)
     return render_template("edit_recipe.html", current_recipe=current_recipe)


@app.route('/recipe/edit/<int:id>', methods=['POST'])
def edit_recipe(id):
     display_edit_recipe = {
          "name": request.form['recipe_name'],
          "description": request.form['recipe_description'],
          "instructions": request.form['recipe_instructions'],
          "user_id": session['user_id'],
          "id": id
     }
     print(display_edit_recipe)
     Recipe.update_one(display_edit_recipe)
     return redirect('/recipes')




"""
Method: GET
Getting all of a particular list
Function: get_all_todos()
          get_todos()
Url: '/todos'

Method: GET
Getting one item of a particular list
Function: get_todo_by_id( id )
          get_todo( id )
Url: '/todo/<int:todo_id>'
     '/todo/<int:id>'

Method: GET
Displaying a form that will eventually refer to a list
Function: display_todo_form()
Url: '/todo/form'

Method: POST
Create a new item of a particular list
Function: create_todo()
          add_todo()
Url: '/todo/new'
     '/todo/add'

Method: POST/PUT
Update an existing item of a particular list
Function: update_todo( id )
          edit_todo( id )
Url: '/todo/update'
     '/todo/edit'

Method: POST/DELETE
Remove an existing item from a particular list
Function: delete_todo( id )
          remove_todo( id )
Url: '/todo/delete'
     '/todo/remove'
"""
