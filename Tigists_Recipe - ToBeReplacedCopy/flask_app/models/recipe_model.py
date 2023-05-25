from flask_app.config.mysqlconnection import connectToMySQL
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
    
    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO recipes(name, description, instructions, date_cooked, under_thirty, user_id ) "
        query += "VALUES(%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_thirty)s, %(user_id)s );"
        
        result = connectToMySQL(DATABASE).query_db(query, data)
        #INSERT doesn't throw any list. So, we won't need to send this result back.
        #But, if there's an issue with the query, we could possibly print result to see what could be wrong
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
            flash("Instructions must be at least 3 characters long.",
                "error_instructions")
            is_valid = False
        if len(data['date_cooked']) == 0:
            flash("You must provide the date cooked.", "error_date_cooked")
            is_valid = False
        if 'under_thirty' not in data:
            flash("You must provide the under thirty value.", "error_under_thirty")
            is_valid = False
        return is_valid



