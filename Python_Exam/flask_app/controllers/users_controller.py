from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.users_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt( app )


@app.route('/', methods=['GET'])
@app.route('/login', methods=['GET'])
@app.route('/registration', methods=['GET'])
def get_login_registration():
    return render_template("login_reg.html")


@app.route( '/user/new', methods=["POST"] )
def create_user():
    if User.validate_registration( request.form ) == True:
        encrypted_password = User.encrypt_password( request.form['password'], bcrypt )
        new_user = {
            **request.form,
            "password" : encrypted_password
        }
        user_id = User.create_one( new_user )
        session[ 'full_name' ] = f"{request.form['first_name']} {request.form['last_name']}" 
        session[ 'user_id' ] = user_id
        return redirect( "/recipes" )
    else:
        return redirect( "/" ) 
    
    
@app.route( '/login', methods=['POST'] )
def user_login():
    login_user = {
        "email" : request.form["email_login"]
    }
    current_user = User.get_one( login_user )
    if current_user != None:
        if User.validate_password( request.form["password_login"], current_user.password, bcrypt ) == True:
            session[ 'full_name' ] = f"{current_user.first_name} {current_user.last_name}" 
            session[ 'user_id' ] = current_user.id
            return redirect( "/recipes" )
        else:
            return redirect( "/" )
    else:
        return redirect( "/" )
    
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")
