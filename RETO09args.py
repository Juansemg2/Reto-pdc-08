#Tres funciones convertidas en args

#Funcion 1 Suma de dos numeros

def suma_numeros(*args) -> int:
    return sum(args)

#Funcion 2 Mayor de dos numeros

def maximo_valor(*args):
    return max(args)

#Funcion 3 aves segun peso
def calcular_prestamo(*args):
    capital, interes, meses = args
    total = capital * (1 + interes) ** meses
    return total

P = float(input("Ingrese el capital prestado: "))
i = float(input("Ingrese la tasa de interés mensual: "))
n = int(input("Ingrese el número de meses: "))

C = calcular_prestamo(P, i, n)

print("El valor total a pagar es: " + str(C))