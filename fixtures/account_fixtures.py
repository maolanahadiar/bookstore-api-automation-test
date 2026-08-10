import pytest
from http import HTTPStatus
from services.account_service import AccountService
from utils.data_generator import DataGenerator

account_service = AccountService()

@pytest.fixture(scope="session")
def created_user():
    """Create a user for pre-condition test that require an account"""

    username = DataGenerator.username()
    password = DataGenerator.password()

    response = account_service.register(
        username=username,
        password=password,
    )

    assert response.status_code == HTTPStatus.CREATED

    body = response.json()

    return {
        "user_id": body["userID"],
        "username": body["username"],
        "password": password,
    }

@pytest.fixture(scope="session")
def user_token(created_user):
    """Generate a token for the test user"""

    response = account_service.generate_token(
        username=created_user["username"],
        password=created_user["password"],
    )

    assert response.status_code == HTTPStatus.OK

    return response.json()["token"]

@pytest.fixture
def delete_user():
    """Create a user specifically for test delete account"""

    username = DataGenerator.username()
    password = DataGenerator.password()

    response = account_service.register(
        username=username,
        password=password,
    )

    assert response.status_code == HTTPStatus.CREATED

    body = response.json()

    return {
        "user_id": body["userID"],
        "username": username,
        "password": password,
    }
    
@pytest.fixture
def delete_user_token(delete_user):
    """Generate a token specifically for test delete account"""

    response = account_service.generate_token(
        username=delete_user["username"],
        password=delete_user["password"],
    )

    assert response.status_code == HTTPStatus.OK

    return response.json()["token"]