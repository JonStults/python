from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template('index.html')

@app.route('/ninjas')
def nin():
    return render_template('ninjas.html', phrase="Play pinball dudes!")

@app.route('/dojos/new')
def dojo():
    return render_template('dojos.html')

app.run(debug=True)