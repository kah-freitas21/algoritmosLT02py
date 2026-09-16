precoAtual: float = 0
novoPreco: float = 0
vendaMensal: float = 0
#Inicio

precoAtual = float(input("Digite o preço atual: "))
vendaMensal = float(input("Digite a quantidade de venda mensal: "))

if (vendaMensal < 500) and (precoAtual < 30):
    novoPreco = precoAtual * 1.1
    print("O novo preço é: ", novoPreco)
elif (vendaMensal >= 500 and vendaMensal <1000) and (precoAtual >= 30 and precoAtual < 80):
    novoPreco = precoAtual * 1.15
    print("O novo preço é: ", novoPreco)
elif (vendaMensal >= 1000) and (precoAtual >= 80):
    novoPreco = precoAtual * 0.95
    print("O novo preço é: ", novoPreco)
else:
    novoPreco = precoAtual
    print("O novo preço é: ", novoPreco)
#Fim


