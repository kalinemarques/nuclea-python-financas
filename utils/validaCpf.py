from validate_docbr import CPF

def validaCpf ():

    cpfValidador = CPF()

    while True:
        cpf = input("CPF: ")
        resultadoValidacao = cpfValidador.validate(cpf)

        if (resultadoValidacao):
            #ver máscara masc
            #ver um modo de tirar os pontos caso ele digite os pontos
            #alguma função como o replace

            cpfFormatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            return cpfFormatado
        else:
            print("CPF inválido, digite novamente: ")

