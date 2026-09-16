#Declaração de variáveis
num: int = 0
fibonacci: int = 0
a: int = 0
b: int = 1
i: int = 1

#Inicio
num = int(input("Digite um número: "))
while ( i <= num):
    print(a)
    fibonacci = a + b
    a = b
    b = fibonacci
    i = i + 1
#Fim