from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'change-this-in-production'

@app.route('/')
def index():
    return "Hello, World! Your Flask app is running."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'password123':
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')

    return render_template('dashboard.html', username=session['username'])

if __name__ == '__main__':
    app.run(debug=True)