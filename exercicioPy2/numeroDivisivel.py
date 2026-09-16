#Declaração de variáveis
valor: int = 0
#Inicio
valor = int(input("Digite o valor: "))

if (valor % 2 == 0) and ( valor % 3 == 0):
    print("O número é divisível por 2 e 3")
else:
    print("O número NÃO é divisível por 2 e 3") 
#Fim