from Repository.bancoDeDados import BancoDeDados


class BancoDeDadosCliente(BancoDeDados):


    def __init__(self):
        super().__init__()


    def insert(self,cliente):
        print("Inserindo cliente no banco de dados.")
        insertQuery = """
        INSERT INTO public.cliente (
        nome, cpf, rg, data_nascimento, cep, logradouro, complemento,
        bairro, cidade, estado, numero_residencia)
        VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s);
        """

        values = (
            cliente['nome'],
            cliente['cpf'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['endereco']['cep'],
            cliente['endereco']['logradouro'],
            cliente['endereco']['complemento'],
            cliente['endereco']['bairro'],
            cliente['endereco']['cidade'],
            cliente['endereco']['estado'],
            cliente['endereco']['numero_residencia']
        )
        self.cursor.execute(insertQuery, values)
        self.connection.commit()

    def select(self, cpf):
        print("Buscando cliente no banco de dados.")
        selectQuery = f"SELECT * FROM CLIENTE where cpf = %s;"
        self.cursor.execute(selectQuery, (cpf,))
        clientes = self.cursor.fetchall()

        return clientes



    def delete(self, cliente):
        print("Deletando cliente do banco de dados.")
        deleteQuery = f"DELETE FROM CLIENTE where cpf = %s;"
        self.cursor.execute(deleteQuery, (cliente['cpf'],))
        self.connection.commit()
        print("Cliente deletado com sucesso!")




    def update(self,cliente):
        print("Atualizando cliente no banco de dados.")
        updateQuery = f"""
        UPDATE CLIENTE SET nome = %s, rg = %s, data_nascimento = %s, cep = %s, logradouro = %s,
        complemento = %s, bairro = %s, cidade = %s, estado = %s, numero_residencia = %s
        where cpf = %s;"""

        endereco = cliente.get('endereco', {})
        set = (
            cliente['nome'],
            cliente['rg'],
            cliente['data_nascimento'],
            endereco.get('cep', ''),
            endereco.get('logradouro', ''),
            endereco.get('complemento', ''),
            endereco.get('bairro', ''),
            endereco.get('cidade', ''),
            endereco.get('estado', ''),
            endereco.get('numero_residencia', ''),
            cliente.get('cpf', '')
        )

        self.cursor.execute(updateQuery, set)
        self.connection.commit()
        print("Cliente atualizado com sucesso!")

    def buscarOrdensPorCpfCliente(self, cpf):
        query = """
            SELECT o.nome, o.ticket, o.valor_compra, o.quantidade_compra, o.data_compra
            FROM cliente c
            JOIN ordem o ON c.id = o.cliente_id
            WHERE c.cpf = %s;
            """

        self.cursor.execute(query, (cpf,))
        ordens = self.cursor.fetchall()
        return ordens





