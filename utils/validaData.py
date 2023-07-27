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
                print("A data de nascimento não pode ser maior que a data autual.")

        except ValueError as e:
            print(e,"\nPor favor digite a data novamente.")


if __name__ == "__main__":
    validaDataNascimento()

