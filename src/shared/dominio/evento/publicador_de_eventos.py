from shared.dominio.evento.evento import Evento
from shared.dominio.evento.ouvinte import Ouvinte


class PublicadorDeEventos:
    def __init__(self) -> None:
        self.__ouvintes: list[Ouvinte] = []

    def adicionar(self, ouvinte: Ouvinte) -> None:
        self.__ouvintes.append(ouvinte)

    def publicar(self, evento: Evento) -> None:
        for ouvinte in self.__ouvintes:
            ouvinte.processa(evento)
