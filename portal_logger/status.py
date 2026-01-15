from enum import IntEnum


class LogStatus(IntEnum):
    SUCESSO = 200
    DESCONHECIDO = 400
    ERRO = 500
    ATENCAO = 100
    PENDENTE = 300
    CANCELADO = 501
