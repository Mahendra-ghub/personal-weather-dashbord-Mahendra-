
import sqlite3, jwt, datetime
from flask import request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from models import get_user_by_email, insert_user

SECRET_KEY = 'your_secret_key_here'

def register_user(form):
    email = form['email']
    password = form['password']
    location = form['location']
    if get_user_by_email(email):
        return 'Email already registered'
    hashed_pw = generate_password_hash(password)
    insert_user(email, hashed_pw, location)
    return redirect('/login')

def login_user(form):
    email = form['email']
    password = form['password']
    user = get_user_by_email(email)
    if not user or not check_password_hash(user['password'], password):
        return 'Invalid credentials'
    token = jwt.encode({
        'email': user['email'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm='HS256')
    return {'token': token}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token') or request.args.get('token') or session.get('token')
        if not token:
            return redirect('/login')
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user = get_user_by_email(data['email'])
        except:
            return redirect('/login')
        return f(user, *args, **kwargs)
    return decorated
