from flask import Flask, redirect, render_template, session, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shit'
mysql = MySQLConnector(app, 'the_wall')


@app.route('/')
def index():
    if 'aPost' not in session:
        session['aPost']=""
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    # email = request.form['email']
    # print email
    # password = request.form['password']
    # print password
    # return redirect('wall.html')
    email = "jdstults1@gmail.com"
    password = "password"
    return redirect('/wall')

@app.route('/register', methods = ['POST'])
def register():
    query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    data = {
            "first_name": "Jon",
            "last_name": "Stults",
            "email": "jdstults1@gmail.com",
            "password": "password"
            }
    mysql.query_db = (query,data)
    return redirect('/wall')

@app.route('/wall')
def wall():
    return render_template('wall.html')

@app.route('/postmsg', methods = ['POST'])
def postmsg():
    query = "INSERT INTO messages(message) VALUES (:content)"
    data = {
            "content": request.form['message']
    }
    session['aPost'] = request.form['message']
    mysql.query_db = (query,data)
    print request.form['message']
    print data
    print query
    return redirect('/wall')
app.run(debug=True)
