from datetime import datetime

from academico.dominio.aluno.aluno import Aluno


class Indicacao:
    __indicado: Aluno
    __indicante: Aluno
    __data_indicacao: datetime

    def __init__(self, indicado: Aluno, indicante: Aluno) -> None:
        self.__indicado = indicado
        self.__indicante = indicante
        self.__data_indicacao = datetime.now()

    @property
    def indicado(self) -> Aluno:
        return self.__indicado

    @property
    def indicante(self) -> Aluno:
        return self.__indicante

    @property
    def data_indicacao(self) -> datetime:
        return self.__data_indicacao
