from app import app, db
from app.models import Post, User
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)


def create_mock_data():
    u = User(nickname="admin", email="admin@ex.com", password=generate_password_hash("admin"))

    p1 = Post(title="Post 1", content="some content for post 1", user=u)
    p2 = Post(title="Post 2", content="some content for post 2", user=u)
    p3 = Post(title="Post 3", content="some content for post 3", user=u)

    db.session.add_all([p1,p2,p3])
    db.session.commit()

    print("Data created")


with app.app_context():
    db.create_all()
    print("Create database")
    create_mock_data()
