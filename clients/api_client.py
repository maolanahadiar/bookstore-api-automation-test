import json
import requests
from config.settings import TIMEOUT
from utils.logger import get_logger

class ApiClient:
    """Base HTTP client used by all API services"""
    
    def __init__(self):
        self.session = requests.Session()
        self.logger = get_logger(self.__class__.__name__)

        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def request(self, method, url, **kwargs):
        """
        All HTTP methods are routed through this method to keep
        request handling and logging consistent across services
        """
        
        method = method.upper()

        self.logger.info("=" * 80)
        self.logger.info("%s %s", method, url)

        if kwargs.get("params"):
            self.logger.info(
                "Query Params:\n%s",
                json.dumps(kwargs["params"], indent=4),
            )

        if kwargs.get("json"):
            self.logger.info(
                "Request Body:\n%s",
                json.dumps(kwargs["json"], indent=4),
            )

        if kwargs.get("headers"):
            self.logger.info(
                "Headers:\n%s",
                json.dumps(kwargs["headers"], indent=4),
            )

        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=TIMEOUT,
                **kwargs,
            )

            self.logger.info("Status Code : %s", response.status_code)

            try:
                self.logger.info(
                    "Response Body:\n%s",
                    json.dumps(response.json(), indent=4),
                )
            except ValueError:
                self.logger.info(
                    "Response Body:\n%s",
                    response.text,
                )

            self.logger.info("=" * 80)

            return response

        except requests.RequestException:
            self.logger.exception("%s request failed: %s", method, url)
            raise

    def get(self, url, params=None, headers=None):
        return self.request(
            "GET",
            url,
            params=params,
            headers=headers,
        )

    def post(self, url, json=None, headers=None):
        return self.request(
            "POST",
            url,
            headers=headers,
            json=json,
        )

    def put(self, url, json=None, headers=None):
        return self.request(
            "PUT",
            url,
            headers=headers,
            json=json,
        )

    def delete(self, url, json=None, headers=None):
        return self.request(
            "DELETE",
            url,
            headers=headers,
            json=json,
        )