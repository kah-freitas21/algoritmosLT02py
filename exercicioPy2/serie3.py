#Declaração de variáveis
numerador: int = 1
denominador: int = 1
serie: int = 0
#Inicio
while (numerador <= 50):
    serie = serie + numerador / denominador
    numerador = numerador + 1
    denominador = denominador + 2
print("Resultado é: ", serie)
#Fim