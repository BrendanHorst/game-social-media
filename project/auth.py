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

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = get_db()
        account = cursor.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

        if account:
            msg = 'Account already exists!'
        # --Note: I don't know where you got 're' from, so I'm commenting this out for now so it doesn't break
        #
        #elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        #    msg = 'Invalid email address!'
        #elif not re.match(r'[A-Za-z0-9]+', username):
        #    msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:

            cursor.execute('INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, 1)', (username, password, email,))
            cursor.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':

        msg = 'Please fill out the form!'

    return render_template('layouts/register.html')




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
        g.user = user


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

def ban_check(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is not None:
            if g.user['role'] is 2:
                return redirect(url_for('admin.banned'))
        return view(**kwargs)
    return wrapped_view

def admin_check(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user['role'] is not 1:
            return redirect(url_for('index'))
        return view(**kwargs)
    return wrapped_view
