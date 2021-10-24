import pytest

from academico.dominio.aluno import CPF


class TestCPF:
    def test_nao_deveria_criar_cpfs_com_numero_invalido(self):
        with pytest.raises(Exception):
            CPF(None)
        with pytest.raises(Exception):
            CPF("")
        with pytest.raises(Exception):
            CPF("cpfinvalido")

    def test_deveria_poder_criar_cpfs_com_numero_valido(self):
        numero = "286.554.390-02"
        cpf = CPF(numero)
        assert numero == str(cpf)
