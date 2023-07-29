import requests


def buscaCep():
    while True:
        cep = input("Digite seu CEP: ")
        try:
            url = f"http://viacep.com.br/ws/{cep}/json/"
            response = requests.get(url)

            endereco = {
                "CEP": response.json().get("cep", ""),
                "Estado": response.json().get("uf", ""),
                "Cidade": response.json().get("localidade", ""),
                "Bairro": response.json().get("bairro", ""),
                "Logradouro": response.json().get("logradouro", ""),
                "Número da casa": input("Número da casa: ")
            }


            if (response.status_code == 200 and response.json().get("cep", "") != ""):
                print("\nVerifique se os dados estão corretos.")

                for chave, valor in endereco.items():
                    print(f'{chave}: {valor}')

                valida = True
                while (valida):
                    corrige = input("\nDeseja alterar o endereço? ").upper()

                    if (corrige == "NÃO" or corrige == "NAO"):

                        return endereco
                        valida = False

                    elif (corrige == "SIM"):
                        valida = False

                    else:
                        print("Entrada inválida, digite novamente.")


            else:
                print("CEP inválido, digite novamente.")

        except:
            print("CEP inválido, digite novamente.")



if __name__=="__main__":
    buscaCep()

