import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # print('inside config')
    # ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
    or 'sqlite:///' + os.path.join(base_dir, 'app.db')
    # print(SQLALCHEMY_DATABASE_URI)