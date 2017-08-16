from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key="sosecret"

mystery = random.randrange(0, 101)
print(mystery)
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/numbers', methods = ['POST'])

def numbers():
    session['number'] = request.form['number']
    if mystery == int(session['number']):
        print("winner")
    else:
        session.pop('number')
    return redirect('/')

app.run(debug=True)
