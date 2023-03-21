from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import users_model


class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_cooked = data["date_cooked"]
        # self.created_at = data["created_at"]
        # self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user_list = []


    @classmethod
    def get_all(cls):
        query = "SELECT * "
        query += "FROM recipes;"
        # In a SELECT we always get a LIST of DICTIONARIES
        results = connectToMySQL(DATABASE).query_db(query)

        list_of_recipes = []
        for row in results:
            list_of_recipes.append(cls(row))
        return list_of_recipes

    @classmethod
    def create_one( cls, data ):
        query  = "INSERT INTO recipes( name, description, instructions, date_cooked, user_id ) "
        query += "VALUES( %(name)s, %(description)s , %(instructions)s, %(date_cooked)s, %(user_id)s );"

        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result

    @classmethod
    def get_one( cls, data ):
        query  = "SELECT * "
        query += "FROM recipes "
        query += "WHERE id = %(id)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )
        current_recipe = cls( result[0] )
        return current_recipe
    
    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes "
        query += "SET name = %(recipe_name)s, description = %(recipe_description)s, instructions = %(recipe_instructions)s, user_id = %(user_id)s "
        query += "WHERE id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query, data)
        if result == None:
            return "Success"
        else:
            return "Something went wrong, look at the terminal logs!"
        
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes "
        query += "WHERE id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query, data)
        if result == None:
            return "Success"
        else:
            return "Something went wrong, look at the terminal logs!"
