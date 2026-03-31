from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'change-this-in-production'

@app.route('/')
def index():
    return "Hello, World! Your Flask app is running."

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)