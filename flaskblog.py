from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

# "__name__" name of module
app = Flask(__name__)

# Must be made an environment variable later on
app.config['SECRET_KEY'] = '11713771a462f1248420575583db66db'
# "///" relative path from current file
# Will change it to postgresql at production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creat db instance
db = SQLAlchemy(app)

# SQLAlchemy allows us to represent database structure as classes (aka models)
# Each class its own table in SQLALCHEMY_DATABASE_URI
# Import db, by going to cmdline,
# "python"... "from flaskblog import db"
# "db.create_all()"
# "from flaskblog import User, Post"
# "user_1 = User(username="dan", email="dan@gmail.com", password='password')
# db.session.add(user_1)
# user_2 = User(username='JohnDoe', email='JD@demo.com', password='password')
# db.session.add(user_2)
# db.session.commit()
# User.query.all()
# User.query.first()
# user = User.query.filter_by(username="Corey").first()
# user.id
# user.posts
# post_1 = Post(title='Blog 1', content='first post', user_id=User.id)
# post_2 = Post(title='Blog 2', content=' post', userid=user.id)
# >>> db.session.add(post_1)
# db.session.add(post_2)
# db.session.commit()
# user.posts


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(
        db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # Add relationship (not col) to Post
    # backref = to Post (not a col)
    # lazy = load data as necessary in one go (all posts by one user)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(
        db.DateTime,
        nullable=False,
        # always utc (not as the method() but as function)
        default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # Relationship to user, id from User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [{
    'author': 'dan',
    'title': 'Job1',
    'content': 'First',
    'date_posted': 'April 20, 2018'
}, {
    'author': 'dave',
    'title': 'Job2',
    'content': 'Second',
    'date_posted': 'April 21, 2018'
}]


@app.route("/")
@app.route("/home")
def home():
    # posts jinja2 var allows us access to posts data (list declared above)
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Bootstrap alert (success/category) as second arg
        flash(f'Account created for {form.username.data}!', 'success')
        # redirect takes @app.route function
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@work.com" and form.password.data == "password":
            flash('You have been logged in!', 'succes')
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful. Please check username and password.",
                  'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
