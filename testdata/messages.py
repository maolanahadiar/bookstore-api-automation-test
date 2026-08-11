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
    },
    "empty_field": {
        "code": "1200",
        "message": "UserName and Password required."
    },
    "invalid_credentials": {
        "code": "1207",
        "message": "User not found!"
    },
    "invalid_user_id": {
        "code": "1207",
        "message": "User not found!"
    }
}