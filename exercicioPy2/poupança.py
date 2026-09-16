#Declaração de variáveis
tipo: int = 0
valor: float = 0
valorCorrigido: float = 0

#Inicio
tipo = int(input("Digite o tipo de investimento (1 - Poupança / 2 - Renda Fixa): "))
valor = float(input("Digite o valor do investimento: "))

if (tipo == 1):
    valorCorrigido = valor * 1.03
    print("Valor corrigido: ", valorCorrigido)
elif (tipo == 2):
    valorCorrigido = valor * 1.05
    print("Valor corrigido: ", valorCorrigido)
#Fim