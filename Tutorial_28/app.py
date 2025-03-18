import sqlite3
from flask import (Flask, render_template, request, flash, redirect
, url_for, abort)

from Tutorial_28.dao.PostDao import PostDao
from Tutorial_28.model.Post import Post

app = Flask(__name__)
# session key to allow fo session handling
app.config['SECRET_KEY'] = 'your secret key'

postDao = PostDao()


# Function to grab post from database based on primary key
@app.route('/')
def index():
    posts = postDao.get_all_posts()
    # pass return of the query with the page to be rendered
    return render_template('index.html', posts=posts)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    # conditional do this if the request is a post
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:

            postDao.create_post(title, content)
            # redirect to function returning to index endpoint
            return redirect(url_for('index'))

    return render_template('create.html')

# this endpoint is taking a parameter of id
@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
# the parameter named after <int: needs to be the same as what the function is calling it
def edit(id):
    #using the function get_post defined above here
    # defined outside condition as we need to render the post if it's a get request
    post = postDao.get_post_by_id(id)
    # anything that changes the data in the database is a post
    # we are applying the same logic as create with two conditions
    # one based on if it's a post and the get for retrieving the page
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            postDao.update_post(post.id, title, content)

            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


# another endpoint that takes argument of id
@app.route('/<int:id>/delete/', methods=('POST',))
# again argument needs to be the same as in the url
def delete(id):
    # grab the post using get function
    post = postDao.get_post_by_id(id)
    postDao.delete_post(post.id)

    flash('"{}" was successfully deleted!'.format(post.title))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)