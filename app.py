from flask import Flask
from config import CONFIG

def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(CONFIG[environment])
    return app

app = create_app('development')

if __name__ == '__main__':
    app.run()