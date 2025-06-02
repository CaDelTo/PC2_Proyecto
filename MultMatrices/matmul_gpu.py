import cupy as cp
import time
import sys

def generar_matrices(N):
    A = cp.random.rand(N, N)
    B = cp.random.rand(N, N)
    return A, B

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python matmul_gpu.py N")
        sys.exit(1)

    N = int(sys.argv[1])
    A, B = generar_matrices(N)

    cp.cuda.Device(0).synchronize()
    inicio = time.time()
    C = cp.dot(A, B)
    cp.cuda.Device(0).synchronize()
    fin = time.time()

    print(f"Tiempo GPU (CuPy): {fin - inicio:.6f} segundos")
