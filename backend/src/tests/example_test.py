from src.api.users import signup, get_user_id, get_user, login, delete_user
from src.api_types import (
    SignupBody,
    SignupResponse,
    UserResponse,
    UserIDResponse,
    LoginBody,
    LoginResponse,
)
from FastApi.requests import Request, Scope
from src.auth import generate_auth_token

def create_dummy_request(auth_token: str) -> Request:
    scope: Scope = {
        "type": "http",
        "headers": [
            (b"authorization", f"Bearer {auth_token}".encode("utf-8")),
        ],
        "method": "GET",
        "path": "/",
    }
    return Request(scope)


#attempt to create an account
def test_account_creation():
    body = SignupBody(username="test_user2", email="test@email.com", password="test")
    response: SignupResponse = signup(body)
    assert response.error == ""
    id: UserIDResponse = get_user_id("test_user2")
    assert id.id != -1


def test_login():
    body = LoginBody(email="test@email.com", password="test")
    response: LoginResponse = login(body)
    assert response.user_id != 0
    assert response.token != ""


def test_get_user():
    response: UserResponse = get_user(1)
    assert response.username == "test_user1"
    assert response.email == "test@test.com"


def test_account_deletion():
    
    token = generate_auth_token("test@test.com", admin=True)
    req = create_dummy_request(token)
    delete_user(1, req)
    response: UserResponse = get_user(1)
    assert response.username == ""
    assert response.email == ""
