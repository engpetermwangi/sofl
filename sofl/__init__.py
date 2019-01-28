from flask import Flask
from peewee import SqliteDatabase
from sofl.config import CONFIG

def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(CONFIG[environment])
    return app

# App instance
app = create_app('development')

# Creation of database
db = SqliteDatabase(app.config['DATABASE'])

from sofl import routes, tokens