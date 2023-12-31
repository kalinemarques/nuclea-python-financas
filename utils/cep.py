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
            "cep": response.json().get("cep", ""),
            "estado": response.json().get("uf", ""),
            "cidade": response.json().get("localidade", ""),
            "bairro": response.json().get("bairro", ""),
            "logradouro": response.json().get("logradouro", "")
            }

            if (response.status_code == 200 and response.json().get("cep", "") != ""):
                endereco["complemento"] = input("Complemento: ")
                endereco["numero_residencia"] = input("Número: ")

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