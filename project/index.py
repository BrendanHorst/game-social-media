from flask import Flask, render_template, g, redirect, url_for, Blueprint, request, session

from .db import get_db

from . import db

bp = Blueprint("main", __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('layouts/index.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('id')
    db=get_db()

    if user_id is None:
        g.user = None
    else:
        user = db.execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        )
        g.user = user.fetchone()
