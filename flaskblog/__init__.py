from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# "__name__" name of module
app = Flask(__name__)

# Must be made an environment variable later on
app.config['SECRET_KEY'] = '11713771a462f1248420575583db66db'
# "///" relative path from current file
# Will change it to postgresql at production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creat db instance
db = SQLAlchemy(app)

from flaskblog import routes
