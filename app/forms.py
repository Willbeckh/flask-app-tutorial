from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    username = StringField('User name', validators=[DataRequired()])
    post = TextAreaField('Post', validators=[DataRequired()])
    submit = SubmitField('Submit')

    