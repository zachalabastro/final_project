from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def index():
    return render_template('welcome-page.html')

@app.route('/welcomepage')
def welcomepage():
    return render_template('welcome-page.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/birdseye')
def birdseye():
    return render_template('birds-eye.html')

if __name__ == '__main__':
    app.run()