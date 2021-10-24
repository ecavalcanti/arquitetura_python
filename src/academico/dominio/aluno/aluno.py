from shared.cpf import CPF
from academico.dominio.aluno.email import Email
from academico.dominio.aluno.telefone import Telefone
from typing import List


class Aluno:
    def __init__(self, cpf: CPF, nome: str, email: Email) -> None:
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__telefones: List[Telefone] = []

    @property
    def email(self) -> Email:
        return self.__email

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> CPF:
        return self.__cpf

    def adicionar_telefone(self, ddd: str, numero: str) -> None:
        self.__telefones.append(Telefone(ddd, numero))
