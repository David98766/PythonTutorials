from flask import Flask, render_template, redirect, url_for
from forms import CourseForm # this class is declared in forms.py
from dao.courses_dao import courses_list
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# GET method = retrieving data, POST requests = sending data to the server (in our case through a web form)
@app.route('/', methods=('GET', 'POST'))
def index():
    # instantiating the CourseForm() class
    form = CourseForm()
    # the validate_on_submit method sees if there is a POST request, and
    # checks if all validations from the form are true (no errors)
    if form.validate_on_submit():
        # building a course dictionary and appending it to our courses_list
        # form.field_name.data is setting the value for each class variable
        courses_list.append({'title': form.title.data,
                            'description': form.description.data,
                            'price': form.price.data,
                            'available': form.available.data,
                            'level': form.level.data
                             })
        return redirect(url_for('courses'))
    # passing the form (CourseForm) instance to the index.html template
    return render_template('index.html', form=form)

@app.route('/courses')
def courses():
    return render_template('courses.html', courses_list=courses_list)

if __name__ == '__main__':
    app.run(debug=True)