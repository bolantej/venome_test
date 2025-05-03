from src.api.users import signup, delete_user, get_user_id, get_user, delete_user
from src.api_types import SignupBody, SignupResponse, UserResponse, UserIDResponse


#attempt to create an account
def test_account_creation():
    body = SignupBody(username="test_user2", email="test@email.com", password="test")
    response: SignupResponse = signup(body)
    assert response.error == ""
    id: UserIDResponse = get_user_id("test_user2")
    assert id.id != -1

def test_get_user():
    response: UserResponse = get_user(1)
    assert response.username == "test_user1"
    assert response.email == "test@test.com"

def test_account_deletion():
    scope: Scope = {
        "type": "http",
        "headers": [(b"authorization", token.encode())],
    }
    delete_user(1, Request(scope))
    response: UserResponse = get_user(1)
    assert response.username == ""
    assert response.email == ""
