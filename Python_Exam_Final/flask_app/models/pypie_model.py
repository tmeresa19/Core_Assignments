from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask_app import DATABASE, EMAIL_REGEX
from flask import flash


class PyPie:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.filling = data['filling']
        self.crust = data['crust']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.owner = None

    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query += "FROM pypies "
        query += "WHERE pypies.id = %(id)s; "

        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO pypies(name, filling, crust, user_id ) "
        query += "VALUES(%(name)s, %(filling)s, %(crust)s, %(user_id)s );"

        result = connectToMySQL(DATABASE).query_db(query, data)
        # INSERT and UPDATE don't throw any list. So, we won't need to send this result back.
        # But, if there's an issue with the query, we could possibly print result to see what could be wrong
        print(result)
        return result

    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * "
        query += "FROM pypies p "
        query += "JOIN users u ON p.user_id = u.id;"

        # to execute the above query
        results = connectToMySQL(DATABASE).query_db(query)
        list_of_pypies = []

        for row in results:
            current_pypie = cls(row)
            data_for_user = {
                "id": row['u.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
                "password": row['password']
            }
            current_pypie.owner = User(data_for_user)
            list_of_pypies.append(current_pypie)
        return list_of_pypies
    
    @classmethod
    def update_one(cls, data):
        query = "UPDATE pypies "
        query += "SET name = %(name)s, filling = %(filling)s, crust = %(crust)s, user_id = %(user_id)s "
        query += "WHERE id=%(id)s;"

        # before executing the query, need to validate (which is in the controller) then come here and execute the query as:
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM pypies "
        query += "WHERE id = %(id)s; "
        
        result = connectToMySQL (DATABASE ).query_db(query, data)
        # print (result)
        return result
    
    
    @staticmethod
    def validate_pypie(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters long.", "error_name")
            is_valid = False
        if len(data['filling']) < 3:
            flash("Filling must be at least 3 characters long.",
                "error_filling")
            is_valid = False
        if len(data['crust']) < 3:
            flash("Crust must be at least 3 characters long.",
                "error_crust")
            is_valid = False
        return is_valid

