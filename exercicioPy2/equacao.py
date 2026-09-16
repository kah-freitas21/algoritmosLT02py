coeficienteA: float = 0
coeficienteB: float = 0
coeficienteoC: float = 0
delta: float = 0
x1: float = 0
x2: float = 0

#Inicio
coeficienteA = float(input("Digite o  cateto A: "))
coeficienteB = float(input("Digite o cateto B: "))
coeficienteC = float(input("Digite o cateto C: "))

if (coeficienteA == 0):
    print("Não é uma equação do 2º grau.")
else:
    delta = (coeficienteB * coeficienteB) - (4 * coeficienteA * coeficienteC)
    if (delta>= 0):
        x1 = (-coeficienteB + (delta ** 0.5) ) / ( 2 * coeficienteA) 
        x2 = (-coeficienteB - (delta ** 0.5) ) / ( 2 * coeficienteA) 
        print("Suas raízes reais são", x1, "e",x2)
    else:
        print("Não possui raízes reais.")
#Fim