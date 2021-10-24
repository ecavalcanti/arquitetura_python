from abc import ABC, abstractmethod

from gameficacao.dominio.selo.selo import Selo
from shared.cpf import CPF


class RepositorioDeSelos(ABC):

    @abstractmethod
    def adicionar(self, selo: Selo) -> None:
        pass

    @abstractmethod
    def selos_dos_alunos_de_cpf(self, cpf: CPF):
        pass
