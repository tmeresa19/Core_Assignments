from flask_app import app
from flask_app.controllers import pypie_controller, user_controller


if __name__ == "__main__":
    app.run( debug = True )