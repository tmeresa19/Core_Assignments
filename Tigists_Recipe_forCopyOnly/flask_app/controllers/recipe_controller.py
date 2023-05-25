from flask_app import app
from flask_app.models.user_model import User
from flask import render_template, session, request, redirect

@app.route ('/recipes', methods = ['GET'])
def get_recipes():
    return render_template("recipes.html")

@app.route ('/login', methods = ['POST'])
def process_login():
    #validate hashed password against plain password
    if User.validate_password ==True:
        pass
    #redirect to home storing user_id and first_name in session
    else:
        return redirect('/')