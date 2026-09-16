# Declaração de variáveis
numero: int = 0
serie: float = 0
# Início
numero = int(input("Digite o número: "))
for cont in range(1, numero + 1, 1):
    serie = serie + 1 / cont
print(serie)
# Fim