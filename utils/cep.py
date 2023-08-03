import requests

def buscaCepTeste(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    return response


def corrigeCep(endereco):
    while True:
        corrige = input("\nDeseja alterar o endereço? ").upper()
        if (corrige == "NÃO" or corrige == "NAO"):
            return endereco
        elif (corrige == "SIM"):
            return endereco
        else:
            print("Entrada inválida, digite novamente.")


def validaCep():
    while True:
        cep = input("CEP: ")
        try:
            response = buscaCepTeste(cep)
            endereco = {
            "CEP": response.json().get("cep", ""),
            "Estado": response.json().get("uf", ""),
            "Cidade": response.json().get("localidade", ""),
            "Bairro": response.json().get("bairro", ""),
            "Logradouro": response.json().get("logradouro", "")
            }

            if (response.status_code == 200 and response.json().get("cep", "") != ""):
                endereco["Complemento"] = input("Complemento: ")
                endereco["Número"] = input("Número: ")

                print("\nVerifique se os dados estão corretos.")

                for chave, valor in endereco.items():
                    print(f'{chave}: {valor}')

                endereco = corrigeCep(endereco)
                return endereco

            else:
                print("CEP inválido, digite novamente.")
        except:
            print("CEP inválido, digite novamente.")



if __name__=="__main__":
    validaCep()