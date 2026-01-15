# test_logger.py
from portal_logger import PortalLogger

logger = PortalLogger(token="30707c77-8473-42d7-b5e8-ce81cf119fb6")

logger.success("Teste local - robô iniciado")
logger.pending("Teste local - aguardando sistema")
logger.success("Teste local - robô finalizado")
logger.warning("Teste local - aviso")