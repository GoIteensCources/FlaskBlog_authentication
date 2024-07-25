from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager

app = Flask(__name__)

postgresql_db = "postgresql+psycopg://postgres:pg@localhost:5432/blog_db"
sqlite_db = "sqlite:///blog.db"

app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = postgresql_db
app.config["SECRET_KEY"] = 'kflkjdds;l;ldk;fl'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
# login_manager.login_message = "NEED LOGIN"
# login_manager.init_app(app)


from app.models import User


@login_manager.user_loader
def load_user(user_id: int):
    user = db.session.execute(db.select(User).where(User.id == int(user_id))).scalar()
    print(user)
    return user


from app.routes import *
