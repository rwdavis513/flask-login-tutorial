import pytest
from login_app import app

@pytest.fixture
def client(request):

    client = app.test_client()

    # def teardown():
    #     os.close(login_app.config['DB_FD'])
    #     os.unlink(login_app.config['DATABASE'])
    # request.addfinalizer(teardown)

    return client


def test_isAlive():

    response = client.post('/')
    assert response.status_code == 200
