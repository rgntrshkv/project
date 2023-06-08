from enum import Enum

from flask import Flask, render_template, redirect, session, url_for, flash, request
from forms import ChoiceStep, Login
from choice_room import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
rooms_names = {Dungeon.__name__: Dungeon,
               Hallway.__name__: Hallway,
               Hall.__name__: Hall,
               Kitchen.__name__: Kitchen,
               Bedroom.__name__: Bedroom,
               Armoury.__name__: Armoury}


# class Way(Enum):
#     NORTH = 0
#     EAST = 1
#     SOUTH = 2
#     WEST = 3


@app.route('/', methods=['POST'])
def post_index():
    form = Login()
    if form.validate_on_submit():
        name = form.name.data
        flash(f"Добро пожаловать в игру {name}. Найдите балкон.")
        return redirect(url_for(get_game.__name__))
    else:
        raise RuntimeError("wrong form data")


@app.route('/', methods=['GET'])
def get_index():
    form = Login()
    return render_template('index.html', form=form)


@app.route('/game', methods=['GET'])
def get_game():
    form = ChoiceStep()
    if "room" not in session:
        session["room"] = Dungeon.__name__
    room_class = rooms_names[session["room"]]
    flash(room_class.message)
    return render_template("game.html", form=form)


@app.route('/game', methods=['POST'])
def post_game():
    form = ChoiceStep()
    way = form.way.data
    number_steps = form.number_steps.data
    room_name = session['room']
    room_class = rooms_names[room_name]
    room = room_class(way, number_steps)
    res = room.validate()
    if isinstance(res, type) and issubclass(res, Room):
        print("ok")
        session["room"] = res.__name__
        return redirect(url_for('post_game'))
    elif res == "win":
        session.clear()
        print("win")
        return redirect(url_for('win'))
    elif res == "error":
        print("error")
        flash("Выберите другую сторону света или убавьте шаг", "error")
        return redirect(url_for('post_game'))
    return render_template("game.html", form=form)


@app.route('/win')
def win():
    return render_template("win.html")


if __name__ == '__main__':
    app.run(debug=True)
