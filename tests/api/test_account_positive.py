import allure
from http import HTTPStatus
from services.account_service import AccountService
from utils.data_generator import DataGenerator
from testdata.messages import EXPECTED_MESSAGES

account_service = AccountService()

@allure.title("User can register new account successfully")
def test_register_success():
    
    with allure.step("Send request to register new account"):
        
        username = DataGenerator.username()
        password = DataGenerator.password()
        
        response = account_service.register(
            username=username,
            password=password
        )
        
    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.CREATED
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert "userID" in body
        assert body["username"] == username
        
    with allure.step("Verify response data type"):
        assert isinstance(body["userID"], str)
        assert isinstance(body["username"], str)
        
@allure.title("User can login with valid credential successfully")        
def test_login_success(created_user):
    
    with allure.step("Send request to login"):
        response = account_service.login(
            username=created_user["username"],
            password=created_user["password"]
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK

@allure.title("User can generate token successfully")        
def test_generate_token_success(created_user):
    
    with allure.step("Send request to generate token"):
        response = account_service.generate_token(
            username=created_user["username"],
            password=created_user["password"]
        )
        
    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert body["status"] == EXPECTED_MESSAGES["token_success"]["status"]
        assert body["result"] == EXPECTED_MESSAGES["token_success"]["result"]
    
    with allure.step("Verify response data type"):
        assert isinstance(body["token"], str)
        assert isinstance(body["expires"], str)
        
@allure.title("User can get account detail succesfully")        
def test_account_detail_success(created_user, user_token):
    
    with allure.step("Send request to get account"):
        response = account_service.get_account(
            user_id=created_user["user_id"],
            token=user_token
        )
    
    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK
        
    with allure.step("Verify response body"):
        body = response.json()

        assert "userId" in body
        assert body["username"] == created_user["username"]
        
    with allure.step("Verify response data type"):
        assert isinstance(body["userId"], str)
        assert isinstance(body["username"], str)
        
@allure.title("User can delete account successfully")        
def test_delete_account_success(delete_user, delete_user_token):
    
    with allure.step("Send request to delete account"):
        response = account_service.delete_account(
            user_id=delete_user["user_id"],
            token=delete_user_token
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.NO_CONTENT