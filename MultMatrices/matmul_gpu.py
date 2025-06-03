import numpy as np
from numba import njit, prange
import time

@njit(parallel=True)
def matmul_numba(A, B):
    N = A.shape[0]
    C = np.zeros((N, N), dtype=np.float64)
    for i in prange(N):
        for j in range(N):
            s = 0.0
            for k in range(N):
                s += A[i, k] * B[k, j]
            C[i, j] = s
    return C

def main(N):
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    start = time.time()
    C = matmul_numba(A, B)
    end = time.time()

    print(f"Tiempo Numba paralelo: {end - start:.4f} segundos")

if __name__ == "__main__":
    main(1000)