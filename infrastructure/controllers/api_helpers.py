from flask import Flask


def create_app() -> Flask:
    new_app = Flask(__name__)
    return new_app
