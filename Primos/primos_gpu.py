import sys
import math
import time
import numpy as np
from numba import cuda

@cuda.jit
def gpu_prime_check(start, primes):
    idx = cuda.grid(1)
    n = start + idx
    if idx < primes.size:
        if n < 2:
            primes[idx] = 0
            return
        if n == 2:
            primes[idx] = 1
            return
        if n % 2 == 0:
            primes[idx] = 0
            return
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                primes[idx] = 0
                return
        primes[idx] = 1

def main():
    if len(sys.argv) != 2:
        print("Uso: python primes_gpu.py D")
        sys.exit(1)

    D = int(sys.argv[1])
    start_num = 10**(D - 1)
    end_num = 10**D
    count_range = end_num - start_num

    threads_per_block = 128
    blocks_per_grid = (count_range + threads_per_block - 1) // threads_per_block

    primes = np.zeros(count_range, dtype=np.uint8)
    d_primes = cuda.to_device(primes)

    start = time.time()
    gpu_prime_check[blocks_per_grid, threads_per_block](start_num, d_primes)
    d_primes.copy_to_host(primes)
    end = time.time()

    total_primes = np.sum(primes)
    print(f"Cantidad de primos con {D} dígitos: {total_primes}")
    print(f"Tiempo de ejecución GPU: {end - start:.4f} segundos")

if __name__ == "__main__":
    main()
