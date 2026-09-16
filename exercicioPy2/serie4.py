#Declaração de variáveis
i: int = 1
serie: float = 0
termo: float = 0
#Inicio
while (i <= 15):
    termo = i / (i * i)
    if (i % 2 == 0):
        serie = serie - termo
    else:
        serie = serie + termo
    i = i + 1
print("Resultado da série: ", serie)
#Fim