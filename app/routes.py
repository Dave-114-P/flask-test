from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
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
    return render_template('login.html', title='LOGIN')