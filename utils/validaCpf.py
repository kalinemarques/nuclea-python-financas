from validate_docbr import CPF

def validaCpf ():

    cpfValidador = CPF()

    while True:
        cpf = input("CPF: ")
        resultadoValidacao = cpfValidador.validate(cpf)

        if (resultadoValidacao):
            cpf = cpf.replace(".", "").replace("-", "")
            cpfFormatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            print(cpfFormatado)
            return cpfFormatado

        else:
            print("CPF inválido, digite novamente.")

if __name__=="__main__":
    validaCpf()