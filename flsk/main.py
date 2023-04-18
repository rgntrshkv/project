from flask import Flask
import configparser as cp

config = cp.ConfigParser()
config.read('config.ini')
p_host = config['DEFAULT']['host']
p_port = config['DEFAULT']['port']

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World. It is Regina'

if __name__ == "__main__":
    app.run(host = p_host, port = p_port)