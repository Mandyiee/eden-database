from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

PLACEHOLDER_CODE = "HELLO WORLD"

class CodeForm(FlaskForm):
    code = TextAreaField('What is your code?', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class StyleForm(FlaskForm):
    style = SelectMultipleField()
    submit = SubmitField('Submit')