from mpi4py import MPI
import sys
import time

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if len(sys.argv) != 2:
    if rank == 0:
        print("Uso: mpiexec -n <n_procesos> python primes_mpi.py D")
    sys.exit(1)

D = int(sys.argv[1])
inicio = 10**(D-1)
fin = 10**D
rango_total = list(range(inicio + rank, fin, size))

t0 = time.time()
conteo_local = sum(1 for i in rango_total if es_primo(i))
t1 = time.time()

conteo_total = comm.reduce(conteo_local, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Cantidad total de primos con {D} dígitos: {conteo_total}")
    print(f"Tiempo MPI con {size} procesos: {t1 - t0:.6f} segundos")
