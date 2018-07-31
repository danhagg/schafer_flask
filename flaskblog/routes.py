from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # Bootstrap alert (success/category) as second arg
        flash(
            f'Account created for {form.username.data}! You are now able to log in.',
            'success')
        # redirect takes @app.route function
        return redirect(url_for('login'))
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
