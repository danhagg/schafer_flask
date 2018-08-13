from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

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


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
