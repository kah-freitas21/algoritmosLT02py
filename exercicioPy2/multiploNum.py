#Declaração de variáveis
valor1: int = 0
valor2: int = 0
maior: int = 0 
menor: int = 0
#Inicio

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
if (v1 > v2):
    maior = v1
    menor = v2
else:
    maior = v2
    menor = v1

if (maior % menor == 0):
    print("O maior número é multiplo do menor.")
else:
    print("O maior número NÃO é multiplo do menor.")
#Fim