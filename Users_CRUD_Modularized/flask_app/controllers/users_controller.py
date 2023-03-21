from flask import render_template, request, redirect, session
from flask_app.models.users_model import User
from flask_app import app


@app.route('/')
def index():
    return redirect('/users')

# Route to display all users


@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all())

# Route to display form for creating a new user


@app.route('/user/new')
def new():
    return render_template("new_user.html")

# Route to create a new user


@app.route('/user/create', methods=['POST'])
def create():

    User.save(request.form)
    return redirect('/users')

# Route to display form for editing a user


@app.route('/user/edit/<int:id>')
def edit(id):

    data = {"id": id}
    return render_template("edit_user.html", user=User.get_one(data))

# Route to display information about a specific user


@app.route('/user/show/<int:id>')
def show(id):

    data = {"id": id}
    return render_template("show_user.html", user=User.get_one(data))

# Route to update a user's information


@app.route('/user/update', methods=['POST'])
def update():

    User.update(request.form)
    return redirect('/users')

# Route to delete a user


@app.route('/user/destroy/<int:id>')
def destroy(id):

    data = {"id": id}
    User.destroy(data)
    return redirect('/users')
