from flask import jsonify, g
from sofl import app
from sofl.auth import basic_auth

@app.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_token()
    return jsonify({'user': g.current_user.username, 'token': token})