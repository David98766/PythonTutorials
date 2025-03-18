from flask import Flask, render_template
from dao.BlogDao import BlogDao
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

blogDao = BlogDao()
@app.route('/')
def index():
    blogs = blogDao.getAllBlogs()
    return render_template('index.html', blogs=blogs)

if __name__ == '__main__':
    app.run(debug=True)
