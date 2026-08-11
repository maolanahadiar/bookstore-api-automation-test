import allure
from assertpy import assert_that
from http import HTTPStatus
from services.account_service import AccountService
from testdata.account_data import CREDENTIALS
from testdata.auth_data import TOKEN
from testdata.messages import EXPECTED_MESSAGES

account_service = AccountService()

@allure.title("User cannot register with empty required fields")
def test_register_with_empty_fields():
    
    with allure.step("Send request to register with empty required fields"):
        
        response = account_service.register(
            username=CREDENTIALS["empty"]["username"],
            password=CREDENTIALS["empty"]["password"]
        )
        
    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert_that(body["code"]).is_equal_to(EXPECTED_MESSAGES["empty_field"]["code"])
        assert_that(body["message"]).is_equal_to(EXPECTED_MESSAGES["empty_field"]["message"])
        
@allure.title("User cannot login using invalid credentials")        
def test_login_using_invalid_credentials():
    
    with allure.step("Send request to login using invalid credentials"):
        response = account_service.login(
            username=CREDENTIALS["invalid"]["username"],
            password=CREDENTIALS["invalid"]["password"]
        )

    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert_that(body["code"]).is_equal_to(EXPECTED_MESSAGES["invalid_credentials"]["code"])
        assert_that(body["message"]).is_equal_to(EXPECTED_MESSAGES["invalid_credentials"]["message"])
        
@allure.title("User cannot generate token with empty required fields")        
def test_generate_token_with_empty_fields():
    
    with allure.step("Send request to generate token with empty required fields"):
        response = account_service.generate_token(
            username=CREDENTIALS["empty"]["username"],
            password=CREDENTIALS["empty"]["password"]
        )
        
    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert_that(body["code"]).is_equal_to(EXPECTED_MESSAGES["empty_field"]["code"])
        assert_that(body["message"]).is_equal_to(EXPECTED_MESSAGES["empty_field"]["message"])

@allure.title("User cannot get account detail using invalid user id")        
def test_account_detail_using_invalid_user_id(delete_user_token):
    
    with allure.step("Send request to get account using invalid user id"):
        response = account_service.get_account(
            user_id=CREDENTIALS["invalid"]["user_id"],
            token=delete_user_token
        )
    
    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.UNAUTHORIZED)
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert_that(body["code"]).is_equal_to(EXPECTED_MESSAGES["invalid_user_id"]["code"])
        assert_that(body["message"]).is_equal_to(EXPECTED_MESSAGES["invalid_user_id"]["message"])
        
@allure.title("User cannot delete using invalid token")        
def test_delete_account_using_invalid_token(delete_user):
    
    with allure.step("Send request to delete account using invalid token"):
        response = account_service.delete_account(
            user_id=delete_user["user_id"],
            token=TOKEN["invalid"]
        )

    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.UNAUTHORIZED)
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert_that(body["code"]).is_equal_to(EXPECTED_MESSAGES["unauthorized"]["code"])
        assert_that(body["message"]).is_equal_to(EXPECTED_MESSAGES["unauthorized"]["message"])