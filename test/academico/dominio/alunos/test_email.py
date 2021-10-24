import pytest

from academico.dominio.aluno.email import Email


class TestEmail:
    def test_nao_deveria_criar_emails_com_endereco_invalido(self):
        with pytest.raises(Exception):
            Email(None)
        with pytest.raises(Exception):
            Email("")
        with pytest.raises(Exception):
            Email("emailinvalido")

    def test_deve_criar_emails_com_endereco_valido(self):
        endereco = "teste@test.com.br"
        email = Email("teste@test.com.br")
        assert endereco == str(email)
