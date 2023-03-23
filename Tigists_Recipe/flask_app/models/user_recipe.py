

from flask_app.models.user_recipe import UserRecipe
class UserRecipe:
    
#  define the attributes "id", "user_id", and "recipe_id".
    
    recipes[]
    
    def get_recipes()
    # this will query the database for all the recipes associated with the user.

    
    users[]
    
    def get_users()
    # will query the database for all the users associated with the recipe.
    
    create_one

    # Here are the steps you can follow to update the models:

    # Create a new file called "user_recipe.py" in your "models" directory. This file will contain the definition of the UserRecipe class .

    # In the User model, add a new attribute called "recipes" which is a list that will contain all the recipes associated with that user. Also, add a new method called "get_recipes" that will query the database for all the recipes associated with the user.

    # In the Recipe model, add a new attribute called "users" which is a list that will contain all the users associated with that recipe. Also, add a new method called "get_users" that will query the database for all the users associated with the recipe.

    # In the UserRecipe class , define the attributes "id", "user_id", and "recipe_id". "id" will be the primary key of the table, "user_id" will be a foreign key referencing the User table, and "recipe_id" will be a foreign key referencing the Recipe table.

    # In the UserRecipe class , define a method called "create_one" that will insert a new row into the "user_recipe" table.

    # In the User model, update the "create_one" method to also insert a row into the "user_recipe" table, linking the new user to any recipes they created.

    # In the Recipe model, update the "create_one" method to also insert a row into the "user_recipe" table, linking the new recipe to the user who created it.

    # In the User model, update the "get_all_with_user" method to also fetch all the recipes associated with each user, using the new "get_recipes" method.

    # In the Recipe model, update the "get_all_with_user" method to also fetch all the users associated with each recipe, using the new "get_users" method.
    
    
    # =================Steps to implement Many-to-Many Relationship============================
    
    # 1. implementation of the UserRecipe class:
    from flask_app.config.mysqlconnection import connectToMySQL


class UserRecipe:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.recipe_id = data['recipe_id']

    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO user_recipe (user_id, recipe_id) VALUES (%(user_id)s, %(recipe_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # 2. updated implementation of the User model:

    from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @classmethod
    def get_one_by_email(cls, data, option):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if len(result) > 0:
            if option == "registration":
                flash("Email already in use,

    #  3. Updated Recipe Model?
    
    class Recipe:
    def __init__(self, data):
    self.id=data['id']
    self.name=data['name']
    self.description=data['description']
    self.instructions=data['instructions']
    self.date_cooked=data['date_cooked']
    self.under_thirty=data['under_thirty']
    self.created_at=data['created_at']
    self.updated_at=data['updated_at']
    self.user_id=data['user_id']
    self.owner=None
    self.users_who_favorited=[]

    @ classmethod
    def create_one(cls, data):
    query="INSERT INTO recipes(name, description, instructions, date_cooked, under_thirty, user_id ) "
    query += "VALUES(%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_thirty)s, %(user_id)s );"
    result=connectToMySQL(DATABASE).query_db(query, data)
    return result

    @ classmethod
    def get_all_with_user(cls):
    query="SELECT * "
    query += "FROM recipes r "
    query += "JOIN users u ON r.user_id = u.id;"
    results=connectToMySQL(DATABASE).query_db(query)
    list_of_recipes=[]
    for row in results:
    current_recipe=cls(row)
    data_for_user={
        "id": row['u.id'],
        "first_name": row['first_name'],
        "last_name": row['last_name'],
        "email": row['email'],
        "created_at": row['created_at'],
        "updated_at": row['updated_at'],
        "password": row['password']
    }
    current_recipe.owner=User(data_for_user)
    list_of_recipes.append(current_recipe)
    return list_of_recipes

    @ classmethod
    def get_all_favorites_for_user(cls, user_id):
    query="SELECT r.* "
    query += "FROM recipes r "
    query += "JOIN favorites f ON r.id = f.recipe_id "
    query += "WHERE f.user_id = %(user_id)s;"
    data={"user_id": user_id}
    results=connectToMySQL(DATABASE).query_db(query, data)
    list_of_recipes=[]
    for row in results:
    current_recipe=cls(row)
    list_of_recipes.append(current_recipe)
    return list_of_recipes

    @ classmethod
    def get_one_by_id(cls, data):
    query="SELECT * FROM recipes WHERE id = %(id)s"
    result=connectToMySQL(DATABASE).query_db(query, data)
    if len(result) == 0:
    return False
    else:
    return cls(result[0])

    @ classmethod
    def update_one(cls, data):
    query="UPDATE recipes SET "
    query += "name=%(name)s, "
    query += "description=%(description)s, "
    query += "instructions=%(instructions)s, "
    query += "date_cooked=%(date_cooked)s, "
    query += "under_thirty=%(under_thirty)s "
    query += "WHERE id=%(id)s;"
    result=connectToMySQL(DATABASE).query_db(query, data)
    return result

    @ classmethod
    def delete_one(cls, data):
    query="DELETE FROM recipes WHERE id = %(id)s;"
    result=connectToMySQL(DATABASE).query_db(query, data)
    return result

    @ staticmethod
    def validate_recipe(data):


    
