from academico.dominio.aluno import Aluno, CPF, Email


class MatricularAlunoDto:
    def __init__(self, nome_aluno: str, cpf_aluno: str, email_aluno: str) -> None:
        self.__nome_aluno = nome_aluno
        self.__cpf_aluno = cpf_aluno
        self.__email_aluno = email_aluno

    def criar_aluno(self) -> Aluno:
        return Aluno(CPF(self.__cpf_aluno), self.__nome_aluno, Email(self.__email_aluno))
