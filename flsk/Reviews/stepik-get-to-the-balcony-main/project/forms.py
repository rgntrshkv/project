from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange


class ProfileForm(FlaskForm):
    side_of_the_world = SelectField(
        'Выберите сторону света, в которую желаете отправиться.',
        coerce=int,
        choices=[
            (0, 'Север'),
            (1, 'Восток'),
            (2, 'Юг'),
            (3, 'Запад')
        ],
        render_kw={
            'class': 'form-control'
        },
    )
    step = IntegerField(
        'Как далеко планируете продвинуться? (Шаги)',
        validators=[NumberRange(min=1), DataRequired()],
        default=1,
        render_kw={
            'class': 'form-control'
        },
    )
    submit = SubmitField('Принять')
