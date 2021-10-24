import pytest

from academico.dominio.aluno.telefone import Telefone


class TestTelefone:
    def test_nao_deveria_criar_telefones_com_numero_invalido(self):
        with pytest.raises(Exception):
            Telefone(None, "992322322")
        with pytest.raises(Exception):
            Telefone("81", None)
        with pytest.raises(Exception):
            Telefone("", "992322322")
        with pytest.raises(Exception):
            Telefone("81", "")
        with pytest.raises(Exception):
            Telefone("1", "992322322")
        with pytest.raises(Exception):
            Telefone("81", "99232-2322")

    def test_deveria_permitir_criar_telefones_com_ddd_e_numero_validos(self):
        ddd = "11"
        numero = "992342382"
        telefone = Telefone(ddd, numero)
        assert ddd == telefone.ddd
        assert numero == telefone.numero
