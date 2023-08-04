import psycopg2
import os


def retornaParametrosConexaoBancoDeDados():
    parametrosConexao = {
        "user": os.getenv("user"),
        "password": os.getenv("password"),
        "host": os.getenv("host"),
        "port": os.getenv("port"),
        "database":  os.getenv("database")
    }

    return parametrosConexao



def conexaoPostgres():
    connection = psycopg2.connect(**retornaParametrosConexaoBancoDeDados())
    cursor = connection.cursor()
    return cursor, connection



def selecionaClienteBancoDeDados():
    print("Buscando clientes no banco de dados.")
    selectQuery = "SELECT * FROM CLIENTE"
    cursor, connection = conexaoPostgres()
    cursor.execute(selectQuery)
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)


print("Execultando banco de dados")
print(selecionaClienteBancoDeDados())



