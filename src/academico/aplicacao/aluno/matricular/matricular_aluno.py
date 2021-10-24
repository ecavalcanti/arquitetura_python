from academico.aplicacao.aluno.matricular.matricular_aluno_dto import MatricularAlunoDto
from academico.dominio.aluno.aluno_matriculado import AlunoMatriculado
from academico.dominio.aluno.repositorio_de_alunos import RepositorioDeAlunos
from shared.dominio.evento.publicador_de_eventos import PublicadorDeEventos


class MatricularAluno:
    def __init__(self, repositorio: RepositorioDeAlunos, publicador_de_eventos: PublicadorDeEventos) -> None:
        self.__repositorio = repositorio
        self.__publicador = publicador_de_eventos

    def executa(self, dados: MatricularAlunoDto) -> None:
        novo = dados.criar_aluno()
        self.__repositorio.matricular(novo)
        self.__publicador.publicar(AlunoMatriculado(novo.cpf))
