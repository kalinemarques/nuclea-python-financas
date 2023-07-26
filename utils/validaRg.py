import re

#re: explressões regulares

def validaRg():
    padraoRg1 = r'^\d{2}\.\d{3}\.\d{3}\-[0-9A-Za-z]$'
    padraoRg2 = r'^\d{3}\.\d{3}\.\d{3}$'

    #ver como faz para não ter que digitar no formato
    # ver formatos de RG para validar
    #ver regra de verificação
    #https://www.ngmatematica.com/2014/02/como-determinar-o-digito-verificador-do.html
    # rg = 00.000.000.-0

    while True:
        rg = input("RG: ")

        if re.match(padraoRg1,rg) or re.match(padraoRg2,rg):
            return rg
        else:
            print("RG inválido, digite novamente: ")