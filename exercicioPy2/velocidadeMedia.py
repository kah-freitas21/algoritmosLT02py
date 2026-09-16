#Declaração de variáveis
numVoltas: float = 0
extensaoCircuito: float = 0
tempo: float = 0
velocidadeMedia: float = 0
distancia: float = 0
#Inicio
numVoltas = int(input("Digite o número de voltas: "))
extensaoCircuito = int(input("Digite a extensão do circuito: "))
tempo = int(input("Digite o tempo: "))

distancia = numVoltas * extensaoCircuito
distancia = distancia / 1000
tempo = tempo / 60
velocidadeMedia = distancia / tempo

print("A velocidade média é: ", velocidadeMedia)
#Fim

