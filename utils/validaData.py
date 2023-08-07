from datetime import datetime



def validaDataNascimento():
    while True:

        dataNascimento = input("Data de nascimento: ")

        try:
            dataConvertida = datetime.strptime(dataNascimento,"%d/%m/%Y").date()

            dataAtual = datetime.now().date()

            if dataConvertida < dataAtual:
                return dataConvertida.strftime("%d/%m/%Y")
            else:
                print("A data não pode ser maior que a data autual.")

        except ValueError as e:
            print(e,"\nPor favor digite a data novamente.")

def validaDataCarteira():
    while True:

        data = input("Data: ")
        data = data.replace("/", "-")

        try:
            dataConvertida = datetime.strptime(data, "%Y-%m-%d").date()

            dataAtual = datetime.now().date()

            if dataConvertida < dataAtual:
                return dataConvertida.strftime("%Y-%m-%d")
            else:
                print("A data não pode ser maior que a data autual.")

        except ValueError as e:
            print(e,"\nPor favor digite a data novamente.")


def validaDataCompra():
    while True:

        dataCompra = input("Data de compra: ")

        try:
            dataConvertida = datetime.strptime(dataCompra,"%d/%m/%Y").date()

            dataAtual = datetime.now().date()

            if dataConvertida < dataAtual:
                return dataConvertida.strftime("%d/%m/%Y")
            else:
                print("A data não pode ser maior que a data autual.")

        except ValueError as e:
            print(e,"\nPor favor digite a data novamente.")


