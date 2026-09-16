#Declaração de variáveis
anoNasc: int = 0
mesNasc: int = 0
diaNasc: int = 0
anoAtual: int = 0
mesAtual: int = 0
diaAtual: int = 0
anos: int = 0
meses: int = 0
dias: int = 0
diasMesAnterior: int = 0

#Inicio
anoNasc = int(input("Digite o ano de nascimento: "))
mesNasc = int(input("Digite o mês de nascimento: "))
diaNasc = int(input("Digite o dia de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
mesAtual = int(input("Digite o mês atual: "))
diaAtual = int(input("Digite o dia atual: "))

anos = anoAtual - anoNasc
meses = mesAtual - mesNasc
dias = diaAtual - diaNasc

if (dias < 0):
    if (mesAtual == 1):
        diasMesAnterior = 31
    elif (mesAtual == 2):
        diasMesAnterior = 31
    elif (mesAtual == 3):
        if (anoAtual % 400 == 0 or (anoAtual % 4 == 0 and anoAtual % 100 != 0)):
            diasMesAnterior = 29
        else:
            diasMesAnterior = 28
    elif (mesAtual == 4):
        diasMesAnterior = 31
    elif (mesAtual == 5):
        diasMesAnterior = 30
    elif (mesAtual == 6):
        diasMesAnterior = 31
    elif (mesAtual == 7):
        diasMesAnterior = 30
    elif (mesAtual == 8):
        diasMesAnterior = 31
    elif (mesAtual == 9):
        diasMesAnterior = 31
    elif (mesAtual == 10):
        diasMesAnterior = 30
    elif (mesAtual == 11):
        diasMesAnterior = 31
    elif (mesAtual == 12):
        diasMesAnterior = 30

    dias = dias + diasMesAnterior
    meses = meses - 1
if (meses < 0):
    meses = meses + 12
    anos = anos - 1
print("Idade:", anos, "anos,", meses, "meses e", dias, "dias")
#Fim
