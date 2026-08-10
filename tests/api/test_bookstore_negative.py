import allure
from http import HTTPStatus
from services.bookstore_service import BookStoreService
from testdata.book_data import BOOKS
from testdata.auth_data import TOKENS
from testdata.messages import EXPECTED_MESSAGES

book_service = BookStoreService()

@allure.title("User cannot add book without token")
def test_add_book_without_token(created_user):

    with allure.step("Send request to add book without token"):
        response = book_service.add_book(
            user_id=created_user["user_id"],
            isbn=BOOKS["existing"]["isbn"],
            token=TOKENS["empty_token"],
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.UNAUTHORIZED
    
    with allure.step("Verify response body"):
        body = response.json()
        
        assert body["code"] == EXPECTED_MESSAGES["unauthorized"]["code"]
        assert body["message"] == EXPECTED_MESSAGES["unauthorized"]["message"]
        
@allure.title("User cannot retrieve specific book using invalid ISBN")
def test_get_book_invalid_isbn():

    with allure.step(f"Send request to retrieve book using invalid ISBN {BOOKS["invalid"]["isbn"]}"):
        response = book_service.get_book_by_isbn(BOOKS["invalid"]["isbn"])

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.BAD_REQUEST
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert body["code"] == EXPECTED_MESSAGES["invalid_isbn"]["code"]
        assert body["message"] == EXPECTED_MESSAGES["invalid_isbn"]["message"]
        
@allure.title("User cannot add duplicate book")
def test_add_duplicate_book(created_user, user_token):

    with allure.step("Send first request to add book as initial data"):
        first_response = book_service.add_book(
            user_id=created_user["user_id"],
            isbn=BOOKS["existing"]["isbn"],
            token=user_token,
        )

        assert first_response.status_code == HTTPStatus.CREATED

    try:
        with allure.step("Send second request to add same book"):
            second_response = book_service.add_book(
                user_id=created_user["user_id"],
                isbn=BOOKS["existing"]["isbn"],
                token=user_token,
            )

        with allure.step("Verify response status code"):
            assert second_response.status_code == HTTPStatus.BAD_REQUEST
            
        with allure.step("Verify response body"):
            body = second_response.json()

            assert body["code"] == EXPECTED_MESSAGES["duplicate_book"]["code"]
            assert body["message"] == EXPECTED_MESSAGES["duplicate_book"]["message"]

    finally:
        with allure.step("Remove first book"):
            book_service.delete_book(
                user_id=created_user["user_id"],
                isbn=BOOKS["existing"]["isbn"],
                token=user_token,
            )
        
@allure.title("User cannot update book using invalid ISBN")
def test_update_invalid_book(created_user, user_token):

    with allure.step(f"Send request to update book using invalid ISBN {BOOKS["invalid"]["isbn"]}"):
        response = book_service.update_book(
            existing_isbn=BOOKS["existing"]["isbn"],
            user_id=created_user["user_id"],
            new_isbn=BOOKS["invalid"]["isbn"],
            token=user_token,
        )
            
    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.BAD_REQUEST
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert body["code"] == EXPECTED_MESSAGES["invalid_isbn"]["code"]
        assert body["message"] == EXPECTED_MESSAGES["invalid_isbn"]["message"]
        
@allure.title("User cannot delete book using invalid token")
def test_delete_book_without_token(created_user):

    with allure.step("Send request to delete book using invalid token"):
        response = book_service.delete_book(
            user_id=created_user["user_id"],
            isbn=BOOKS["new"]["isbn"],
            token=TOKENS["invalid_token"],
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.UNAUTHORIZED
    
    with allure.step("Verify response body"):
        body = response.json()
        
        assert body["code"] == EXPECTED_MESSAGES["unauthorized"]["code"]
        assert body["message"] == EXPECTED_MESSAGES["unauthorized"]["message"]