import requests

from swagger_server.config.access import access

class NotificationClient:

    def __init__(self):
        self.base_url = access()["API_NOTIFICATION"]

    def send_notification(self, payload):
        response = requests.post(
            f"{self.base_url}",
            json=payload,
            timeout=5
        )

        # Lanza excepción si devuelve 4xx o 5xx
        response.raise_for_status()

        return response.json()