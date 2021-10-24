from academico.dominio.aluno import Aluno, CPF, Email
from academico.infra.aluno.repositorio_de_alunos_em_memoria import RepositorioDeAlunosEmMemoria


class TestRepositorioDeAlunosEmMemoria:
    def test_deveria_matricular_o_aluno(self):
        cpf = CPF("123.456.789-00")
        aluno = Aluno(cpf, "Eric Cavalcanti", Email("teste@email.com"))
        repositorio = RepositorioDeAlunosEmMemoria()
        repositorio.matricular(aluno)
        alunoConsultado = repositorio.buscar_por_cpf(cpf)
        assert alunoConsultado is not None
        assert alunoConsultado.nome == aluno.nome

    def test_nao_deveria_encontrar_o_aluno(self):
        aluno = Aluno(CPF("123.456.789-00"), "Eric Cavalcanti", Email("teste@email.com"))
        repositorio = RepositorioDeAlunosEmMemoria()
        repositorio.matricular(aluno)
        alunoConsultado = repositorio.buscar_por_cpf(CPF("111.111.111-00"))
        assert alunoConsultado is None
