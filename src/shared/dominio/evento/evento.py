from datetime import datetime
from abc import ABC, abstractmethod

from shared.dominio.evento.tipo_de_evento import TipoDeEvento


class Evento(ABC):

    def __init__(self) -> None:
        self.__momento = datetime.now()

    @property
    @abstractmethod
    def tipo(self) -> TipoDeEvento:
        pass

    @property
    @abstractmethod
    def informacoes(self) -> dict[str, object]:
        pass

    @property
    def momento(self) -> datetime:
        return self.__momento
