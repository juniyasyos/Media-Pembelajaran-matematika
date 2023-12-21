# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/quiz')
def wuiz_page():
    return render_template('quiz.html')

@app.route('/topics')
def dashboard():
    return render_template('dashboard.html')

@app.route('/exercise')
def wuiz_page():
    return render_template('quiz.html')

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/quiz')
def wuiz_page():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)
