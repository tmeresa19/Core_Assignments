from flask import Flask
import re
app = Flask(__name__)

app.secret_key = "password1234"
DATABASE = "users_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
