from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key="sosecret"



@app.route('/')

def index():
    if 'mystery' not in session:
        session['mystery'] = random.randrange(0, 101)
    print(session['mystery'])
    if 'word' not in session:
        session['word']=""
    return render_template('index.html', word = session['word'], key1 = session['key1']  )

@app.route('/numbers', methods = ['POST'])

def numbers():
    session['number'] = request.form['number']
    if int(session['mystery']) == int(session['number']):
        session['key1'] = str(session['mystery']) + " was the number"
        session['word'] = "win"
    elif int(session['mystery']) > int(session['number']):
        session['word'] = "Too Low!"
        session.pop('number')
    elif int(session['mystery']) < int(session['number']):
        session['word'] = "Too High!"
        session.pop('number')
    return redirect('/')

@app.route('/reset', methods=["POST"])

def reset():
    session['mystery'] = random.randrange(0, 101)
    session['word']=''
    return redirect('/')

app.run(debug=True)
