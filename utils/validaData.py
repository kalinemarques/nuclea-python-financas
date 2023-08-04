from datetime import datetime



def validaData():
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



