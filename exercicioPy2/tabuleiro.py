#Declaração de variáveis
graos: int = 1
total: int = 0
i: int = 1
#Inicio
while (i <= 64):
    total = total + graos
    graos = graos * 2
    i = i + 1
print("Total de grãos:", total)
#Fim