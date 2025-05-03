from src.api.users import signup
from src.api_types import SignupBody, SignupResponse


#attempt to create an account
def test_account_creation():
    body = SignupBody(username="test", email="test@test.com", password="test")
    response: SignupResponse = signup(body)
    assert response.error == ""
