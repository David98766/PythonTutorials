from flask import Flask, render_template
from data.movie_data import movies  # Import movie data
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)