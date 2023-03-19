# import connectToMySQL function from mysqlconnection module
from mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"  # SQL query to select all rows from users table
        # execute query using connectToMySQL and store results
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in results:
            # create new User instance for each row returned by query and append to list
            users.append(cls(u))
        return users  # return list of User instances

    @classmethod
    def save(cls, data):
        # SQL query to insert new row into users table
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        # comes back as the new row id
        # execute query with data parameter using connectToMySQL and store result
        result = connectToMySQL('users_schema').query_db(query, data)
        return result  # return result (new row id)
