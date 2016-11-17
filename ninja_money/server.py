from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key='ninja'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
    if 'log' not in session:
        session['log']= ""
    total = session['gold']
    print total
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():

    requested_data = request.form['location']

    if requested_data == 'farm':
        value=random.randrange(10,21)

    if requested_data == 'cave':
        value=random.randrange(5,10)

    if requested_data == 'house':
        value=random.randrange(2,5)

    if requested_data == 'casino':
        value=random.randrange(-50,50)

    if('location'=='casino' and value<0):
        print 'Entered a casino and lost' + str(value) + 'gold...Outch' + requested_data + "!"
    else:
        print session['log'] = 'Earned'+ " " + str(value) + " " + 'golds from the' + " " + requested_data + "!" + session['log']

    session['log'] = 'Earned'+ " " + str(value) + " " + 'golds from the' + " " + requested_data + " !\n" + session['log']
    session['gold'] += value

app.run(debug=True)
