from academico.aplicacao.aluno.matricular.matricular_aluno import MatricularAluno
from academico.aplicacao.aluno.matricular.matricular_aluno_dto import MatricularAlunoDto
from academico.dominio.aluno.log_de_aluno_matriculado import LogDeAlunoMatriculado
from academico.infra.aluno.repositorio_de_alunos_em_memoria import RepositorioDeAlunosEmMemoria
from gameficacao.aplicacao.gera_selo_aluno_novato import GeraSeloAlunoNovato
from gameficacao.infra.selo.repositorio_de_selos_em_memoria import RepositorioDeSelosEmMemoria
from shared.dominio.evento.publicador_de_eventos import PublicadorDeEventos

if __name__ == '__main__':
    cpf = '478.058.900-21'
    nome = 'Eric Cavalcanti'
    email = 'email@test.com.br'

    publicador_de_eventos = PublicadorDeEventos()
    publicador_de_eventos.adicionar(LogDeAlunoMatriculado())

    repositorio_de_selos = RepositorioDeSelosEmMemoria()
    publicador_de_eventos.adicionar(GeraSeloAlunoNovato(repositorio_de_selos))

    matricularAluno = MatricularAluno(RepositorioDeAlunosEmMemoria(), publicador_de_eventos)
    matricularAluno.executa(MatricularAlunoDto(nome, cpf, email))
