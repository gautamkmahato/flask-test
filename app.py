from flask import Flask
from gevent.pywsgi import WSGIServer
from dotenv import load_dotenv
import os

app = Flask(__name__)

PORT = 5000

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# if __name__ == '__main__':
#     http_server = WSGIServer(('0.0.0.0', PORT), app)
#     http_server.serve_forever()