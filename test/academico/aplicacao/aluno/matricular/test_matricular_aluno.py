from academico.aplicacao.aluno.matricular.matricular_aluno import MatricularAluno
from academico.aplicacao.aluno.matricular.matricular_aluno_dto import MatricularAlunoDto
from academico.dominio.aluno import CPF
from academico.infra.aluno.repositorio_de_alunos_em_memoria import RepositorioDeAlunosEmMemoria
from shared.dominio.evento.publicador_de_eventos import PublicadorDeEventos


class TestMatricularAluno:
    def test_aluno_deveria_ser_persistido(self):
        repositorio = RepositorioDeAlunosEmMemoria()
        publicador_de_eventos = PublicadorDeEventos()

        useCase = MatricularAluno(repositorio, publicador_de_eventos)

        dados = MatricularAlunoDto("Fulano", "123.456.789-00", "fulano@email.com.br")
        useCase.executa(dados)

        aluno = repositorio.buscar_por_cpf(CPF("123.456.789-00"))

        assert "Fulano" == aluno.nome
        assert "123.456.789-00" == str(aluno.cpf)
        assert "fulano@email.com.br" == str(aluno.email)



