from typing import Optional
import sqlalchemy as sql
import sqlalchemy.orm as sqlo
from app import login
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model):
    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    username: sqlo.Mapped[str] = sqlo.mapped_column(sql.String(64), index=True, unique=True)
    email: sqlo.Mapped[str] = sqlo.mapped_column(sql.String(120), index=True, unique=True)
    password_hash: sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sql.String(256))
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    # password_hash = db.Column(db.String(256))


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User{}>'.format(self.username)
    
class User(UserMixin, db.Model):
    pass

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))