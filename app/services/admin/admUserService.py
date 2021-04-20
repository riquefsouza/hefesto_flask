from app import db
from app.models.user import User
from flask import flash
from flask_login import login_user

def findById(id):
    userList = User.query.filter_by(id=id).all()
    return userList

def insert(user):
    db.session.add(user)
    db.session.commit()
    return True

def update(user):
    db.session.add(user)
    db.session.commit()
    return True

def delete(user):
    db.session.delete(user)
    db.session.commit()
    return True

def login(loginForm):
    user = User.query.filter_by(username=loginForm.username.data).first()
    if user and user.password == loginForm.password.data:
        login_user(user)
        flash("Logged in.")
        return True
    else:
        flash("Invalid login.")
        return False
