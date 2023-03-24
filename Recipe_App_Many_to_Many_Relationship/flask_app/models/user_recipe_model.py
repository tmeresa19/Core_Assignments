from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_recipe_model import UserRecipe

# # 1. Create a new file called "user_recipe_model.py" in your "models" directory. This file will contain the definition of the UserRecipe class .

# 2. In the UserRecipe class , define the attributes "id", "user_id", and "recipe_id". "id" will be the primary key of the table, "user_id" will be a foreign key referencing the User table, and "recipe_id" will be a foreign key referencing the Recipe table.

class UserRecipe:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.recipe_id = data['recipe_id']
    
#  3. In the UserRecipe class , define a method called "create_one" that will insert a new row into the "user_recipe" table.

    @classmethod
        def create_one(cls, data):
            query = "INSERT INTO user_recipe (user_id, recipe_id) VALUES (%(user_id)s, %(recipe_id)s);"
            result = connectToMySQL(DATABASE).query_db(query, data)
            return result


#     @ classmethod
#     def create_one(cls, data):
#     query="INSERT INTO recipes(name, description, instructions, date_cooked, under_thirty, user_id ) "
#     query += "VALUES(%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_thirty)s, %(user_id)s );"
#     result=connectToMySQL(DATABASE).query_db(query, data)
#     return result

# 4. Double LEFT JOINS to address the M-to-M r/s

    @classmethod
    def get_by_id(cls, data):
        query = 'SELECT * FROM books '
        query+= 'LEFT JOIN favorites ON books.id = favorites.book_id '
        query+= 'LEFT JOIN authors ON authors.id = favorites.author_id '
        query+= 'WHERE books.id = %(id)s;'
        
        book = cls(results[0])
        
        for row in results:
            if row['authors.id']==NOne:
                break
            data = {
                'id' : row['authors.id'],
                'name' : row['name'],
                # 'name': row['authors.name'],
                'created_at' : row['authors.created_at'],
                'updated_at' : row['authors.updated_at']
            }
            book.authors_who_favorited.append(author.Author(data))
        return book
    
    # 5. Unfavorited authors: using the NOT IN key work of the select statement
    # that means filtering out any of the ids that don't match up. Then, it will return
    # all the different authors that didn't favorited the books
    
    @classmethod
    def unfavorited_authors(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL('books').query_db(query, data)
        for row in results:
            authors.append(cls(row))
        return authors
    
# 6.Unfavorited books:

@classmethod
def unfavorited_books(cls, data):
    query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('books').query_db(query, data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books
    
    # 7. 
    
    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)

        # Creates instance of author object from row one
        author = cls(results[0])
        # append all book objects to the instances favorites list.
        for row in results:
            # if there are no favorites
            if row['books.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(book.Book(data))
        return author

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

#     @ classmethod
#     def get_one_by_id(cls, data):
#     query="SELECT * FROM recipes WHERE id = %(id)s"
#     result=connectToMySQL(DATABASE).query_db(query, data)
#     if len(result) == 0:
#     return False
#     else:
#     return cls(result[0])

#     @ classmethod
#     def update_one(cls, data):
#     query="UPDATE recipes SET "
#     query += "name=%(name)s, "
#     query += "description=%(description)s, "
#     query += "instructions=%(instructions)s, "
#     query += "date_cooked=%(date_cooked)s, "
#     query += "under_thirty=%(under_thirty)s "
#     query += "WHERE id=%(id)s;"
#     result=connectToMySQL(DATABASE).query_db(query, data)
#     return result

#     @ classmethod
#     def delete_one(cls, data):
#     query="DELETE FROM recipes WHERE id = %(id)s;"
#     result=connectToMySQL(DATABASE).query_db(query, data)
#     return result

#     @staticmethod
#     def validate_recipe(data):
#         errors={}
#         if 'name' not in data or not data['name'].strip():
#             errors['name']='Name is required.'
#         if 'description' not in data or not data['description'].strip():
#             errors['description']='Description is required.'
#         if 'ingredients' not in data or not data['ingredients'].strip():
#             errors['ingredients']='Ingredients are required.'
#         if 'instructions' not in data or


    
