# Declaração de variáveis
i: int = 0
num1: int = 0
num2: int = 0
maior: int = 0
menor: int = 0
soma: int = 0
# Início
num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))
if (num1 > num2):
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
i = menor
while (i <= maior):
    if (i % 2 != 0):
        soma = soma + i
    i = i + 1
print(soma)

#Fim