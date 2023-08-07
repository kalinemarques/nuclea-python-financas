
from carteira import analiseDaCarteira
from models.cliente import Cliente
from models.ordem import Ordem
from relatorio import obterDadosAcao
from utils.cep import validaCep
from utils.funcoesAuxiliares import formataTexto, imprimiDados, retornaMenuPrincipal, validaCompra, validaQunatidade, \
    validaId
from utils.validaCpf import validaCpf
from utils.validaData import validaDataNascimento, validaDataCompra
from utils.validaRg import validaRg

listaCliente = []
listaAcao = []


def opcao1():
    validadorOpcao1 = True
    while validadorOpcao1:
        print("MENU CLIENTE\n1 - Cadastrar\n2 - Consultar\n3 - Atualizar\n4 - Deletar\n5 - Voltar ao menú principal")
        opcaoCliente = int(input("\nDigite a opção desejada:"))

        if opcaoCliente == 1:
            print("\nInsira os dados do cliente.")

            teste = Cliente()
            cliente = dadosCliente()
            listaCliente.append(cliente)
            teste.cadastrarCliente(cliente)

            validadorOpcao1 = retornaMenuPrincipal()


        elif opcaoCliente == 2:
            print("CONSULTA")
            print("Insira o CPF para buscar o cliente.")
            busca = validaCpf()
            teste = Cliente()
            teste.consultarCliente(busca)
            validadorOpcao1 = retornaMenuPrincipal()

        elif opcaoCliente == 3:
            print("ATUALIZAÇÃO")
            print("Insira o CPF do cliente.")
            busca = validaCpf()
            teste = Cliente()
            teste.consultarCliente(busca)
            escolha = input("Deseja alterar os dados deste cliente?(sim/não)").upper()
            valida = True
            while valida:
                if escolha == "SIM":
                    print("Insira os dados do cliente.")
                    clienteatualizado = clienteAtualizado()
                    teste.alterarCliente(clienteatualizado)
                    validadorOpcao1 = retornaMenuPrincipal()
                    valida = False

                elif escolha == "NÃO" or escolha == "NAO":
                    validadorOpcao1 = retornaMenuPrincipal()
                    valida = False

                else:
                    print("Opção inválida.")
                    valida = True

        elif opcaoCliente == 4:
            print("DELETAR")
            print("ATUALIZAÇÃO")
            print("Insira o CPF do cliente.")
            busca = validaCpf()
            teste = Cliente()
            teste.consultarCliente(busca)
            escolha = input("Deseja deletar este cliente?(sim/não)").upper()
            valida = True
            while valida:
                if escolha == "SIM":
                    teste.deletarCliente(busca)
                    validadorOpcao1 = retornaMenuPrincipal()
                    valida = False

                elif escolha == "NÃO" or escolha == "NAO":
                    validadorOpcao1 = retornaMenuPrincipal()
                    valida = False

                else:
                    print("Opção inválida.")
                    valida = True

        elif opcaoCliente == 5:
            validadorOpcao1 = False
        else:
            print("operação inválida.")




def opcao2():
    validaOpcao2 = True
    while validaOpcao2:
        print("MENU ORDEM\n1 - Cadastrar ordem\n2 - Sair")
        opcao = int(input("Escolha a opção: "))
        if opcao == 1:
            print("Insira os dados da ação.")
            dados = dadosOrdem()
            listaAcao.append(dados)
            ordem = Ordem()
            ordem.cadastrarOrdem(dados)

            validaOpcao2 = retornaMenuPrincipal()
        elif opcao == 2:
            validaOpcao2 = False
        else:
            print("operação inválida.")


def opcao4():
    validaOpcao4 = True
    while validaOpcao4:
        print("RELATÓRIO DA CARTEIRA")
        ticket = input("Digite o nome da ação: ").upper()
        nome_arquivo = input("Digite o nome do arquivo: ")
        obterDadosAcao(ticket, nome_arquivo)

        validaOpcao4 = retornaMenuPrincipal()


def opcao3():
    validaOpcao3 = True
    while validaOpcao3:
        analiseDaCarteira()
        validaOpcao3 = retornaMenuPrincipal()


def dadosCliente():
    dadosCliente = {
        "nome": formataTexto(input("Nome: ")),
        "cpf": validaCpf(),
        "rg": validaRg(),
        "data_nascimento": validaDataNascimento(),
        "endereco": validaCep(),
    }
    return dadosCliente


def clienteAtualizado():
    dadosCliente = {
        "nome": formataTexto(input("Nome: ")),
        "rg": validaRg(),
        "data_nascimento": validaDataNascimento(),
        "endereco": validaCep(),
    }
    return dadosCliente


def dadosOrdem():
    dadosOrdem = {
        "nome": input("Nome: "),
        "ticket": input("Ticket: "),
        "valor_compra": validaCompra(),
        "quantidade_compra": validaQunatidade(),
        "data_compra": validaDataCompra(),
        "cliente_id": validaId()
    }
    return dadosOrdem

if __name__=="__main__":
    opcao2()

