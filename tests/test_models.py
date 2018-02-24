from models import User


def test_user_class():
    u = User(email="test1234@gmail.com", password="mysecretpassword")
