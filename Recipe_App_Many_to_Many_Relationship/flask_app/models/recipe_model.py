from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask_app import DATABASE, EMAIL_REGEX
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.owner = None
        #self.owner is not a list, but just one single user. That means, the user who created the recipe 
        
        #1. self.users_who_favorited = []
        self.users_who_favorited = []
        
    # 2. In the Recipe model, add a new attribute called "users" which is a list that will contain all the users associated with that recipe. 
    
    # 3. Also, add a new method called "get_users" that will query the database for all the users associated with the recipe. 
    
    @classmethod
    def get_one (cls, data):
        query = "SELECT * "
        query += "FROM recipes "
        query += "WHERE recipes.id = %(id)s; "
        
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])
    
    # 4. In the Recipe model, update the "create_one" method to also insert a row into the "user_recipe" table, linking the new recipe to the user who created it.
    
    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO recipes(name, description, instructions, date_cooked, under_thirty, user_id ) "
        query += "VALUES(%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_thirty)s, %(user_id)s );"
        
        result = connectToMySQL(DATABASE).query_db(query, data )
        #INSERT doesn't throw any list. So, we won't need to send this result back.
        #But, if there's an issue with the query, we could possibly print result to see what could be wrong
        print(result)
        return result
    
    # 5. In the Recipe model, update the "get_all_with_user" method to also fetch all the users associated with each recipe, using the new "get_users" method.
    
    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * "
        query += "FROM recipes r "
        query += "JOIN users u ON r.user_id = u.id;"    
        
        #to execute the above query
        results = connectToMySQL( DATABASE ).query_db (query)
        list_of_recipes = []
        
        for row in results:
            current_recipe = cls(row)
            data_for_user = {
                "id" : row['u.id'],
                "first_name" : row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "password": row['password']
            }
            current_recipe.owner = User (data_for_user)
            list_of_recipes.append(current_recipe)
        return list_of_recipes 
    
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes "
        query += "WHERE id = %(id)s; "
        
        result = connectToMySQL (DATABASE ).query_db(query, data)
        # print (result)
        return result
    
    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes "
        query += "SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s, under_thirty = %(under_thirty)s, user_id = %(user_id)s "
        query += "WHERE id=%(id)s;"
        
        # before executing the query, need to validate (which is in the controller) then come here and execute the query as:
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
        
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len( data['name']) < 3:
            flash("Name must be at least 3 characters long.", "error_name")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters long.", "error_description")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters long.", "error_instructions")
            is_valid = False
        if len(data['date_cooked']) == 0:
            flash("You must provide the date cooked.", "error_date_cooked")
            is_valid = False
        if 'under_thirty' not in data:
            flash("You must provide the under thirty value.", "error_under_thirty")
            is_valid = False
        return is_valid
    
    



