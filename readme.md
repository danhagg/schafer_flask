# SQLAlchemy
In cmd line... run python

```python
from flask_job import db
from flask_job.models import User, Post
db.create_all()
User.query.all()
```


SQLAlchemy allows us to represent database structure as classes (aka models)

Each class its own table in SQLALCHEMY_DATABASE_URI.

During initial setup of classes we tested like this...

- Import db, by going to cmdline,
- "python"... "from flaskblog import db"
- "db.create_all()"
- "from flaskblog import User, Post"
- "user_1 = User(username="dan", email="dan@gmail.com", password='password')
- db.session.add(user_1)
- user_2 = User(username='JohnDoe', email='JD@demo.com', password='password')
- db.session.add(user_2)
- db.session.commit()
- User.query.all()
- User.query.first()
- user = User.query.filter_by(username="Corey").first()
- user.id
- user.posts
- post_1 = Post(title='Blog 1', content='first post', user_id=User.id)
- post_2 = Post(title='Blog 2', content=' post', userid=user.id)
- db.session.add(post_1)
- db.session.add(post_2)
- db.session.commit()
- user.posts

# Circular Imports and packaging
Circular imports when moving the SQLAlchemy classes into `models.py`.

When app is run from cmd line then python names the app `flaskblog.py` `__main__`. At the top of `flaskblog.py` we import from `models.py` both `User` and `Post`. So, when python looks in `models.py` it reads the line `from flaskblog import db`. Now... its already read `flaskblog.py` but under the pseudonym `__main__` so it does not know what `flaskblog` is.

If we then change in `models.py`

```python
from flaskblog import db
# to
from __main__ import db
```

We then get the standard, more understandable circular error `ImportError: cannot import name 'db'`. Because `flaskblog` is trying to import from models (and subsequently `db` from `models`) prior to the declaration of `db` itself in `flaskblog`.

We can get around all this nonsense by making our python application a `package` by making a new `flaskblog` folder and make an `__init__.py` file inside, and copy all files (other than `flaskblog.py`) into it. Now we a `flaskblog package` (the folder) and a `flaskblog module` (`.py` file).


# Bcrypt
```python
>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()

# Run same password twice = different results
>>> bcrypt.generate_password_hash('test')
b'$2b$12$DHHmUyt05oS3W4IzncHkte78uLhU7//q2ZRjQwUl.X3B71rEVXSaq'
>>> bcrypt.generate_password_hash('test')
b'$2b$12$tPTFDTDtOfgas/SKmX75z.lUJOyvVYoeXUNfOj7JAXcc7cexbFuJ2'

# Change from bytes to string
>>> bcrypt.generate_password_hash('test').decode('utf-8')
'$2b$12$FdwVUYMOw30fMJQGLJ7Ls.hzhgbu/GjKAegHrD.8yRQu.i9nZJgOq'
```

As the hash gives a diff answer each time we need to check password hash to validate a password check.

```python
>>> hashed_pwd = bcrypt.generate_password_hash('test')
>>> hashed_pwd
b'$2b$12$99250LKAauuSeXMM.KSy/.oizj1YyNdmIzv9jjwLycSITimTV8tBS'


>>> bcrypt.check_password_hash(hashed_pwd, 'password')
false

>>> bcrypt.check_password_hash(hashed_pwd, 'test')
True
```
