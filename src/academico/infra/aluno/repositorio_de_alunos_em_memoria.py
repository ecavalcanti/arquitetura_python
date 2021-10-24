from academico.dominio.aluno import CPF, Aluno
from academico.dominio.aluno.repositorio_de_alunos import RepositorioDeAlunos


class RepositorioDeAlunosEmMemoria(RepositorioDeAlunos):
    def __init__(self) -> None:
        self.__matriculados: list[Aluno] = []

    def matricular(self, aluno: Aluno) -> None:
        self.__matriculados.append(aluno)

    def buscar_por_cpf(self, cpf: CPF) -> Aluno:
        return next(filter(lambda aluno: (str(aluno.cpf) == str(cpf)), self.__matriculados), None)
