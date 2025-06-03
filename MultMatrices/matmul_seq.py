import numpy as np
import sys
import time
import csv
import os

def main():
    if len(sys.argv) < 2:
        print("Uso: python matmul_seq.py N")
        sys.exit(1)
    N = int(sys.argv[1])
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    start = time.perf_counter()
    C = np.matmul(A, B)
    end = time.perf_counter()
    execution_time = end - start

    print(f"Tiempo de ejecución: {execution_time:.4f} segundos")

    results_file = "matmul_results.csv"
    header = ["implementacion", "N", "tiempo"]
    new_row = ["secuencial", N, execution_time]

    file_exists = os.path.isfile(results_file)
    with open(results_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(new_row)

if __name__ == "__main__":
    main()
