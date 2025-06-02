from mpi4py import MPI
import numpy as np
import time
import sys

def generar_matrices(N):
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)
    return A, B

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if len(sys.argv) != 2:
    if rank == 0:
        print("Uso: mpiexec -n <num_procesos> python matmul_mpi.py N")
    sys.exit(1)

N = int(sys.argv[1])
rows_per_proc = N // size

if rank == 0:
    A, B = generar_matrices(N)
else:
    A = None
    B = None

B = comm.bcast(B if rank == 0 else None, root=0)

local_A = np.zeros((rows_per_proc, N))
comm.Scatter(A, local_A, root=0)

inicio = time.time()
local_C = np.dot(local_A, B)
fin = time.time()

C = None
if rank == 0:
    C = np.zeros((N, N))
comm.Gather(local_C, C, root=0)

if rank == 0:
    print(f"Tiempo MPI con {size} procesos: {fin - inicio:.6f} segundos")
