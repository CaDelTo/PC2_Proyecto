from mpi4py import MPI
import numpy as np
import sys
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def main():
    if len(sys.argv) != 2:
        if rank == 0:
            print("Uso: mpirun -np <nprocs> python matmul_mpi.py N")
        sys.exit(1)

    N = int(sys.argv[1])
    rows_per_proc = N // size

    # Solo el proceso 0 genera las matrices completas
    if rank == 0:
        A = np.random.rand(N, N).astype(np.float32)
        B = np.random.rand(N, N).astype(np.float32)
    else:
        A = None
        B = np.empty((N, N), dtype=np.float32)

    # Todos necesitan B completa
    comm.Bcast(B, root=0)

    # Distribuir las filas de A
    local_A = np.empty((rows_per_proc, N), dtype=np.float32)
    comm.Scatter(A, local_A, root=0)

    # Multiplicación local
    start = MPI.Wtime()
    local_C = np.dot(local_A, B)
    end = MPI.Wtime()

    # Reunir los resultados
    if rank == 0:
        C = np.empty((N, N), dtype=np.float32)
    else:
        C = None
    comm.Gather(local_C, C, root=0)

    if rank == 0:
        print(f"Tiempo de ejecución MPI: {end - start:.4f} segundos")

if __name__ == "__main__":
    main()
