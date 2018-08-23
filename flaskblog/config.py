import os


class Config:
    # Must be made an environment variable later on
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # "///" relative path from current file
    # Will change it to postgresql at production
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # Environment Variables in .bash_profile
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
