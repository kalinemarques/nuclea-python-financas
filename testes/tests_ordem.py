import string
import unittest
import random
from unittest.mock import patch

from faker import Faker

from main import main
from utils.opcao import listaAcao


class TestOrdem(unittest.TestCase):


    def geraAcaoFake(self):
        fake = Faker()
        nome = fake.company()
        caracteres = string.ascii_uppercase + string.digits
        ticket = ''.join(random.choices(caracteres, k = 4))
        return ticket


    def geraCompraFake(self):
        fake = Faker()
        valor = fake.pyfloat(left_digits = 1, right_digits = 2, positive = True)
        quantidade = fake.random_int(min=1, max = 100)
        return quantidade, valor

    def testAcao(self):
        nome = "teste"
        ticket = self.geraAcaoFake()
        quantidade, valor = self.geraCompraFake()

        inputs = ["2", "1", nome, ticket, valor, quantidade, "25/02/2023", "16", "sim", "5"]

        with patch("builtins.input", side_effect=inputs):
            main()

        OrdemEsperada = {
            "nome": nome,
            "ticket": ticket,
            "valor_compra": valor,
            "quantidade_compra": quantidade,
            "data_compra":  "25/02/2023",
            "cliente_id": "16"
        }

        self.assertIn(OrdemEsperada, listaAcao)