#Declaração de variáveis
num1: int = 0
num2: int = 0
num: int = 0
primo: bool = False
i: int = 2

#Inicio
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

num = num1
while (num <= num2):
    i = 2
    primo = True
    while (i < num):
        if (num % i == 0):
            primo = False
        i = i + 1
    if (primo and num >= 2):
        print(num)
    num = num + 1
#Fim