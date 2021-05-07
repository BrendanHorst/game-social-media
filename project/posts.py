import sqlite3

from flask import Blueprint, g, render_template, request

from project.db import get_db
from project.auth import ban_check
bp = Blueprint('posts', __name__)

@bp.route('/<int:game_id>/posts', methods=('GET', 'POST'))
@ban_check
def post_list(game_id):

    db = get_db()

    posts = db.execute("SELECT posts.id AS post_id, username, users.id, title, body FROM posts JOIN users ON user_id=users.id WHERE game_id = ?", str(game_id)).fetchall()
    game = db.execute("SELECT * FROM games WHERE id = ?", str(game_id)).fetchone()

    return render_template("layouts/posts.html", posts=posts, game=game)


@bp.route('/<int:game_id>/posts/<int:post_id>', methods=('GET', 'POST'))
def comments(game_id, post_id):
    """Displays a specific post and handles creating and viewing comments on that post"""

    db = get_db()

    if (request.method == 'POST') and (g.user != None):
        #If there is a post request and the user is logged in, insert their comment into the database

        comment = request.form['comment']

        db.execute("INSERT INTO comments(user_id, post_id, comment_id, content, hidden) VALUES (?, ?, NULL, ?, 0)", (g.user['id'], post_id, comment))


    #Retrieve all of the necessary data for the page
    post = db.execute("SELECT username, users.id, title, body, game_id FROM posts JOIN users ON user_id=users.id WHERE posts.id = ?", str(post_id)).fetchone()

    game = db.execute("SELECT id, title FROM games WHERE id = ?", str(post['game_id'])).fetchone()

    comments = db.execute("SELECT content, username, users.id FROM comments JOIN users ON user_id=users.id WHERE post_id = ?", str(post_id)).fetchall()

    return render_template("layouts/comments.html", post=post, comments=comments, game=game)


@bp.route('/user/<int:user_id>/', methods=('GET',))
@ban_check
def profile(user_id):

    db = get_db()

    user = db.execute("SELECT username FROM users WHERE id = ?", str(user_id)).fetchone()

    posts = db.execute("SELECT posts.title, body, games.title AS game, games.id FROM posts JOIN games ON posts.game_id=games.id WHERE posts.user_id = ?", str(user_id)).fetchall()

    return render_template("layouts/profile.html", posts=posts, user=user)
