from clients.api_client import ApiClient
from config.settings import BASE_URL

class BookStoreService(ApiClient):

    def get_all_books(self):
        """Retrieve the list of all available books"""
        
        return self.get(
            url=f"{BASE_URL}/BookStore/v1/Books",
        )

    def get_book_by_isbn(self, isbn):
        """Retrieve specific book by using ISBN"""
        
        return self.get(
            url=f"{BASE_URL}/BookStore/v1/Book",
            params={
                "ISBN": isbn,
            },
        )

    def add_book(self, user_id, isbn, token):
        """Add book to the user's collection"""

        headers = {
            "Authorization": f"Bearer {token}"
        }

        payload = {
            "userId": user_id,
            "collectionOfIsbns": [
                {
                    "isbn": isbn,
                }
            ],
        }
        
        return self.post(
            url=f"{BASE_URL}/BookStore/v1/Books",
            headers=headers,
            json=payload,
        )

    def update_book(self, existing_isbn, user_id, new_isbn, token):
        """Update an existing book in the user's collection"""

        headers = {
            "Authorization": f"Bearer {token}"
        }

        payload = {
            "userId": user_id,
            "isbn": new_isbn,
        }
        
        return self.put(
            url=f"{f"{BASE_URL}/BookStore/v1/Books"}/{existing_isbn}",
            headers=headers,
            json=payload,
        )

    def delete_book(self, user_id, isbn, token):
        """Remove book from the user's collection"""

        headers = {
            "Authorization": f"Bearer {token}"
        }

        payload = {
            "userId": user_id,
            "isbn": isbn,
        }
        
        return self.delete(
            url=f"{BASE_URL}/BookStore/v1/Book",
            headers=headers,
            json=payload,
        )