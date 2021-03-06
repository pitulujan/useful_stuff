#!venv/bin/python
from flask import Flask, jsonify, abort, make_response, g, request
from flask_httpauth import HTTPBasicAuth
from typing import Any
import jwt
from time import time 
from werkzeug.exceptions import BadRequest 


private_key = open("jwt-key").read()
public_key = open("jwt-key.pub").read()





auth = HTTPBasicAuth()

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": u"Buy Groceries",
        "description": "Milk,Cheese, Pizza,Fruit,Tylenol",
        "done": False,
    },
    {
        "id": 2,
        "title": u"Learn French",
        "description": "Get your ass to work",
        "done": False,
    },
]

class NotAuthorized(BadRequest):
    def get_json_repr(self):
        return str(self)


class User:
    def __init__(self, username: str, password: str, id: int):
        self.username = username
        self.password = password
        self.id = id

    def _get_username(self):
        return self.username

    def _get_password(self):
        return self.password

    def _get_id(self):
        return self.id

    def generate_auth_token(self, expiration=300):
        payload = {"user_id": self.id, "exp": time() + expiration}
        return jwt.encode(payload, private_key, algorithm="RS256").decode("utf-8")


pitu = User("pitu", "tuvieja", 1)
julian = User("julian", "tuvieja", 2)
users = [pitu, julian]

@app.errorhandler(NotAuthorized)
def respond_not_authorized(e: NotAuthorized):
    return jsonify({"error" : e.get_json_repr()}), 400 


@app.errorhandler(404)
def not_fount(error):
    return make_response(jsonify({"error": "Not Found Vieja"}))


@app.errorhandler(401)
def not_fount(error):
    return make_response(
        jsonify(
            {
                "error": "Missing or Malformed authentication. HTTP authorization header should be of the form 'Bearer [JWT]'"
            }
        )
    )


@auth.verify_password
def verify_password(username_or_token, password):

    auth_header =  request.headers.get("Authorization", None)

    if auth_header is None:
        abort(401)
    token = None 

    try:
        auth_type,token = auth_header.strip().split(" ")
    except:
        abort(401)
    if auth_type.lower() == "basic":

        user = [
            user
            for user in users
            if user._get_username() == username_or_token
            and user._get_password() == password
        ]
        if not user:
            return False

        g.user = user[0]
        return True
    
    elif auth_type.lower() == "bearer":
        user = verify_auth_token(token)
        g.user = user[0]
        return True
    else:
        abort(401)





def verify_auth_token(token):

    try:
        payload = jwt.decode(token, public_key, algorithms=["RS256"])
    
    except jwt.DecodeError:
        return None
    except jwt.ExpiredSignatureError:
        raise NotAuthorized("Token Expired")

    user = [user for user in users if user._get_id() == payload["user_id"]]
    return user


@app.route("/todo/api/v1.0/tasks/token", methods=["GET"])
@auth.login_required
def get_token():
    token = g.user.generate_auth_token()
    return jsonify({"token": token})


@app.route("/todo/api/v1.0/tasks", methods=["GET"])
@auth.login_required
def get_tasks():
    return jsonify({"tasks": tasks})


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["GET"])
@auth.login_required
def get_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({"task": task[0]})


@app.route("/todo/api/v1.0/tasks", methods=["POST"])
@auth.login_required
def create_task():
    if not request.json or not "title" in request.json:
        abort(400)
    task = {
        "id": tasks[-1]["id"] + 1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False,
    }
    tasks.append(task)
    return jsonify({"task": task}), 201


if __name__ == "__main__":
    app.run(debug=True)
