import math
import sys
import time
import csv
import os

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    if len(sys.argv) < 2:
        print("Uso: python primos_seq.py D")
        sys.exit(1)
    D = int(sys.argv[1])
    start_num = 10**(D-1)
    end_num = 10**D - 1

    start = time.perf_counter()
    count = sum(1 for i in range(start_num, end_num + 1) if is_prime(i))
    end = time.perf_counter()

    execution_time = end - start
    print(f"Primos con {D} dígitos: {count}")
    print(f"Tiempo de ejecución: {execution_time:.4f} segundos")

    results_file = "primos_results.csv"
    header = ["implementacion", "D", "tiempo"]
    new_row = ["secuencial", D, execution_time]

    file_exists = os.path.isfile(results_file)
    with open(results_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(new_row)

if __name__ == "__main__":
    main()
