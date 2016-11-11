#!/usr/bin/env python

import flask_socketio
import socket
from os import environ

from flask import Flask
# from OpenSSL import SSL

app = Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.route("/")
def hello():
    return "Hello World!"


def main():
  print "Web_app room location: "
  HOST = environ.get('SERVER_HOST', 'localhost')
  try:
      PORT = int(environ.get('SERVER_PORT', '5555'))
  except ValueError:
      PORT = 5555
  socketio.run(app, debug=False, host=HOST, port=PORT)

if __name__ == '__main__':
  main()
