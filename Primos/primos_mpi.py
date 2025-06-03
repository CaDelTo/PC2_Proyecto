from mpi4py import MPI
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
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if len(sys.argv) < 2:
        if rank == 0:
            print("Uso: mpiexec -n <num_procesos> python primos_mpi.py D")
        sys.exit(1)

    D = int(sys.argv[1])
    start_num = 10**(D-1)
    end_num = 10**D - 1

    numbers = list(range(start_num + rank, end_num + 1, size))

    comm.Barrier()
    start = time.perf_counter()

    local_count = sum(1 for n in numbers if is_prime(n))
    total_count = comm.reduce(local_count, op=MPI.SUM, root=0)

    comm.Barrier()
    end = time.perf_counter()

    if rank == 0:
        execution_time = end - start
        print(f"Primos con {D} dígitos: {total_count}")
        print(f"Tiempo de ejecución MPI: {execution_time:.4f} segundos con {size} procesos")

        results_file = "primos_results.csv"
        header = ["implementacion", "D", "tiempo", "workers"]
        new_row = ["mpi", D, execution_time, size]

        file_exists = os.path.isfile(results_file)
        with open(results_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(header)
            writer.writerow(new_row)

if __name__ == "__main__":
    main()
