from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

# Route to redirect to the '/users' page


@app.route('/')
def index():
    return redirect('/users')

# Route to display all users


@app.route('/users')
def users():
    # Call the get_all method from the User class to retrieve all users
    # and pass them to the 'users.html' template
    return render_template("users.html", users=User.get_all())

# Route to display form for creating a new user


@app.route('/user/new')
def new():
    # Render the 'new_user.html' template to display a form for creating a new user
    return render_template("new_user.html")

# Route to create a new user


@app.route('/user/create', methods=['POST'])
def create():
    # Call the save method from the User class to save the new user data
    # which was submitted using a form and then redirect to the 'users' route
    User.save(request.form)
    return redirect('/users')

# Route to display form for editing a user


@app.route('/user/edit/<int:id>')
def edit(id):
    # Call the get_one method from the User class to retrieve the user data
    # corresponding to the given 'id' and pass it to the 'edit_user.html' template
    data = {"id": id}
    return render_template("edit_user.html", user=User.get_one(data))

# Route to display information about a specific user


@app.route('/user/show/<int:id>')
def show(id):
    # Call the get_one method from the User class to retrieve the user data
    # corresponding to the given 'id' and pass it to the 'show_user.html' template
    data = {"id": id}
    return render_template("show_user.html", user=User.get_one(data))

# Route to update a user's information


@app.route('/user/update', methods=['POST'])
def update():
    # Call the update method from the User class to update the user data
    # which was submitted using a form and then redirect to the 'users' route
    User.update(request.form)
    return redirect('/users')

# Route to delete a user


@app.route('/user/destroy/<int:id>')
def destroy(id):
    # Call the destroy method from the User class to delete the user data
    # corresponding to the given 'id' and then redirect to the 'users' route
    data = {"id": id}
    User.destroy(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
