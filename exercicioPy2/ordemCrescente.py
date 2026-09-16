#Declaração de variáveis
v1: int = 0
v2: int = 0
#Inicio
v1 = int(input("Digite o valor 1: "))
v2 = int(input("Digite o valor 2: "))

if (v1 > v2):
    print("A ordem crescente é: ", v2, "e", v1)
else:
    print("A ordem crescente é: ", v1, "e", v2)
#Fim