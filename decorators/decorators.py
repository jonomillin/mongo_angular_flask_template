from lib.tools import *
from flask import Blueprint, render_template, abort, redirect, Response, jsonify, send_from_directory
from functools import wraps
from flask import g, request, redirect, url_for

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not logged_in():
            return redirect('/signin')
        return f(*args, **kwargs)
    return decorated_function

def require_authorization(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not logged_in():
            abort(401)
        return f(*args, **kwargs)
    return decorated_function