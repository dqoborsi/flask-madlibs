from flask import Flask
from stories import *

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('madlibfe.html')