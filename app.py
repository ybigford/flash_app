#initialize flask
from flask import Flask, render_template
app = Flask(__name__)

#define home page route
@app.route('/')
def home():
    return render_template ('index.html')

#define about page route
@app.route('/about')
def about():
    return render_template ('about.html')

#define contact page route
@app.route('/contact')
def contact():
    return render_template ('contact.html')


if __name__ == '__main__':
    app.run(debug=True)