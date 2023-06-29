
import flask
from flask import request, jsonify, render_template, send_file, send_from_directory, url_for, redirect, flash, session, make_response


app = flask.Flask(__name__)
app._static_folder = 'static'
app.config["DEBUG"] = True
app.secret_key = "super secret key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


user_found = []

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/',methods=["POST", "GET"])
def index():
    return render_template('index.html')


app.run()

