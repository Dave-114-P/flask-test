
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import app, db
from app.models import User
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username':'DD'}
    # return '''
    # <html>
    #     <head>
    #         <title>Home Page - Microblog</title>
    #     </head>
    #     <body>
    #         <h1>Hello. '''+ user['username']+'''</h1>
    #     </body>
    # </html>'''
    return render_template('index.html', title='HOME',user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))