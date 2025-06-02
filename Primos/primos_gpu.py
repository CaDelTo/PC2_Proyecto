import sys
import math
import time
from numba import cuda

@cuda.jit(device=True)
def es_primo_gpu(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

@cuda.jit
def contar_primos_kernel(rango, resultados):
    idx = cuda.grid(1)
    if idx < rango.shape[0]:
        if es_primo_gpu(rango[idx]):
            resultados[idx] = 1

def contar_primos_gpu(inicio, fin):
    import numpy as np
    import cupy as cp

    rango = np.arange(inicio, fin, dtype=np.int32)
    resultados = np.zeros_like(rango, dtype=np.int32)

    d_rango = cuda.to_device(rango)
    d_resultados = cuda.to_device(resultados)

    threads_per_block = 128
    blocks_per_grid = (len(rango) + threads_per_block - 1) // threads_per_block

    contar_primos_kernel[blocks_per_grid, threads_per_block](d_rango, d_resultados)
    d_resultados.copy_to_host(resultados)

    return resultados.sum()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python primes_gpu.py D")
        sys.exit(1)

    D = int(sys.argv[1])
    inicio = 10**(D-1)
    fin = 10**D

    start = time.time()
    total = contar_primos_gpu(inicio, fin)
    end = time.time()

    print(f"Cantidad de primos con {D} dígitos: {total}")
    print(f"Tiempo GPU (CUDA): {end - start:.6f} segundos")
