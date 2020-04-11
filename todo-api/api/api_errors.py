from werkzeug.exceptions import BadRequest 
class NotAuthorized(BadRequest):
    def get_json_repr(self):
        return str(self)