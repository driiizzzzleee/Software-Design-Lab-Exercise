"""
File: doctorclienthandler.py

"""
from codecs import decode
from threading import Thread

import self as self
from doctor import Doctor

BUFSIZE = 1024
CODE = "ascii"

class DoctorClientHandler(Thread):
 """Handles a session between a doctor and a patient."""
def __init__(self, client):
      Thread.__init__(self)
      self.client = client
      self.dr = Doctor()
def run(self):
 self.client.send(bytes(self.dr.greeting(),CODE()))
while True:
    message = decode(self.client.recv(BUFSIZE),CODE)
    if not message:
        self.client.close(print("Client disconnected"))
    break
else:
      self.client.send(bytes(self.dr.reply(message),CODE()))
