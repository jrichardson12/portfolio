from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Index'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page'

@app.route('/blog')
def blog():
    return "Blog Page"

@app.route('/contact')
def contact():
    return "Contact page"