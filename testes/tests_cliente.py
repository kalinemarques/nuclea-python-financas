import random
import string
import unittest
from unittest.mock import patch

from faker import Faker

from main import main
from utils.opcao import listaCliente
from utils.validaCpf import geraCpf


class TestClientes(unittest.TestCase):


    def gerarNomeFake(self):
        fake = Faker()
        return fake.name()


    def testCliente(self):
        nome = self.gerarNomeFake()
        cpf = geraCpf()
        inputs = ["1", "1", nome, cpf, "12.345.647-x", "12/02/2001", "59296-238", "Casa", "42", "não", "sim", "5"]

        with patch("builtins.input", side_effect = inputs):
            main()

        clienteEsperado = {
            "nome": nome,
            "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "rg": "12.345.647-x",
            "data_nascimento": "12/02/2001",
            "endereco": {
                "cep": "59296-238",
                "estado": "RN",
                "cidade": "São Gonçalo do Amarante",
                "bairro": "Novo Amarante",
                "logradouro": "Rua Santa Bárbara",
                "complemento": "Casa",
                "numero_residencia": "42"
            }
        }


        self.assertIn(clienteEsperado, listaCliente)



