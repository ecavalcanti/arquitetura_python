import re


class CPF:
    def __init__(self, numero: str) -> None:
        if numero is None or not re.match(r'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}', numero):
            raise Exception('CPF inválido.')
        self.__numero = numero

    def __str__(self) -> str:
        return self.__numero
