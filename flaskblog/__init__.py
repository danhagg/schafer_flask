from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# "__name__" name of module
app = Flask(__name__)

# Must be made an environment variable later on
app.config['SECRET_KEY'] = '11713771a462f1248420575583db66db'
# "///" relative path from current file
# Will change it to postgresql at production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creat db instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
