# pylint: disable=missing-docstring

from flask import Flask, render_template, request
from flask_session import Session
from longest_word.game import Game

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Yohann's code
# SESSION_TYPE = 'redis'
# app.config.from_object(__name__)
# Session(app)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid, score = 0)



@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    if is_valid:
        score += 1
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word, score = score)
