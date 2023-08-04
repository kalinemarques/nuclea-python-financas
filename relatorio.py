import yfinance as yf

def obterDadosAcao(ticket, nome_arquivo):
    try:
        print("Coletando dados da ação: " + ticket)

        acao = yf.download(ticket + '.SA', progress = False)

        with open(nome_arquivo,'w') as arquivo:
            arquivo.write("Relatório da ação: " + ticket + '\n')
            arquivo.write(str(acao.tail()))

    except Exception as e:
        print("Erro ao obter dados da ação. Verifique se o nome está correto.")




