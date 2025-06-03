from mpi4py import MPI
import numpy as np
import sys
import time
import csv
import os

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if len(sys.argv) < 2:
        if rank == 0:
            print("Uso: mpiexec -n <num_procesos> python matmul_mpi.py N")
        sys.exit(1)

    N = int(sys.argv[1])
    rows_per_process = N // size

    # Solo el proceso 0 genera los datos
    A = None
    B = None
    if rank == 0:
        A = np.random.rand(N, N)
        B = np.random.rand(N, N)

    # Broadcast de B
    B = comm.bcast(B, root=0)

    # Scatter de A
    local_A = np.zeros((rows_per_process, N))
    comm.Scatter(A, local_A, root=0)

    # Medir tiempo solo en el rank 0
    comm.Barrier()
    start = time.perf_counter()

    # Multiplicación local
    local_C = np.matmul(local_A, B)

    # Gather de los resultados
    C = None
    if rank == 0:
        C = np.zeros((N, N))
    comm.Gather(local_C, C, root=0)

    comm.Barrier()
    end = time.perf_counter()

    if rank == 0:
        execution_time = end - start
        print(f"Tiempo de ejecución MPI: {execution_time:.4f} segundos con {size} procesos")

        results_file = "matmul_results.csv"
        header = ["implementacion", "N", "tiempo", "workers"]
        new_row = ["mpi", N, execution_time, size]

        file_exists = os.path.isfile(results_file)
        with open(results_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(header)
            writer.writerow(new_row)

if __name__ == "__main__":
    main()
