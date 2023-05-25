from flask_app import app
from flask_app.models.pypie_model import PyPie
from flask import render_template, session, request, redirect


@app.route('/dashboard', methods=['GET'])
def get_pypies():
    if 'user_id' in session:
        list_of_pypies = PyPie.get_all_with_user()
        return render_template("dashboard.html", list_of_pypies=list_of_pypies)
    else:
        return redirect('/')


# @app.route('/pypies/new', methods=['GET'])
# def display_pypie_form():
#     if 'user_id' in session:
#         return render_template("pypie_form.html")
#         # note that all of our GET routs will eventually require the session validation
#     else:
#         return redirect('/')


@app.route('/pypies/new', methods=['POST'])
def create_recipe():
    if PyPie.validate_pypie(request.form) == True:
        data = {
            **request.form,
            "user_id": session['user_id']
        }
        PyPie.create_one(data)
        return redirect('/dashboard')
    else:
        return redirect('/pypies/new')
    
@app.route("/pypies/edit/<int:id>", methods=["GET"])
def display_update_pypies_form(id):
    if 'user_id' in session:
        current_pypie = PyPie.get_one({"id": id})
        return render_template("update_pypie_form.html", current_pypie=current_pypie)
    else:
        return redirect('/')
    

@app.route("/pypie/update/<int:id>", methods=["POST"])
def update_pypie(id):
    if PyPie.validate_pypie(request.form) == True:
        data = {
            **request.form,
            'id': id,
            'user_id': session['user_id']
        }
        # After validating and executing the update method in the recipe_model for update_one method, then come in the controller and execute the query as:
        PyPie.update_one(data)
        return redirect('/dashboard')
    else:
        return redirect(f'/pypies/edit/{id}')


@app.route('/pies', methods=['GET'])
def get_all_pypies():
    if 'user_id' in session:
        list_of_pypies = PyPie.get_all_with_user()
        return render_template("pies.html", list_of_pypies=list_of_pypies)
    else:
        return redirect('/')
    
@app.route('/pypie/delete/<int:id>', methods=['POST'])
def delete_recipe(id):
    PyPie.delete_one({"id": id})
    return redirect('/dashboard')


@app.route("/show/<int:id>", methods=["GET"])
def display_show_pypie_form(id):
    if 'user_id' in session:
        current_pypie = PyPie.get_one({"id": id})
        return render_template("show.html", current_pypie=current_pypie)
    else:
        return redirect('/')
