#Declaração de variáveis
dado1: int = 1
dado2: int = 1

#Inicio
while (dado1 <= 6):
    dado2 = 1
    while (dado2 <= 6):
        if (dado1 + dado2 == 7):
            print(dado1, "+", dado2, "= 7")
        dado2 = dado2 + 1
    dado1 = dado1 + 1
#Fim
