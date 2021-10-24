from abc import ABC, abstractmethod

from shared.dominio.evento.evento import Evento


class Ouvinte(ABC):
    def processa(self, evento: Evento) -> None:
        if self._deve_processar(evento):
            self._reage_ao(evento)

    @abstractmethod
    def _deve_processar(self, evento: Evento) -> None:
        pass

    @abstractmethod
    def _reage_ao(self, evento: Evento) -> None:
        pass
