from datetime import datetime
# from flaskblog import db
from flaskblog import db


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
