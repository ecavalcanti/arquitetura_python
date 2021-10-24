from shared.cpf import CPF


class Selo:
    def __init__(self, cpf_do_aluno: CPF, nome: str) -> None:
        self.__cpf_do_aluno = cpf_do_aluno
        self.__nome = nome

    @property
    def cpf_do_aluno(self) -> CPF:
        return self.__cpf_do_aluno

    @property
    def nome(self) -> str:
        return self.__nome