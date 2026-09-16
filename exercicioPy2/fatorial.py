#Declaração de variáveis
numero: int = 0
fatorial: int = 1
#Inicio
numero = int(input("Digite o número: "))

for cont in range(1, numero + 1, 1):
    fatorial = fatorial * cont
print("O fatorial é: ", fatorial)
#Fim