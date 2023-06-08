import json

from flask import Flask, render_template, redirect

from forms import SizeForm
from game_of_life import *
from generate_secret_key import generate_secret_key

app = Flask(__name__)

SECRET_KEY = generate_secret_key()
app.config.from_mapping({'SECRET_KEY': SECRET_KEY})


@app.route('/', methods=['get', 'post'])
def index():
    """Задание размера мира и его инициализация"""
    form_size = SizeForm()
    if form_size.validate_on_submit():
        width = form_size.width.data
        height = form_size.height.data

        GameOfLife(width, height)
        return redirect('/live')
    return render_template('index.html', form_size=form_size)


@app.route('/reload_table')
def live1():
    life = GameOfLife()
    cell = [['' for w in range(life.get_width())] for h in range(life.get_height())]

    if life.counter != 0:
        life.form_new_generation()  # Генерация следующего поколения
    life.counter += 1

    for i in range(life.get_height()):
        for j in range(life.get_width()):
            if life.world[i][j]:
                cell[i][j] = "cell living-cell"
            elif life.world[i][j] == 0 and life.old_world[i][j] == 1:
                cell[i][j] = "cell dead-cell"
            else:
                cell[i][j] = "cell"

    return json.dumps({'cell': cell, 'counter': life.counter})


@app.route('/live')
def live():
    """Присвоение переменной life раннее созданного мира и отправка в шаблон live.html"""
    life = GameOfLife()
    return render_template('live.html', life=life)


if __name__ == '__main__':
    app.run(host='127.0.0.0', port=5000)
