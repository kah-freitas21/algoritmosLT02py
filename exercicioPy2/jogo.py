#Declaração de variáveis
horaInicio: int = 0
horaFinal: int = 0
minutoInicio: int = 0
minutoFinal: int = 0
hora: int = 0
minuto: int = 0

#Inicio
horaInicio = int(input("Digite a hora início: "))
minutoInicio = int(input("Digite o minuto início: "))
horaFinal = int(input("Digite a hora final: "))
minutoFinal = int(input("Digite o minuto final: "))

if (horaFinal < horaInicio):
    horaFinal = horaFinal + 24
if (minutoFinal < minutoInicio):
    minutoFinal = minutoFinal + 60
    horaFinal = horaFinal - 1
hora = horaFinal - horaInicio
minuto = minutoFinal - minutoInicio
print("O jogo durou", hora, "horas e", minuto, "minutos")
#Fim