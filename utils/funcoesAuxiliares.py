def retornaMenuPrincipal():
    verifica = True
    while verifica:
        menu = input("\nDeseja retornar para o menu principal? " ).upper()
        try:
            if (menu == "SIM"):
                retornaMenu = True
                verifica = False

            elif (menu == "NÃO" or menu == "NAO"):
                retornaMenu = False
                verifica =False
            return retornaMenu

        except:
            print("Entrada inválida, digite novamente.")



if __name__=="__main__":
    retornaMenuPrincipal()



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