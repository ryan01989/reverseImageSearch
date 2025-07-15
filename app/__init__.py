from flask import Flask, Blueprint
from .main import main as main_blueprint
import os


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_blueprint, url_prefix="", name="")

    return app
