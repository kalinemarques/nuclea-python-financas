import requests


#verificar se o cep existe e pegar os dados de
# entreço a parti do cep e por no dicionário
def buscaCep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    print(response.text)

if __name__=="__main__":
    buscaCep("59296238")
