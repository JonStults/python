from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yikes'
mysql = MySQLConnector(app,'emaildb')


@app.route('/')
def index():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('index.html', all_emails=emails)

@app.route('/emails', methods = ['POST'])
def create ():
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", request.form['email']):
        query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
        data = {'email': request.form['email']}
        session['email']=request.form['email']
        mysql.query_db(query,data)
        query = "SELECT * FROM emails"
        emails = mysql.query_db(query)
        return render_template('/success.html', all_emails=emails, name=session['email'])
    else:
        message = "Email is not valid!"
        flash(message)
        return redirect('/')

app.run(debug=True)
