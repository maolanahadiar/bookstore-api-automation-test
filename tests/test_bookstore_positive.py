import allure
from assertpy import assert_that
from http import HTTPStatus
from services.bookstore_service import BookStoreService
from utils.assertions import assert_book_schema
from testdata.book_data import BOOKS

book_service = BookStoreService()

@allure.title("User can add a book into collection")
def test_add_book_success(created_user, user_token):

    with allure.step("Send request to add a book"):
        response = book_service.add_book(
            user_id=created_user["user_id"],
            isbn=BOOKS["existing"]["isbn"],
            token=user_token,
        )

    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.CREATED)

    with allure.step("Verify response body"):
        body = response.json()

        assert_that(body).contains_key("books")
        assert_that(len(body["books"])).is_greater_than(0)
        assert_that(body["books"][0]["isbn"]).is_equal_to(BOOKS["existing"]["isbn"])

    with allure.step("Verify response data type"):
        assert_that(body["books"]).is_instance_of(list)
        assert_that(body["books"][0]["isbn"]).is_instance_of(str)
        
@allure.title("User can retrieve the book list")
def test_get_all_books_success():

    with allure.step("Send request to retrieve all books"):
        response = book_service.get_all_books()

    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.OK)

    with allure.step("Verify response body"):
        body = response.json()

        assert_that(body).contains_key("books")
        assert_that(len(body["books"])).is_greater_than(0)
        
        for book in body["books"]:
            assert_book_schema(book)
    
    with allure.step("Verify response data type"):
        assert_that(body["books"]).is_instance_of(list)
        assert_that(body["books"][0]["title"]).is_instance_of(str)
        assert_that(body["books"][0]["pages"]).is_instance_of(int)
        
@allure.title("User can retrieve specific book using valid ISBN")
def test_get_book_detail_success():

    with allure.step(f"Send request to retrive book with ISBN {BOOKS["existing"]["isbn"]}"):
        response = book_service.get_book_by_isbn(
            isbn=BOOKS["existing"]["isbn"]
        )

    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.OK)

    with allure.step("Verify response body"):
        body = response.json()

        assert_that(body["isbn"]).is_equal_to(BOOKS["existing"]["isbn"])
        assert_that(body["title"]).is_equal_to(BOOKS["existing"]["title"])
        assert_that(body["author"]).is_equal_to(BOOKS["existing"]["author"])
        assert_that(body["pages"]).is_greater_than(0)
        
    with allure.step("Verify response data type"):
        assert_that(body).is_instance_of(dict)
        assert_that(body["title"]).is_instance_of(str)
        assert_that(body["pages"]).is_instance_of(int)
        
@allure.title("User can update an existing book")
def test_update_book_success(created_user, user_token):

    with allure.step(f"Send request to update ISBN from {BOOKS["existing"]["isbn"]} to {BOOKS["new"]["isbn"]}"):
        response = book_service.update_book(
            existing_isbn=BOOKS["existing"]["isbn"],
            user_id=created_user["user_id"],
            new_isbn=BOOKS["new"]["isbn"],
            token=user_token,
        )

    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.OK)

    with allure.step("Verify response body"):
        body = response.json()

        assert_that(body).contains_key("books")
        assert_that(len(body["books"])).is_equal_to(1)
     
        assert_that(body["books"][0]["isbn"]).is_equal_to(BOOKS["new"]["isbn"])
        assert_that(body["books"][0]["title"]).is_equal_to(BOOKS["new"]["title"])
        assert_that(body["books"][0]["author"]).is_equal_to(BOOKS["new"]["author"])
        
    with allure.step("Verify response data type"):
        assert_that(body["books"]).is_instance_of(list)
        assert_that(body["books"][0]["title"]).is_instance_of(str)
        assert_that(body["books"][0]["pages"]).is_instance_of(int)

@allure.title("User can delete a book from collection")
def test_delete_book_success(created_user, user_token):

    with allure.step(f"Send request to delete book with ISBN {BOOKS["new"]["isbn"]}"):
        response = book_service.delete_book(
            user_id=created_user["user_id"],
            isbn=BOOKS["new"]["isbn"],
            token=user_token,
        )

    with allure.step("Verify response status code"):
        assert_that(response.status_code).is_equal_to(HTTPStatus.NO_CONTENT)