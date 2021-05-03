import functools
import bcrypt
from .db import get_db

from project.auth import ban_check , admin_check

from flask import (
Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import db
bp = Blueprint("admin", __name__)

@bp.route('/admin', methods=('GET', 'POST'))
@admin_check
def admin():
    if request.method == 'POST' and 'username' in request.form:
        banname = request.form['username']
        db = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (banname,)
        ).fetchone()
        ban = user['username']
        db.execute(
        'UPDATE users SET role = ?'
        'WHERE username = ?', (2, ban)
        )
        db.commit()
    return render_template('layouts/admin.html')
@bp.route('/banned', methods=('GET',))
def banned():
    return render_template('layouts/banned.html')
