from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('splash/splash.html')

@app.route('/about')
def about():
    return render_template('about/about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio/portfolio.html')

@app.route('/blog/<string:blog_id>')
def blog(blog_id):
    return render_template('blog/blog.html')

@app.route('/contact')
def contact():
    return render_template('contact/contact.html')
