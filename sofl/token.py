from flask import jsonify, g
from sofl import app, db
from sofl.auth import basic_auth

@app.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_token()
    current_user.save
    return jsonify({'token': token})