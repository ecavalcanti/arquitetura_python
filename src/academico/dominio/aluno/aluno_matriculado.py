from shared.cpf import CPF
from shared.dominio.evento.evento import Evento
from shared.dominio.evento.tipo_de_evento import TipoDeEvento


class AlunoMatriculado(Evento):
    def __init__(self, cpf_do_aluno: CPF) -> None:
        super().__init__()
        self.__cpf_do_aluno = cpf_do_aluno

    @property
    def tipo(self) -> TipoDeEvento:
        return TipoDeEvento.ALUNO_MATRICULADO

    @property
    def informacoes(self) -> dict[str, object]:
        return {"cpf": self.__cpf_do_aluno}
