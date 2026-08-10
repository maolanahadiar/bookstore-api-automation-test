EXPECTED_MESSAGES = {
    "token_success": {
        "status": "Success",
        "result": "User authorized successfully."
    },
    "unauthorized": {
        "code": "1200",
        "message": "User not authorized!"
    },
    "invalid_isbn": {
        "code": "1205",
        "message": "ISBN supplied is not available in Books Collection!"
    },
    "duplicate_book": {
        "code": "1210",
        "message": "ISBN already present in the User's Collection!"
    }
}