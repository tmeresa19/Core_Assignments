from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.users_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt( app )