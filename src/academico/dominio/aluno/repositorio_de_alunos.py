from abc import ABC, abstractmethod

from academico.dominio.aluno import CPF, Aluno


class RepositorioDeAlunos(ABC):
    @abstractmethod
    def matricular(self) -> None:
        pass

    @abstractmethod
    def buscar_por_cpf(self, cpf: CPF) -> Aluno:
        pass