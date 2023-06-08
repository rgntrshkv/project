from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import InputRequired

class GOFForm(FlaskForm):
    height = IntegerField("Высота игрового поля")
    weight = IntegerField("Ширина игрового поля")
    oldw_flag = SelectField("Отображать красным цветом клетки, умершие на текущем ходу?", 
                            coerce=int,
                            choices=[(1, 'Yes'),
                                     (0, 'No')])
    time_reload = IntegerField("Время обновления, в мс")
    submit = SubmitField("Создать жизнь")