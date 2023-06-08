from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class HouseForm(FlaskForm):
    height = IntegerField("Высота дома")
    weight = IntegerField("Ширина дома")
    submit = SubmitField("Создать дом")

class MoveForm(FlaskForm):
    way = SelectField("Выберите сторону света", 
                            coerce=int,
                            choices=[(0, 'Север'),
                                     (1, 'Юг'),
                                     (2, 'Восток'),
                                     (3, 'Запад')],
                            validators = [DataRequired()])
    number_steps = IntegerField("На какое количество шагов хотите продвинуться?",
                                validators = [DataRequired(), NumberRange(min=1)],
                                default = 1)
    submit = SubmitField("Сделать движение")