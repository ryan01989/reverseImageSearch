from flask import Flask, Blueprint, render_template, url_for

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')
