import sqlite3

from flask import Blueprint, g, render_template

from project.db import get_db

bp = Blueprint('games', __name__, url_prefix='/games')

@bp.route('/list', methods=('GET', 'POST'))
def game_list():
    pass
