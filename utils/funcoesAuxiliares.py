


def retornaMenuPrincipal():
    verifica = True
    while verifica:
        menu = input("\nDeseja retornar para o menu principal? " ).upper()
        try:
            if (menu == "SIM"):
                retornaMenu = False
                verifica = False

            elif (menu == "NÃO" or menu == "NAO"):
                retornaMenu = True
                verifica =False
        except:
            print("Entrada inválida, digite novamente.")

    return retornaMenu

# if __name__=="__main__":
#     retornaMenuPrincipal(True)



def formataTexto(texto):
    nomeFormatado = texto.title()
    return nomeFormatado


def imprimiDados (lista):
    print()
    for cliente in lista:
        for chave, dado in cliente.items():
            if isinstance(dado, dict):
                print(f'{chave}')
                for subChave, subDado in dado.items():
                    print(f'{subChave}: {subDado}')
            else:
                print(f'{chave}: {dado}')

        print("______________________________________")


def validaCompra():
    valida = True
    while valida:
        try:
            valorCompra = float(input("Valor da compra: "))
            valida = False
        except:
            print("Valor inválido. Digite novamente.")
    return valorCompra


def validaQunatidade():
    valida = True
    while valida:
        try:
            quantidadeComprada = int(input("Quantidade comprada: "))
            valida = False
        except:
            print("Valor inválido. Digite novamente.")
    return quantidadeComprada


def validaId():
    valida = True
    while valida:
        try:
            idCliente = input("ID do cliente: ")
            valida = False
        except:
            print("Valor inválido. Digite novamente.")
    return idCliente

if __name__=="__main__":
    validaQunatidade()