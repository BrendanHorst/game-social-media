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

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:

            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':

        msg = 'Please fill out the form!'

    return render_template('layouts/auth.html')




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
