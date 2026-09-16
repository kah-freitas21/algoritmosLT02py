# Declaração de variáveis

maior: int = 0
menor: int = 0
i: int = 1
num: int = 0

# Início

while (i <= 100):

    num = int(input("Digite um número: "))

    if (i == 1):
        maior = num
        menor = num
    else:
        if (num > maior):
            maior = num

        if (num < menor):
            menor = num

    i = i + 1

print("Maior: ", maior)
print("Menor: ", menor)

# Fim
