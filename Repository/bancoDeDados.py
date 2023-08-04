import psycopg2
import os





class BancoDeDados:


    def __init__(self):
        self.connection = psycopg2.connect(**self.retornaParametrosConexaoBancoDeDados())
        self.cursor = self.connection.cursor()



    def __del__(self):
        self.cursor.close()
        self.connection.close()


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
            cliente['cep']['cep'],
            cliente['cep']['logradouro'],
            cliente['cep']['complemento'],
            cliente['cep']['bairro'],
            cliente['cep']['cidade'],
            cliente['cep']['estado'],
            cliente['cep']['numero_residencia']
        )
        self.cursor.execute(insertQuery, values)
        self.connection.commit()

    def select(self, cliente):
        print("Buscando clientes no banco de dados.")
        selectQuery = f"SELECT * FROM CLIENTE where cpf ='"+ cliente['cpf']+"';"
        self.cursor.execute(selectQuery)
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)
        return clientes


    def retornaParametrosConexaoBancoDeDados(self):
        parametrosConexao = {
            "user": os.getenv("user"),
            "password": os.getenv("password"),
            "host": os.getenv("host"),
            "port": os.getenv("port"),
            "database":  os.getenv("database")
        }

        return parametrosConexao


conexao = BancoDeDados()
cliente = {'cpf': "362.479.370-59"}
conexao.select(cliente)

