from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/products')
def gallery():
    return render_template('products.html')

@app.route('/contact-us')
def gallery():
    return render_template('contact-us.html')

if __name__ == "__main__":
    app.run()
