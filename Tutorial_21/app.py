import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# default route will look like http://{ip address}:5000
#port 5000 because it is the normal port for python applications
@app.route('/')
def hello():
    #calling render_template to display index html file
    #passing date and time in with it to be displayed by Jinja2
    #datetime.datetime = datetime class from the datetime module
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

#Creating a new endpoint called /about this will return a new html page
#It will look like http://{ip addrss}:5000/about
@app.route('/about/')
def about():
    #Calling the render_template function to return about.html page to client
    return render_template('about.html')

#Creating another new endpoint to display new html page
#It will look like http://{ip address}:5000/comments
@app.route('/comments/')
def comments():
    # comments list hard coded but would be pulled from a database normally
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]
    # returns a html page to the client called comments.html
    # returns web page with array comments
    return render_template('comments.html', comments=comments)

@app.route('/comments2/')
def comments2():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments2.html', comments=comments)

@app.route('/bootstrap_columns/')
def bootstrap_columns():
    #Calling the render_template function to return bootstrap_columns.html page to client
    return render_template('bootstrap_columns.html')

if __name__ == '__main__':
    app.run(debug=True)
