from flask import Flask
from starter import *
app = Flask(__name__)

@app.route('/start-process')
def start_process():
  print("start-process")
  main("hashes.txt", 5)  
  return 'Server Works!'
@app.route('/')
def index():
  return 'Server Works!'  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'