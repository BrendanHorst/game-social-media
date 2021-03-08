import sqlite3

from flask import Blueprint, g, render_template, request

from project.db import get_db

bp = Blueprint('games', __name__)

@bp.route('/', methods=('GET', 'POST'))
def game_list():

    genre = "0"

    if request.method == 'POST':

        genre = request.form['genre']
        print(genre)

    db = get_db()

    if genre != "0":
        games = db.execute(
            'SELECT title FROM games JOIN games_genres ON games.id = game_id WHERE genre_id = ?', genre
            ).fetchall()

    else:
        games = db.execute(
            'SELECT title FROM games'
            ).fetchall()

    genres = db.execute('SELECT * FROM genres').fetchall()

    return render_template('layouts/game-list.html', games=games, genres=genres)
