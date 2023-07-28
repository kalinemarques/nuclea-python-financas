def retornaMenuPrincipal():
    menu = input("\nDeseja retornar para o menu principal?").upper()

    if (menu == "SIM"):
        retornaMenu = True
    elif (menu == "NÃO"):
        retornaMenu = False
    return retornaMenu



def formataTexto(texto):
    nomeFormatado = texto.title()
    return nomeFormatado


def imprimiDados (lista):
    print()
    for cliente in lista:
        for chave, dado in cliente.items():
            if isinstance(dado, dict):
                print(f'{dado}')
                for subChave, subDado in dado.items():
                    print(f'{subChave}: {subDado}')
            else:
                print(f'{chave}: {dado}')

        print("______________________________________")