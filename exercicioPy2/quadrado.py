# Declaração de variáveis
numero: float = 0
quadrado: float = 0

# Início
for cont in range(10, 151, 1):
    numero = cont
    quadrado = numero * numero
    print("O quadrado de", numero, "é:", quadrado)
# Fim