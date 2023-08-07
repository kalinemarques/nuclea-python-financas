from Repository.bancodeDadosCliente import BancoDeDadosCliente
import pandas as pd


class Cliente:

    def __init__(self):
        self.bancoDeDados = BancoDeDadosCliente()
        self.cpf = None
        self.nome = None
        self.rg = None
        self.data_nascimento = None
        self.cep = None
        self.logradouro = None
        self.complemento = None
        self.bairro = None
        self.cidade = None
        self.estado = None
        self.numero_residencia = None


    def cadastrarCliente(self,cliente):
        self.cpf = cliente['cpf']
        self.nome = cliente['nome']
        self.rg = cliente['rg']
        self.data_nascimento = cliente['data_nascimento']
        self.cep = cliente['endereco']['cep']
        self.logradouro = cliente['endereco']['logradouro']
        self.complemento = cliente['endereco']['complemento']
        self.bairro = cliente['endereco']['bairro']
        self.cidade = cliente['endereco']['cidade']
        self.estado = cliente['endereco']['estado']
        self.numero_residencia = cliente['endereco']['numero_residencia']

        with self.bancoDeDados:
            self.bancoDeDados.insert(cliente)
        print("Cliente cadastrdo com sucesso!")


    def consultarCliente(self,cpf):
        with self.bancoDeDados:
            cliente_data = self.bancoDeDados.select(cpf)
            if cliente_data:
                print("Cliente encontrado:")
                print(cliente_data)
            else:
                print("Cliente não encontrado.")


    def alterarCliente(self, cliente):

        endereco = cliente['endereco']
        cliente_data = {
            #'cpf': self.cpf,
            'nome': self.nome,
            'rg': self.rg,
            'data_nascimento': self.data_nascimento,
            'cep': endereco['cep'],
            'logradouro': endereco['logradouro'],
            'complemento': endereco['complemento'],
            'bairro': endereco['bairro'],
            'cidade': endereco['cidade'],
            'estado': endereco['estado'],
            'numero_residencia': endereco['numero_residencia']
        }
        with self.bancoDeDados:
            self.bancoDeDados.update(cliente_data)


    def deletarCliente(self,cpf):
        cliente = {'cpf': cpf}
        with self.bancoDeDados:
            self.bancoDeDados.delete(cliente)



    def buscarOrdensPorCliente(self, cpf):

        with self.bancoDeDados:
            self.bancoDeDados.buscarOrdensPorCpfCliente(cpf)


    def exibirOrdensPorCpfCliente(self, cpf):
            with self.bancoDeDados:
                ordens = self.bancoDeDados.buscarOrdensPorCpfCliente(cpf)

                if ordens:
                    df = pd.DataFrame(ordens,
                                      columns=['Nome', 'Ticket', 'Valor Compra', 'Quantidade Compra', 'Data Compra'])
                    print(df)
                else:
                    print("Nenhuma ordem encontrada para o cliente.")