import re


class Email:
    def __init__(self, endereco) -> None:
        if endereco is None or not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', endereco):
            raise Exception('Email inválido')
        self.__endereco = endereco

    def __str__(self) -> str:
        return self.__endereco
