from datetime import datetime
import requests
import os

class PortalClient:
    def __init__(self, token: str):
        self.endpoint = os.getenv("PORTAL_LOG_ENDPOINT")
        if not self.endpoint:
            raise RuntimeError("PORTAL_LOG_ENDPOINT não configurado")

        self.token = token

    def _format_datetime(self, dt: datetime) -> str:
        return dt.strftime("%Y/%m/%d %H:%M:%S")

    def send(self, cod, message, start_time: datetime, end_time: datetime):
        payload = {
            "startTime": self._format_datetime(start_time),
            "endTime": self._format_datetime(end_time),
            "cod": int(cod),
            "token": self.token,
            "details": {
                "massaje": message
            }
        }

        response = requests.post(self.endpoint, json=payload)
        response.raise_for_status()
