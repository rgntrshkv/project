import flask as flsk
import configparser as cp
from house import House
from form import MoveForm, HouseForm
from config import Config

config = cp.ConfigParser()
config.read('config.ini')
p_host = config['DEFAULT']['host']
p_port = config['DEFAULT']['port']

app = flsk.Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods = ["POST", "GET"])
def index():
    form = HouseForm()
    return flsk.render_template('index.html', form=form)

@app.route('/house', methods = ["POST", "GET"])
def house():
    h = flsk.request.form.get('height')
    w = flsk.request.form.get('weight')
    if not h:
        h = 2
    if not w:
        w = 3
    HS = House(int(w),int(h))
    return flsk.render_template('house.html', HS=HS)

@app.route('/house_cur', methods = ["POST", "GET"])
def house_cur():
    HS = House()
    return flsk.render_template('house.html', HS=HS)

@app.route('/move', methods = ["POST", "GET"])
def move():
    HS = House()
    mform = MoveForm()
    dir = flsk.request.form.get('way')
    n_st = flsk.request.form.get('number_steps')
    if (not dir) or (not n_st):
        return flsk.render_template('move.html', mform=mform)
    else:
        msg = HS.move(int(dir),int(n_st))
        return flsk.render_template('move.html', mform=mform, msg=msg)

if __name__ == "__main__":
    app.run(host = p_host, port = p_port, debug = 0)