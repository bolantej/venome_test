from src.api.users import login, signup, delete_user, get_user_id
from src.api_types import *

def test_example():
    assert 1

#attempt to login to the venome admin account
#def test_login():
#    assert login({"admin@venome.cqls.oregonstate.edu", "password"}).token != ""

#attempt to create and delete an account
def test_account_creation():
    body = SignupBody(username="test", email="test@test.com", password="test")
    response = signup(body)
    assert response.error == ""
    id = get_user_id("test")
    assert delete_user(id) == 0
