import sqlite3

from flask import Blueprint, g, render_template, request

from project.db import get_db

bp = Blueprint('posts', __name__)

@bp.route('/<int:game_id>/posts', methods=('GET', 'POST'))
def post_list(game_id):
    pass
