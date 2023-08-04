import random
import string
import unittest
from unittest.mock import patch

from faker import Faker

from main import main
from utils.opcao import listaCliente, listaAcao
from utils.validaCpf import geraCpf


class TestStringMethods(unittest.TestCase):


    def gerarNomeFake(self):
        fake = Faker()
        return fake.name()


    def testCliente(self):
        nome = self.gerarNomeFake()
        cpf = geraCpf()
        inputs = ["1","1", nome, cpf, "12.345.647-x", "12/02/2001", "59296-238", "Casa", "42", "não", "sim","5"]

        with patch("builtins.input", side_effect = inputs):
            main()

        clienteEsperado = {
            "Nome": nome,
            "CPF": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "RG": "12.345.647-x",
            "Data de nascimento": "12/02/2001",
            "Endereço": {
                "CEP": "59296-238",
                "Estado": "RN",
                "Cidade": "São Gonçalo do Amarante",
                "Bairro": "Novo Amarante",
                "Logradouro": "Rua Santa Bárbara",
                "Complemento": "Casa",
                "Número": "42"
            }
        }


        self.assertIn(clienteEsperado, listaCliente)

    def geraAcaoFake(self):
        fake = Faker()
        nome = fake.company()
        caracteres = string.ascii_uppercase + string.digits
        ticket = ''.join(random.choices(caracteres, k = 4))
        return nome, ticket


    def geraCompraFake(self):
        fake = Faker()
        valor = fake.pyfloat(left_digits = 1, right_digits = 2, positive = True)
        quantidade = fake.random_int(min=1, max = 100)
        return quantidade, valor

    def testAcao(self):
        nome, ticket = self.geraAcaoFake()
        quantidade, valor = self.geraCompraFake()
        inputs = ["2", nome, ticket, valor, quantidade, "25/02/2023",2, "sim", "5"]

        with patch("builtins.input", side_effect=inputs):
            main()

        OrdemEsperada = {
            "Nome": nome,
            "Ticket": ticket,
            "Valor da compra": valor,
            "Quantidade comprada": quantidade,
            "Data da Compra":  "25/02/2023",
            "ID do cliente": 2
        }

        self.assertIn(OrdemEsperada, listaAcao)
