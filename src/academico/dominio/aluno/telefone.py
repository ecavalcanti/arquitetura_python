import re


class Telefone:
    def __init__(self, ddd: str, numero: str) -> None:
        if ddd is None or numero is None:
            raise Exception('DDD e Número são obrigatórios')

        if not re.match(r"\d{2}", ddd):
            raise Exception('DDD inválido')

        if not re.match(r"\d{8}|\d{9}", numero):
            raise Exception('Número inválido')

        self.__ddd = ddd
        self.__numero = numero

    @property
    def ddd(self) -> str:
        return self.__ddd

    @property
    def numero(self) -> str:
        return self.__numero

    def __str__(self) -> str:
        return f'({self.__ddd}) {self.__numero}'
