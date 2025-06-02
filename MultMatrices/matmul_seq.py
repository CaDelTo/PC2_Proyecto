import numpy as np
import time
import sys

def generar_matrices(N):
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)
    return A, B

def multiplicar_matrices(A, B):
    return np.dot(A, B)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python matmul_seq.py N")
        sys.exit(1)

    N = int(sys.argv[1])
    A, B = generar_matrices(N)

    inicio = time.time()
    C = multiplicar_matrices(A, B)
    fin = time.time()

    print(f"Tiempo secuencial: {fin - inicio:.6f} segundos")
