import sys
import math
import time
import numpy as np
from numba import njit, prange

@njit(parallel=True)
def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    raiz = int(math.sqrt(n)) + 1
    for i in range(3, raiz, 2):
        if n % i == 0:
            return False
    return True

@njit(parallel=True)
def cuenta_primos(start, end):
    total = 0
    for num in prange(start, end):
        
        if es_primo(num):
            total += 1
    return total

def main():
    if len(sys.argv) != 2:
        print("Uso: python primos_cpu.py D")
        sys.exit(1)

    D = int(sys.argv[1])
    start_num = 10**(D - 1)
    end_num = 10**D

    start = time.time()
    total_primos = cuenta_primos(start_num, end_num)
    end = time.time()

    print(f"Cantidad de primos con {D} dígitos: {total_primos}")
    print(f"Tiempo de ejecución CPU paralelo: {end - start:.4f} segundos")

if __name__ == "__main__":
    main()