from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
  return render_template('madlibfe.html', prompts=story.prompts)

@app.route('/story')
def display_story():

  text = story.generate(request.args)

  return render_template("story.html", text = text)