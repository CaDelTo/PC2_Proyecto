import numpy as np
import time
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: python matmul_seq.py N")
        sys.exit(1)

    N = int(sys.argv[1])

    # Generar matrices aleatorias
    A = np.random.rand(N, N).astype(np.float32)
    B = np.random.rand(N, N).astype(np.float32)

    start = time.time()
    C = np.dot(A, B)
    end = time.time()

    print(f"Tiempo de ejecución: {end - start:.4f} segundos")

if __name__ == "__main__":
    main()
