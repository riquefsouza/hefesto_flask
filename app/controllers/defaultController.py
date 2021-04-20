from app import app, lm
from flask import  render_template, redirect, url_for
from app.services.admin.admParameterCategoryService import AdmParameterCategoryService
from app.services.admin.admUserService import login
from flask_login import logout_user
from app.models.user import User

from app.forms.loginForm import LoginForm

admParameterCategoryService = AdmParameterCategoryService()

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ["GET", "POST"])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
       if login(loginForm):
           return redirect(url_for("index"))
    return render_template('login.html', loginForm=loginForm)

@app.route("/logout")
def logout():
    logout_user()
    #flash("Logged out.")
    return redirect(url_for("index"))

@app.route('/about')
def about():
    return render_template('private/about.html')

@app.route('/changePassword')
def changePassword():
    return render_template('private/changePassword.html')

@app.route('/admParameterCategoryView')
def admParameterCategoryView():
    return render_template('private/admParameterCategory/listAdmParameterCategory.html', 
    lista = admParameterCategoryService)
