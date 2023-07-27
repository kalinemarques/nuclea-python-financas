import requests


def buscaCep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    print(response.text)

if __name__=="__main__":
    buscaCep("59296238")
