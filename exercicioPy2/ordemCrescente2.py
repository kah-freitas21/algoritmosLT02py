#Declaração de variáveis
valorCrescente1: float = 0
valorCrescente2: float = 0
valorCrescente3: float = 0
numero: float = 0
#Inicio

valorCrescente1 = float(input("Digite o primeiro valor em oredem crescente: "))
valorCrescente2 = float(input("Digite o segundo valor em oredem crescente: "))
valorCrescente3 = float(input("Digite o terceiro valor em oredem crescente: "))
numero = float(input("Digite um número qualquer: "))

if (numero <= valorCrescente1):
    print("A ordem crescente é: ", numero,  ",",valorCrescente1, ",", valorCrescente2,  ",",valorCrescente3)
elif (numero <= valorCrescente2):
    print("A ordem crescente é: ", valorCrescente1,  ",",numero, ",", valorCrescente2,  ",",valorCrescente3)
elif (numero <= valorCrescente3):
    print("A ordem crescente é: ", valorCrescente1, ",",valorCrescente2, ",", numero,  ",",valorCrescente3)
else:
    
    print("A ordem crescente é: ", valorCrescente1,  ",",valorCrescente2,  ",",valorCrescente3, ",", numero,)
#Fim

