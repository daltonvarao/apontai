from functools import wraps
from flask import session, redirect, url_for, flash


def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not session.get('logged_in'):
            flash('É necessário fazer Login para fazer uma reclamação!','danger')
            return redirect(url_for('login.index_login'))
        return func(*args, **kwargs)
    return wrapper
