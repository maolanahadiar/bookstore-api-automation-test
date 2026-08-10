from clients.api_client import ApiClient
from config.settings import BASE_URL

class AccountService(ApiClient):
    
    def register(self, username, password):
        """Register a new user account"""

        payload = {
            "userName": username,
            "password": password
        }
        
        return self.post(
            url=f"{BASE_URL}/Account/v1/User",
            json=payload
        )
        
    def login(self, username, password):
        """Log in with user credentials"""
        
        payload = {
            "userName": username,
            "password": password
        }
        
        return self.post(
            url=f"{BASE_URL}/Account/v1/Login",
            json=payload
        )
        
    def generate_token(self, username, password):
        """Generate an authentication token"""
        
        payload = {
            "userName": username,
            "password": password
        }
        
        return self.post(
            url=f"{BASE_URL}/Account/v1/GenerateToken",
            json=payload
        )
        
    def get_account(self, user_id, token):
        """Get account details for a user"""
        
        headers = {
            "Authorization": f"Bearer {token}"
        }
        
        return self.get(
            url=f"{BASE_URL}/Account/v1/User/{user_id}",
            headers=headers
        )
        
    def delete_account(self, user_id, token):
        """Delete a user account"""
        
        headers = {
            "Authorization": f"Bearer {token}"
        }
        
        return self.delete(
            url=f"{BASE_URL}/Account/v1/User/{user_id}",
            headers=headers
        )