from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField, StringField
from wtforms.validators import NumberRange, DataRequired, Length


class Login(FlaskForm):
    name = StringField("Имя: ", validators=[DataRequired(), Length(min=3, max=15, message="Имя должно быть от 3 до 15 символов")])
    submit = SubmitField("Начать игру")


class ChoiceStep(FlaskForm):
    way = SelectField(
        "Выберите сторону света, в которую желаете отправится",
        coerce=int,
        choices=[
            (0, 'North'),
            (1, 'East'),
            (2, 'South'),
            (3, 'West')
        ],
        render_kw={
            'class': 'form-control'
        },
    )

    number_steps = IntegerField(
        """Введите количество шагов (от 1 до 2): """,
        validators=[NumberRange(min=1, max=2), DataRequired()],
        default=1,
        render_kw={
            'class': 'form-control'
        }
    )

    submit = SubmitField("Отправить")
