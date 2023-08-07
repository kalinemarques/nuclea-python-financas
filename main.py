from utils.opcao import opcao1, opcao2, opcao3, opcao4


def main():
    validador = True

    while(validador):

        print("Seja bem vindo(a) ao sistema de gerenciamento da carteira de ações da Nuclea.\nSelecione uma das opções abaixo:")
        print("1 - Cliente\n2 - Cadastrar ação\n3 - Realizar análise da carteira\n4 - Imprimir relatório da carteira\n5 - Sair")
        opcao = int(input("Digite a opção desejada:"))

        if (opcao == 1):
            opcao1()
        elif (opcao == 2):
            opcao2()
        elif (opcao == 3):
            opcao3()
        elif (opcao == 4):
            opcao4()
        elif (opcao == 5):
            validador = False
        else:
           print("Entrada inválida! Tente novamente.")

    print("\nObrigada por utilizar nossos serviços.")



if __name__=="__main__":
    main()
