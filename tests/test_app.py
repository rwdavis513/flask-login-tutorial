import pytest
from app import app
from flask_app import init_db


def setup():
    init_db()
    print("Created database")


@pytest.fixture
def client(request):

    client = app.test_client()

    # def teardown():
    #     os.close(login_app.config['DB_FD'])
    #     os.unlink(login_app.config['DATABASE'])
    # request.addfinalizer(teardown)

    return client


def test_isAlive(client):
    response = client.get('/')
    assert response.status_code == 200


def test_signup_post(client):
    with app.app_context():
        response = client.post('/signup', data=dict(email="test@email.com",
                                                password="123456",
                                                csrf_token=client.csrf_token), follow_redirects=True)
    print(response.data)
    assert response.status_code == 200