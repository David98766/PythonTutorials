from flask import Flask, render_template, abort, redirect, url_for, request
from data.movie_data import movies  # Import movie data
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

# this endpoint is taking a parameter of movieTitle
@app.route('/<string:movieTitle>/view_details/', methods=['GET'])
# the parameter named after <int: needs to be the same as what the function is calling it
def view_details(movieTitle):

    movie = None  # Default to None if no match is found

    for m in movies:
        if m['movieTitle'] == movieTitle:  # Check if the movie title matches
            movie = m  # Store the first matching movie
            break  # Stop searching once we find the match

    if movie is None:
        abort(404)  # Return a 404 page if the movie is not found

    return render_template('single-movie.html', movie=movie)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        movieTitle = request.form['movieTitle']
        movieReleaseYear = request.form['movieReleaseYear']
        movieStars = request.form['movieStars']
        movieImageURL = request.form['movieImageURL']

        # Convert `movieStars` and `movieReleaseYear` to integers
        try:
            movieReleaseYear = int(movieReleaseYear)
            movieStars = int(movieStars)
        except ValueError:
            return "Invalid input. Please enter numeric values for Release Year and Stars.", 400

        new_movie = {
            "movieTitle": movieTitle,
            "movieReleaseYear": movieReleaseYear,
            "movieStars": movieStars,
            "movieImageURL": movieImageURL
        }

        movies.append(new_movie)
        return redirect(url_for('index'))  # Redirect to homepage

    return render_template('add-movie.html')


if __name__ == '__main__':
    app.run(debug=True)