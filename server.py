#!/usr/bin/env python

from speech_synthesizer import speech_synthesizer as ss
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)

    self.send_header('Content-type','text/html')
    self.end_headers()

    gizmo = ss.speech_syn('GIzmo', 'Hi');

    message = gizmo.reply("how are you")
    print('------------------------------------------------> ', message[0])

    self.wfile.write(bytes(message[0], 'utf8'))
    return

  def do_POST(self):
    print(self.path)
    length = int(self.headers['Content-Length'])
    my_bytes_value = self.rfile.read(length)
    my_json = my_bytes_value.decode('utf8').replace("'", '"')



    data = json.loads(my_json)
    print(data['text'])
    gizmo = ss.speech_syn('GIzmo', 'Hi');

    message = gizmo.reply(data['text'])
    msg = "".join(str(x) for x in message)
    print(type(msg))
    print(type(message))

    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.send_header('Location', '/reply')
    self.end_headers()
    self.wfile.write(bytes(msg, "utf8"))


def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 5000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...', 5000)
  httpd.serve_forever()


run()
