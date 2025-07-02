# Función recursiva para calcular la potencia
def potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

if __name__ == "__main__":
    print("2^4 =", potencia(2, 4))