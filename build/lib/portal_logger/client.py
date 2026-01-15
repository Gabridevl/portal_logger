import os
import requests

ENDPOINT_URL = os.getenv("PORTAL_LOG_ENDPOINT")

if not ENDPOINT_URL:
    raise RuntimeError("PORTAL_LOG_ENDPOINT não configurado")

class PortalClient:
    def __init__(self, token: str, timeout: int = 10):
        self.token = token
        self.timeout = timeout

    def send(self, cod, message, start_time, end_time):
        payload = {
            "startTime": start_time.isoformat(),
            "endTime": end_time.isoformat(),
            "cod": cod,
            "token": self.token,
            "details": {
                "massaje": message
            }
        }

        response = requests.post(
            ENDPOINT_URL,
            json=payload,
            timeout=self.timeout
        )

        response.raise_for_status()
