from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'kanye'
mysql = MySQLConnector(app, 'the_wall')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wall', methods = ['GET'])
def wall():
    if 'message_id' not in session:
        session['message_id'] = 1
    query = "SELECT m.id, u.first_name, u.last_name, m.message, m.created_at FROM messages m JOIN users u on m.user_id = u.id"
    data = {
            'user_id': session['user']
    }
    message = mysql.query_db(query, data)
    query1 = "SELECT c.message_id, u.first_name, u.last_name, c.comment, c.created_at FROM comments c JOIN users u on c.user_id = u.id "
    data1 = {
            'user_id': session['user']
    }
    comment = mysql.query_db(query1,data1)
    return render_template('wall.html', all_messages = message, all_comments = comment)

@app.route('/login', methods = ['POST'])
def login():
    email = request.form['email1']
    password = request.form['password1']
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {
            'email' :email
    }
    user = mysql.query_db(query, data)
    print user
    if user:
        if bcrypt.check_password_hash(user[0]['password'], password):
            session['user']= user[0]['id']
            return redirect ('/wall')
        else:
            flash('Incorrect Password')
            return redirect ('/')
    else:
        flash('Email does not exist. Please register.')
        return redirect('/')

@app.route('/register', methods = ['POST'])
def register():
    password = request.form['password']
    pw_hash = bcrypt.generate_password_hash(password)
    query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW())"
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash
            }
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/post_message', methods = ['POST'])
def post_message():
    query = "INSERT INTO messages(user_id, message, created_at) VALUES (:user_id, :message, NOW())"
    data = {
            'user_id': session['user'],
            'message': request.form['message']
    }
    post_message = mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/post_comment', methods = ['POST'])
def post_comment():
    query = "INSERT INTO comments(message_id, user_id, comment, created_at) VALUES (:message_id, :user_id, :comment, NOW())"
    data = {
            'message_id': request.form['message_id'],
            'user_id': session['user'],
            'comment': request.form['comment']
    }
    post_comment = mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/logout', methods = ['POST'])
def logout():
    session.pop('user', None)
    return redirect('/')
app.run(debug=True)
