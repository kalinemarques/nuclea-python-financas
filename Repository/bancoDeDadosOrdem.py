from Repository.bancoDeDados import BancoDeDados


class BancoDeDadosOrdem(BancoDeDados):


    def __init__(self):
        super().__init__()



    def insert(self, cliente):
        print("Inserindo ordem no banco de dados.")
        insertQuery = """
        INSERT INTO public.ordem (
        nome, ticket, valor_compra, quantidade_compra, data_compra, cliente_id)
        VALUES (%s, %s, %s, %s, %s,%s);
        """

        values = (
            cliente['nome'],
            cliente['ticket'],
            cliente['valor_compra'],
            cliente['quantidade_compra'],
            cliente['data_compra'],
            cliente['cliente_id']
        )
        self.cursor.execute(insertQuery, values)
        self.connection.commit()
