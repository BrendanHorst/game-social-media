import sqlite3

from flask import Blueprint, g, render_template, request

from project.db import get_db
from project.auth import ban_check
bp = Blueprint('games', __name__)

@bp.route('/', methods=('GET', 'POST'))
@ban_check
def game_list():

    genre = "0"

    if request.method == 'POST':

        genre = request.form['genre']

    db = get_db()

    if genre != "0":
        games = db.execute(
            'SELECT games.id, title FROM games JOIN games_genres ON games.id = game_id WHERE genre_id = ?', genre
            ).fetchall()

    else:
        games = db.execute(
            'SELECT id, title FROM games'
            ).fetchall()

    genres = db.execute('SELECT * FROM genres').fetchall()

    return render_template('layouts/game-list.html', games=games, genres=genres)
