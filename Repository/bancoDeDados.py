import psycopg2
import os



class BancoDeDados:
    def __init__(self):
        self.params = self.retornaParametrosConexaoBancoDeDados()
        self.connection = None
        self.cursor = None


    def __enter__(self):
        self.connection = psycopg2.connect(**self.params)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.commit()
            self.connection.close()


    # def __del__(self):
    #     self.cursor.close()
    #     self.connection.close()



    def retornaParametrosConexaoBancoDeDados(self):
        parametrosConexao = {
            "user": os.getenv("user"),
            "password": os.getenv("password"),
            "host": os.getenv("host"),
            "port": os.getenv("port"),
            "database": os.getenv("database")
        }

        return parametrosConexao










