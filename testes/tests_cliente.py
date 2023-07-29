import unittest
from unittest.mock import patch

from faker import Faker

from main import main, listaCiente
from utils.validaCpf import geraCpf


class TestStringMethods(unittest.TestCase):
    pass


    def gerarNomeFake(self):
        fake = Faker()
        return fake.name()


    def testCliente(self):
        nome = self.gerarNomeFake()
        cpf = geraCpf()
        inputs = ["1", nome, cpf, "12.345.647-x", "12/02/2001", "05003-060", "42", "não", "não"]

        with patch("builtins.input", side_effect = inputs):
            main()

        clienteEsperado = {
            "Nome": nome,
            "CPF": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "RG": "12.345.647-x",
            "Data de nascimento": "12/02/2001",
            "Endereço": {
                "CEP": "05003-060",
                "Estado": "SP",
                "Cidade": "São Paulo",
                "Bairro": "Água Branca",
                "Logradouro": "Rua Higino Pellegrini",
                "Número da casa": "48"
            }
        }


        #self.assertEquals(self.gerarNomeFake(),"batata")

