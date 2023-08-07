import sys

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

from utils.validaData import validaDataCarteira


def analiseDaCarteira():
    print("ANÁLISE DA CARTEIRA")
    print("Data inicial")
    start_date = validaDataCarteira()
    print("Data final")
    end_date = validaDataCarteira()

    #usar ações do banco de dados
    lista = ['ABCB4.SA', 'AGRO3.SA', 'BBAS3.SA', 'BBSE3.SA', 'CPLE6.SA', 'GOAU4.SA', 'ITSA4.SA', 'RANI3.SA', 'SAPR11.SA', 'TAEE11.SA', 'VIVT3.SA']

    df = pd.DataFrame()

    for i in lista:
        cotacao = yf.download(i,start = start_date, end =end_date)
        df[i] = cotacao['Adj Close']

    df.plot(figsize=(15,10))

    plt.xlabel('Anos')
    plt.ylabel('Valor Ticket')
    plt.title('Variação de valor das ações')
    plt.legend()
    plt.show()

    plt.show(block=False)



if __name__=="__main__":
    analiseDaCarteira()
