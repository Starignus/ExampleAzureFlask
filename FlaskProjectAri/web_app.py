#!/usr/bin/env python

import flask_socketio
import socket

from flask import Flask
# from OpenSSL import SSL
import sys

app = Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.route("/")
def hello():
    return "Hello World!"


# Function to get id in Linux, Windows, OS X, Python 2.x and Python 3
def get_local_ip():
  return ([l for l in (
  [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1],
  [[(s.connect(('8.8.8.8', 80)),
  s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
  socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

def main():
  print "Web_app room location: "
  socketio.run(app, debug=True, host=get_local_ip(), port=8080)

if __name__ == '__main__':
  main()
