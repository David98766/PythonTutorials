from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField)
from wtforms.validators import InputRequired, Length

class CourseForm(FlaskForm):
    # Defining a collection of form fields as class variables
    # When you instantiate a field, the first argument is the fields label
    title = StringField('Title', validators=[InputRequired(), Length(min=10, max=100)])
    description = TextAreaField('Course Description',
                                validators=[InputRequired(), Length(max=200)])
    # Input box for numbers (with increase and decrease arrows)
    price = IntegerField('Price', validators=[InputRequired()])
    # Radio Buttons
    level = RadioField('Level',choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])
    # This is a checkbox
    available = BooleanField('Available', default='checked')