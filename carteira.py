import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def main():
    #Pedir pro cliente escolher o período de consulta
    #
    start_date = '2020-01-01'
    end_date = '2023-01-01'

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

if __name__=="__main__":
    main()
