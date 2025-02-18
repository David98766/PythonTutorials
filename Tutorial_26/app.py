import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for, abort

app = Flask(__name__)
# session key to allow fo session handling
app.config['SECRET_KEY'] = 'your secret key'

# Function to retrieve the database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to grab post from database based on primary key
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/')
def index():
    # grabbing the connection first
    conn = get_db_connection()
    # executing the query on the database then to fetch all
    posts = conn.execute('SELECT * FROM posts').fetchall()
    # closing the connection
    conn.close()
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
            # Insert the new record to the database
            conn = get_db_connection()
            # pass in parameters using tuple
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            # commit transaction and close connection
            conn.commit()
            conn.close()
            # redirect to function returning to index endpoint
            return redirect(url_for('index'))

    return render_template('create.html')

# this endpoint is taking a parameter of id
@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
# the parameter named after <int: needs to be the same as what the function is calling it
def edit(id):
    #using the function get_post defined above here
    # defined outside condition as we need to render the post if it's a get request
    post = get_post(id)
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
            # write query execute with parameters and commit and close
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


# another endpoint that takes argument of id
@app.route('/<int:id>/delete/', methods=('POST',))
# again argument needs to be the same as in the url
def delete(id):
    # grab the post using get function
    post = get_post(id)
    conn = get_db_connection()
    # take ID from the post and execute query
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)