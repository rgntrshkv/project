from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import NumberRange


class SizeForm(FlaskForm):
    width = IntegerField('Ширина мира', default=20, validators=[NumberRange(min=10, max=50)])
    height = IntegerField('Высота мира', default=20, validators=[NumberRange(min=10, max=50)])
    submit = SubmitField('принять')
