from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/process_info', methods=['POST'])
def process_info():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    return render_template('redirect.html', one=name, two=location, three=language, four=comments)

@app.route('/send_back')
def send_back():
    return redirect('/')

app.run(debug=True)
