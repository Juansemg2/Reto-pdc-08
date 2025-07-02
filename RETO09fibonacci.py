import time

def fibo_iterativo(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibo_recursivo(n: int) -> int:
    if n <= 1:
        return n
    return fibo_recursivo(n - 1) + fibo_recursivo(n - 2)

if __name__ == "__main__":
    n = 30  

    start_time = time.time()
    fibo_iterativo(n)
    end_time = time.time()
    print("Tiempo Fibonacci Iterativo (n={}):".format(n), end_time - start_time)

    start_time = time.time()
    fibo_recursivo(n)
    end_time = time.time()
    print("Tiempo Fibonacci Recursivo (n={}):".format(n), end_time - start_time)