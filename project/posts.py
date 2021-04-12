import sqlite3

from flask import Blueprint, g, render_template, request

from project.db import get_db
from project.auth import ban_check
bp = Blueprint('posts', __name__)

@bp.route('/<int:game_id>/posts', methods=('GET', 'POST'))
@ban_check
def post_list(game_id):

    db = get_db()

    posts = db.execute("SELECT username, users.id, title, body FROM posts JOIN users ON user_id=users.id WHERE game_id = ?", str(game_id)).fetchall()
    game = db.execute("SELECT * FROM games WHERE id = ?", str(game_id)).fetchone()

    return render_template("layouts/posts.html", posts=posts, game=game)

@bp.route('/user/<int:user_id>/', methods=('GET',))
def profile(user_id):

    db = get_db()

    user = db.execute("SELECT username FROM users WHERE id = ?", str(user_id)).fetchone()

    posts = db.execute("SELECT posts.title, body, games.title AS game, games.id FROM posts JOIN games ON posts.game_id=games.id WHERE posts.user_id = ?", str(user_id)).fetchall()

    return render_template("layouts/profile.html", posts=posts, user=user)
