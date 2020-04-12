from werkzeug.exceptions import BadRequest 
from api.errors import bp
from flask import make_response,jsonify


class NotAuthorized(BadRequest):
    def get_json_repr(self):
        return str(self)

@bp.app_errorhandler(NotAuthorized)
def respond_not_authorized(e: NotAuthorized):
    return jsonify({"error" : e.get_json_repr()}), 400 


@bp.app_errorhandler(404)
def not_fount(error):
    return make_response(jsonify({"error": "Not Found Vieja"})),400


@bp.app_errorhandler(401)
def not_fount(error):
    return make_response(
        jsonify(
            {
                "error": "Missing or Malformed authentication. HTTP authorization header should be of the form 'Bearer [JWT]'"
            }
        )
    ), 400
