from gameficacao.dominio.selo.repositorio_de_selos import RepositorioDeSelos
from gameficacao.dominio.selo.selo import Selo
from shared.cpf import CPF


class RepositorioDeSelosEmMemoria(RepositorioDeSelos):

    def __init__(self) -> None:
        self.__selos: list[Selo] = []

    def adicionar(self, selo: Selo) -> None:
        self.__selos.append(selo)

    def selos_dos_alunos_de_cpf(self, cpf: CPF):
        return next(filter(lambda selo: (str(selo.cpf_do_aluno) == str(cpf)), self.__selos), None)
