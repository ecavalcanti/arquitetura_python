from gameficacao.dominio.selo.repositorio_de_selos import RepositorioDeSelos
from gameficacao.dominio.selo.selo import Selo
from shared.cpf import CPF
from shared.dominio.evento.evento import Evento
from shared.dominio.evento.ouvinte import Ouvinte
from shared.dominio.evento.tipo_de_evento import TipoDeEvento


class GeraSeloAlunoNovato(Ouvinte):

    def __init__(self, repositorio: RepositorioDeSelos) -> None:
        self.__repositorio = repositorio

    def _deve_processar(self, evento: Evento) -> None:
        return evento.tipo == TipoDeEvento.ALUNO_MATRICULADO

    def _reage_ao(self, evento: Evento) -> None:
        cpf_do_aluno: CPF = evento.informacoes["cpf"]
        novato = Selo(cpf_do_aluno, "Novato")
        self.__repositorio.adicionar(novato)
