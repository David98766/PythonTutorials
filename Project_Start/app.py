from flask import Flask, render_template
from BlogDao.BlogDao import BlogDao
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():

    return render_template('index.html',)