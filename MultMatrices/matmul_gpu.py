import cupy as cp
import time
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: python matmul_gpu.py N")
        sys.exit(1)

    N = int(sys.argv[1])

    # Generar matrices en GPU
    A = cp.random.rand(N, N, dtype=cp.float32)
    B = cp.random.rand(N, N, dtype=cp.float32)

    cp.cuda.Device(0).synchronize()
    start = time.time()
    C = cp.dot(A, B)
    cp.cuda.Device(0).synchronize()
    end = time.time()

    print(f"Tiempo de ejecución GPU: {end - start:.4f} segundos")

if __name__ == "__main__":
    main()
