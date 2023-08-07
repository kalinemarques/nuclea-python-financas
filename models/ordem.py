from Repository.bancoDeDadosOrdem import BancoDeDadosOrdem


class Ordem:

    def __init__(self):
        self.bancoDeDados = BancoDeDadosOrdem()
        self.nome = None
        self.ticket = None
        self.valor_compra = None
        self.quantidade_compra = None
        self.data_compra = None
        self.cliente_id = None


    def cadastrarOrdem(self,ordem):
        self.nome = ordem['nome']
        self.ticket = ordem['ticket']
        self.valor_compra = ordem['valor_compra']
        self.quantidade_compra = ordem['quantidade_compra']
        self.data_compra = ordem['data_compra']
        self.cliente_id = ordem['cliente_id']

        with self.bancoDeDados:
            self.bancoDeDados.insert(ordem)
        print("Ordem cadastrda com sucesso!")