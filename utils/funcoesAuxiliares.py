def retornaMenuPrincipal():
    menu = input("\nDeseja retornar para o menu principal?").upper()

    if (menu == "SIM"):
        retornaMenu = True
    elif (menu == "NÃO"):
        retornaMenu = False
    return retornaMenu

#fazer o try catch


def formataTexto(texto):
    nomeFormatado = texto.title()
    return nomeFormatado

