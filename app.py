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


# SQLAlchemy allows us to represnt database structe as classes (aka models)
# Each class its own table in SQLALCHEMY_DATABASE_URI
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


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
