import pytest
from password_checking import User, Password


@pytest.fixture
def user():
    user = User()
    user.password = "1234"
    return user

def test_password_hash_changed(user):
    original_hash = user.password_hash
    user.password = "aadsfasedf"
    assert original_hash != user.password_hash

def test_password_not_eq(user):
    user.password = "1234"
    assert user.password != "lol wtf"

def test_password_eq(user):
    user.password = "1234"
    assert user.password == "1234"
