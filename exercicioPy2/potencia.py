#Declaração de variáveis
base: int = 0
expoente: int = 0
resultado: int  = 1
i: int  = 1
#Inicio
base = int (input("Digite a base: "))
expoente = int (input("Digite o expoente: "))
while (i <= expoente):
    resultado = resultado * base
    i = i + 1
print("Resultado da potência: ", resultado)
#Fim