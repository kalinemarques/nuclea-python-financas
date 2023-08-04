from relatorio import obterDadosAcao
from utils.cep import validaCep
from utils.funcoesAuxiliares import formataTexto, imprimiDados, retornaMenuPrincipal, validaCompra, validaQunatidade, \
    validaId
from utils.validaCpf import validaCpf
from utils.validaData import validaData
from utils.validaRg import validaRg

listaCliente = []


def opcao1():
    validadorOpcao1 = True
    while validadorOpcao1:
        print("MENU CLIENTE\n1 - Cadastrar\n2 - Consultar\n3 - Atualizar\n4 - Deletar\n5 - Voltar ao menú principal")
        opcaoCliente = int(input("\nDigite a opção desejada:"))

        if opcaoCliente == 1:
            print("\nInsira os dados do cliente.")

            dadosCliente = {
                "Nome": formataTexto(input("Nome: ")),
                "CPF": validaCpf(),
                "RG": validaRg(),
                "Data de nascimento": validaData(),
                "Endereço": validaCep(),
            }

            listaCliente.append(dadosCliente)

            imprimiDados(listaCliente)

            validadorOpcao1 = retornaMenuPrincipal()

        elif opcaoCliente == 2:
            print("SELECT")
        elif opcaoCliente == 3:
            print("UPDATE")
        elif opcaoCliente == 4:
            print("DELET")
        elif opcaoCliente == 5:
            validadorOpcao1 = False
        else:
            print("operação inválida.")



listaAcao = []



def opcao2():
    validaOpcao2 = True
    while validaOpcao2:
        print("Insira os dados da ação.")
        dadosOrdem = {
            "Nome": input("Nome: "),
            "Ticket": input("Ticket: "),
            "Valor da compra": validaCompra(),
            "Quantidade comprada": validaQunatidade(),
            "Data da Compra": validaData(),
            "ID do cliente": validaId()
        }
        listaAcao.append(dadosOrdem)
        imprimiDados(listaAcao)

        validaOpcao2 = retornaMenuPrincipal()


def opcao4():
    ticket = input("Digite o nome da ação: ")
    nome_arquivo = input("Digite o nome do arquivo: ")
    obterDadosAcao(ticket, nome_arquivo)


if __name__=="__main__":
    opcao2()