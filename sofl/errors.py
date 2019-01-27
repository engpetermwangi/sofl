from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
def error_response(status_code, message = None):
    error = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        error['message'] = message
    response = jsonify(error)
    response.status_code = status_code
    return response

def bad_request(message):
    return error_response(400, message)