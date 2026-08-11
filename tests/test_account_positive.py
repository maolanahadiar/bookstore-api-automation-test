import allure
from assertpy import assert_that
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
        assert_that(response.status_code).is_equal_to(HTTPStatus.CREATED)
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert_that(body).contains_key("userID")
        assert_that(body["username"]).is_equal_to(username)
        
    with allure.step("Verify response data type"):
        assert_that(body["userID"]).is_instance_of(str)
        assert_that(body["username"]).is_instance_of(str)
        
@allure.title("User can login using valid credential successfully")        
def test_login_success(created_user):
    
    with allure.step("Send request to login"):
        response = account_service.login(
            username=created_user["username"],
            password=created_user["password"]
        )

    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.OK)

@allure.title("User can generate token successfully")        
def test_generate_token_success(created_user):
    
    with allure.step("Send request to generate token"):
        response = account_service.generate_token(
            username=created_user["username"],
            password=created_user["password"]
        )
        
    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert_that(body["status"]).is_equal_to(EXPECTED_MESSAGES["token_success"]["status"])
        assert_that(body["result"]).is_equal_to(EXPECTED_MESSAGES["token_success"]["result"])
    
    with allure.step("Verify response data type"):
        assert_that(body["token"]).is_instance_of(str)
        assert_that(body["expires"]).is_instance_of(str)
        
@allure.title("User can get account detail succesfully")        
def test_account_detail_success(created_user, user_token):
    
    with allure.step("Send request to get account"):
        response = account_service.get_account(
            user_id=created_user["user_id"],
            token=user_token
        )
    
    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert_that(body).contains_key("userId")
        assert_that(body["username"]).is_equal_to(created_user["username"])
        
    with allure.step("Verify response data type"):
        assert_that(body["userId"]).is_instance_of(str)
        assert_that(body["username"]).is_instance_of(str)
        
@allure.title("User can delete account successfully")        
def test_delete_account_success(delete_user, delete_user_token):
    
    with allure.step("Send request to delete account"):
        response = account_service.delete_account(
            user_id=delete_user["user_id"],
            token=delete_user_token
        )

    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.NO_CONTENT)