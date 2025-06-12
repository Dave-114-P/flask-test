from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

login.login_view = 'login'

# from app import routes, models 必须放在 app、db、migrate、login 等都初始化之后（通常是文件最后），这样 Flask 应用才能正常工作。
from app import routes, models

