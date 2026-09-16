# Declaração de variáveis
num: int = 0
i: int = 1
calculo: int = 1
serie: float = 1
# Início
num = int(input("Digite um número: "))
for i in range(1, num + 1, 1):
    calculo = calculo * i
    serie = serie + (1 / calculo)
print(serie)
#Fim