from datetime import datetime
from .client import PortalClient
from .status import LogStatus


class PortalLogger:
    def __init__(self, token: str):
        self.start_time = datetime.now()
        self.client = PortalClient(token)

    def _send(self, status: LogStatus, message: str):
        end_time = datetime.now()

        self.client.send(
            cod=status,
            message=message,
            start_time=self.start_time,
            end_time=end_time
        )

    def success(self, message: str):
        self._send(LogStatus.SUCESSO, message)

    def error(self, message: str):
        self._send(LogStatus.ERRO, message)

    def warning(self, message: str):
        self._send(LogStatus.ATENCAO, message)

    def pending(self, message: str):
        self._send(LogStatus.PENDENTE, message)

    def cancelled(self, message: str):
        self._send(LogStatus.CANCELADO, message)

    def unknown(self, message: str):
        self._send(LogStatus.DESCONHECIDO, message)
