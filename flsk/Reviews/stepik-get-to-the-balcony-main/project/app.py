from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

from forms import ProfileForm
from matrix import Matrix


class Config(object):
    SECRET_KEY = 'key'


app = Flask(__name__)

app.config.from_object(Config)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def index():
    global game
    game = Matrix()
    return render_template('index.html')


@app.route("/surprise/", methods=["GET", "POST"])
def surprise():
    return render_template('surprise.html')


@app.route("/game/", methods=["GET", "POST"])
def game():
    if isinstance(game, Matrix):
        form = ProfileForm()
        if form.validate_on_submit():
            side_of_the_world = form.side_of_the_world.data
            step = form.step.data
            submit = form.submit.data
            new_location, flag = game.movement(side_of_the_world, step)
            if new_location is not None and new_location != 'Балкон' and flag is True:
                return render_template(
                    'game.html',
                    form=form,
                    side_of_the_world=side_of_the_world,
                    step=step, submit=submit,
                    location=new_location
                )
            elif new_location is not None and new_location == 'Балкон':
                return redirect(url_for('surprise'))
            else:
                return render_template(
                    'game.html',
                    form=form,
                    side_of_the_world=side_of_the_world,
                    step=step, submit=submit,
                    warning='Вы уперлись в стену!',
                    location=new_location
                )
        else:
            return render_template(
                'game.html',
                form=form,
                instance='Вам нужно выбраться на балкон!',
                surprise='Там вас ждет награда!',
                location='Вы находитесь в "Подземелье".')
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
