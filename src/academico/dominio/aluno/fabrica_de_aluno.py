from __future__ import annotations

from academico.dominio.aluno.aluno import Aluno
from shared.cpf import CPF
from academico.dominio.aluno.email import Email


class FabricaDeAluno:
    
    def com_nome_cpf_email(self, nome: str, cpf: str, email: str) -> FabricaDeAluno:
        self.__aluno = Aluno(CPF(cpf), nome, Email(email))
        return self

    def com_telefone(self, ddd: str, numero: str) -> FabricaDeAluno:
        self.__aluno.adicionar_telefone(ddd, numero)
        return self

    def criar(self) -> Aluno:
        return self.__aluno
