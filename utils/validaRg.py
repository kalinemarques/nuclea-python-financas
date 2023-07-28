import re

#re: explressões regulares

def validaRg():
    padraoRg1 = r'^\d{2}\.\d{3}\.\d{3}\-[0-9A-Za-z]$'
    padraoRg2 = r'^\d{3}\.\d{3}\.\d{3}$'
    padraoRg3 = r'^\d{1}\.\d{3}\.\d{3}$'

    # rg = 00.000.000.-0

    while True:
        rg = input("RG: ")

        if re.match(padraoRg1,rg) or re.match(padraoRg2,rg) or re.match(padraoRg3,rg):
            return rg
        else:
            print("RG inválido, digite novamente.")


if __name__ == "__main__":
    validaRg()
