from flask import flask
app = flask (__name__)
@app.route("/home")
def index():
    return render-template ("index.html")
