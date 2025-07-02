# Tres funciones convertidas en lambdas

# Funcion 1 Suma de dos números
suma = lambda a, b: a + b

# Funcion 2Mayor de dos números
mayor = lambda a, b: a if a > b else b

# Funcion 3 Prestamo con interes compuesto
P = float(input("Ingrese el capital prestado: "))
i = float(input("Ingrese la tasa de interés mensual: "))
n = int(input("Ingrese el número de meses: "))
C = (lambda capital, interes, meses: capital * (1 + interes) ** meses)(P, i, n)

print("El valor total a pagar es: " + str(C))