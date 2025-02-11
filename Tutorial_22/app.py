from flask import (Flask, render_template, request, flash, redirect, url_for)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

messages=[
    {'title': 'Message One',
    'content': 'Message One Content'},
    {'title': 'Message Two',
    'content': 'Message Two Content'}
    ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)


# Get = requesting data from the server, Post = posting data to the server
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # flash is used for validation
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    # This has nothing to do with the post, this is if the method is get
        return render_template('create.html')



if __name__ == '__main__':
    app.run(debug=True)