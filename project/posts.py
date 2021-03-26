import sqlite3

from flask import Blueprint, g, render_template, request

from project.db import get_db

bp = Blueprint('posts', __name__)

@bp.route('/<int:game_id>/posts', methods=('GET', 'POST'))
def post_list(game_id):

    db = get_db()

    posts = db.execute("SELECT username, title, body FROM posts JOIN users ON user_id=users.id WHERE game_id = ?", str(game_id)).fetchall()
    game = db.execute("SELECT * FROM games WHERE id = ?", str(game_id)).fetchone()

    return render_template("layouts/posts.html", posts=posts, game=game)