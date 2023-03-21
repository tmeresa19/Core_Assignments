from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, EMAIL_REGEX
from flask_app.models import recipes_model
from flask import flash


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        # self.created_at = data["created_at"]
        # self.updated_at = data["updated_at"]
        self.email = data["email"]
        self.password = data["password"]
        self.recipe_list = []

    @classmethod
    def get_one_with_recipes(cls, data):
        query = "SELECT * "
        query += "FROM users u "
        query += "LEFT JOIN recipes r ON u.id = r.user_id "
        query += "WHERE u.id = %(id)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)
        current_user = cls(results[0])

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['first_name']) == 0:
            flash("You must provide your first name!", "first_name_error")
            is_valid = False
        if len(data['last_name']) == 0:
            flash("You must provide your last name!", "last_name_error")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords must match!", "password_error")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", "email_error")
            is_valid = False
        return is_valid
    
    @staticmethod
    def encrypt_password( pwd, bcrypt ):
        return bcrypt.generate_password_hash( pwd )
    
    @classmethod
    def get_one( cls, data ):
        query  = "SELECT * "
        query += "FROM users "
        query += "WHERE email = %(email)s; "

        result = connectToMySQL( DATABASE ).query_db( query, data )
        if len( result ) > 0:
            return cls( result[0] )
        else:
            flash( "Wrong credentials!", "password_login_error" )
            return None
        
    @classmethod
    def create_one( cls, data ):
        query  = "INSERT INTO users( email, password, first_name, last_name ) "
        query += "VALUES( %(email)s, %(password)s, %(first_name)s, %(last_name)s ); "

        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result
    
    @staticmethod
    def validate_password(pwd, encr_pwd, bcrypt):
        if not bcrypt.check_password_hash(encr_pwd, pwd):
            flash("Wrong credentials!", "password_login_error")
            return False
        else:
            return True
    
    