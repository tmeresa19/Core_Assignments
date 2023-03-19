# import necessary Flask modules
from flask import Flask, render_template, request, redirect

from users import User  # import User class from separate module

app = Flask(__name__)  # create Flask application instance


@app.route('/')  # define route for root URL
def index():
    return redirect('/users')  # redirect to /users URL


@app.route('/users')  # define route for /users URL
def users():
    # render users.html template and pass list of all users
    return render_template("users.html", users=User.get_all())


@app.route('/user/new')  # define route for /user/new URL
def new():
    return render_template("new_user.html")  # render new_user.html template


# define route for /user/create URL and specify it only accepts POST requests
@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)  # print submitted form data to console
    User.save(request.form)  # save form data to User class
    return redirect('/users')  # redirect to /users URL


if __name__ == "__main__":
    # start Flask application in debug mode if running module directly
    app.run(debug=True)
