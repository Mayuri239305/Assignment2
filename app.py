from flask import Flask, render_template, redirect, url_for, request, session
from config import Config
from models import init_app, register_user, validate_user

app = Flask(__name__)
app.config.from_object(Config)
init_app(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        register_user(username, password)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validate_user(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid Credentials'
    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session:
        return f'Hello, {session["username"]}!'
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

