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