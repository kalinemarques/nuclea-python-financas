import sys

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

from models.cliente import Cliente
from utils.validaCpf import validaCpf
from utils.validaData import validaDataCarteira


def analiseDaCarteira():
    print("ANÁLISE DA CARTEIRA")
    print("Data inicial")
    start_date = validaDataCarteira()
    print("Data final")
    end_date = validaDataCarteira()

    print("Insira o CPF do cliente para a busca:")
    cpf = validaCpf()
    cliente = Cliente()

    print("Ações do cliente")
    ordens = cliente.exibirOrdensPorCpfCliente(cpf)

    try:
        tickets = [ordem['ticket'] for ordem in ordens]
        df = pd.DataFrame()

        for ticket in tickets:
              cotacao = yf.download(ticket,start = start_date, end =end_date)
              df[ticket] = cotacao['Adj Close']


        df.plot(figsize=(15,10))

        plt.xlabel('Anos')
        plt.ylabel('Valor Ticket')
        plt.title('Variação de valor das ações')
        plt.legend()
        plt.show()

        plt.show(block=False)
    except:
        print("Não foi possível gerar o gráfico de análise da carteira.")



if __name__=="__main__":
    analiseDaCarteira()
