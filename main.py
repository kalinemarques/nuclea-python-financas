from utils.cep import buscaCep
from utils.funcoesAuxiliares import formataTexto, retornaMenuPrincipal, imprimiDados
from utils.validaCpf import validaCpf
from utils.validaData import validaDataNascimento
from utils.validaRg import validaRg

validador = True
listaCiente = []

while(validador):

    print("Seja bem vindo(a) ao sistema de gerenciamento da carteira de ações da Nuclea.\nSelecione uma das opções abaixo:")
    print("1 - Cadastar cliente\n2 - Cadastrar ação\n3 - Realizar análise da carteira\n4 - Imprimir relatório da carteira\n5 - Sair")
    opcao = int(input("Digite a opção desejada:"))

    if (opcao == 1):
        print("\nInsira os dados do cliente.")

        dadosCliente = {
            "Nome": formataTexto(input("Nome: ")),
            "CPF": validaCpf(),
            "RG": validaRg(),
            "Data de nascimento": validaDataNascimento(),
            "Endereço": buscaCep(),
        }

        listaCiente.append(dadosCliente)

        imprimiDados(listaCiente)

        validador = retornaMenuPrincipal()

    elif (opcao == 2):
        pass
    elif (opcao == 3):
        pass
    elif (opcao == 4):
        pass
    elif (opcao == 5):
        validador = False
    else:
       print("Entrada inválida! Tente novamente.")

print("\nObrigada por utilizar nossos serviços.")
