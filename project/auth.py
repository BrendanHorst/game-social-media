import functools
import bcrypt
from .db import get_db

from flask import (
Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import db
bp = Blueprint("auth", __name__)

#def hash_pass(password):
#    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
#    return hashed

@bp.route('/register', methods=('GET', 'POST'))
def register():

    msg = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        msg = 'Please fill out the form!'
        db = get_db()
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

        msg = 'You have successfully registered!'


    return render_template('register.html', msg=msg)




            msg = 'You have successfully registered!'

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        if user is None or password != user['password']:
            error = 'Incorrect email or password!'

        if error is None:
            session.clear()
            session['id'] = user['id']
            return redirect(url_for('index'))
        flash(error)

    return render_template('layouts/auth.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('id')
    db=get_db()

    if user_id is None:
        g.user = None
    else:
        user = db.execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()
        print(user['username'])
        g.user = user


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
