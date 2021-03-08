import sqlite3

from flask import Blueprint, g, render_template

from project.db import get_db

bp = Blueprint('games', __name__)

@bp.route('/', methods=('GET', 'POST'))
def game_list():

    db = get_db()

    games = db.execute('SELECT * FROM games').fetchall()

    genres = db.execute('SELECT * FROM genres').fetchall()

    return render_template('/game-list.html', games=games, genres=genres)
