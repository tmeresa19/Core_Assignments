from flask_app import app
from flask_app.models.user_model import User 
from flask import render_template, session, request, redirect
from flask_bcrypt import Bcrypt 

bcrypt = Bcrypt(app)

@app.route ('/', methods = ['GET'])
def display_login_registration_form():
    return render_template ("login_registration.html")

@app.route('/user/new', methods = ['POST'])
def create_user():
    #Validate the fields (since this is a POST)
    if User.validate_registration(request.form):
        #encrypt password
        encrypted_password = User.encrypt_password(request.form["password"], bcrypt)
        # validate if email already exists! (done in the user_model)
        if User.get_one_by_email({"email": request.form['email']}, "registration") == True:
            #that means, email doesn't exist in the db
            data = {
            **request.form,
            "password" : encrypted_password
        }
            # Execute the methods holding the query
            user_id = User.create_one(data)
            session['user_id']= user_id
            session['first_name'] = request.form['first_name']
            return redirect('/recipes')
        else:
            return redirect('/')
    else:
        return redirect ('/')    

@app.route('/login', methods=['POST'])
def process_login():
    #Do the query to grab the current user's encrypted password
    current_user = User.get_one_by_email({"email": request.form["email_login"]}, "login")
    #Validate hashed password against plain password
    if current_user:
        if User.validate_password(request.form["password_login"], current_user.password, bcrypt) == True:
            #redirect to home storing user_id and first_name in session
            session['user_id'] = current_user.id
            session['first_name'] = current_user.first_name
            return redirect('/recipes')
            #Redirect to home storing user_id and first_name in session
        else:
            return redirect("/")
    else:
        return redirect("/")















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
