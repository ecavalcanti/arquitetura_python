from shared.dominio.evento.evento import Evento
from shared.dominio.evento.ouvinte import Ouvinte
from shared.dominio.evento.tipo_de_evento import TipoDeEvento


class LogDeAlunoMatriculado(Ouvinte):
    def _deve_processar(self, evento: Evento) -> None:
        return evento.tipo == TipoDeEvento.ALUNO_MATRICULADO

    def _reage_ao(self, evento: Evento) -> None:
        print(f'Aluno com CPF {evento.informacoes["cpf"]} matriculado em: {evento.momento}')
