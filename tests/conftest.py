import pytest
from app import create_app
from app.extensions import db
from app.models import User

@pytest.fixture()
def app(tmp_path):
    app=create_app({'TESTING':True,'SECRET_KEY':'test','SQLALCHEMY_DATABASE_URI':f"sqlite:///{tmp_path/'test.db'}",'WTF_CSRF_ENABLED':False})
    with app.app_context(): db.drop_all(); db.create_all(); yield app; db.session.remove(); db.drop_all()

@pytest.fixture()
def client(app): return app.test_client()

@pytest.fixture()
def student(app):
    with app.app_context():
        u=User(name='Test Student',email='student@test.local',role='student');u.set_password('Password123');db.session.add(u);db.session.commit();return u.id

@pytest.fixture()
def admin(app):
    with app.app_context():
        u=User(name='Admin',email='admin@test.local',role='admin');u.set_password('Password123');db.session.add(u);db.session.commit();return u.id

def login(client,email='student@test.local'):
    return client.post('/login',data={'email':email,'password':'Password123'},follow_redirects=True)
