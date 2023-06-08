import flask as flsk
import configparser as cp
from game_of_life import GameOfLife
from form import GOFForm
from config import Config

config = cp.ConfigParser()
config.read('config.ini')
p_host = config['DEFAULT']['host']
p_port = config['DEFAULT']['port']

app = flsk.Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods = ["POST", "GET"])
def index():
    form = GOFForm()
    return flsk.render_template('index.html', form=form)

@app.route('/live', methods = ['POST', 'GET'])
def live():
    h = flsk.request.form.get('height')
    w = flsk.request.form.get('weight')
    oldwf = flsk.request.form.get('oldw_flag')
    tr = flsk.request.form.get('time_reload')
    if not h:
        h = 20
    if not w:
        w = 20
    if not oldwf:
        oldwf = 1
    if not tr:
        tr = 1000
    GOL = GameOfLife(int(h),int(w))
    GOL.counter+=1
    if GOL.counter > 1:
        GOL.form_new_generation()
    return flsk.render_template('live.html', GOL=GOL, tr=tr, oldwf=oldwf)

@app.route('/live_loop', methods = ['POST', 'GET'])
def live_loop():
    GOL = GameOfLife()
    args = flsk.request.args
    print(args)
    oldwf = args['oldwf1']
    tr = args['tr1']
    GOL.counter+=1
    if GOL.counter > 1:
        GOL.form_new_generation()
    return flsk.render_template('live.html', GOL=GOL, tr=tr, oldwf=oldwf)

if __name__ == "__main__":
    app.run(host = p_host, port = p_port, debug = 0)