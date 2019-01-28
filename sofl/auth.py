from flask import g
from flask_httpauth import HTTPBasicAuth
from sofl.models import User
from sofl.errors import error_response

basic_auth = HTTPBasicAuth()

@basic_auth.verify_password
def verify_password(username, password):
    user = User.get_or_none(User.username == username)
    if not user:
        return False
    g.current_user = user
    return user.check_password(password)

@basic_auth.error_handler
def basic_auth_error():
    return error_response(401, 'Invalid credentials.')