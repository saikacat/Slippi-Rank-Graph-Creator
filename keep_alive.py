from flask import Flask, render_template, request
from threading import Thread
from listofplayers import *
app = Flask('')

@app.route('/')
def home():
  with open("listofplayers.py", "r") as file:
        data = file.read()
  return data

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target = run)
    t.start()