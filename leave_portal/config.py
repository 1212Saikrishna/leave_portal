import os

class Config:
    DEBUG = True
    SECRET_KEY = 'your_secret_key'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///leave_requests.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Mail configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'msaik739@gmail.com'
    MAIL_PASSWORD = 'sety huaq gpxq ftjq'
    MAIL_DEFAULT_SENDER = 'msaik739@gmail.com'