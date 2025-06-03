from mpi4py import MPI
import sys
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def main():
    if len(sys.argv) != 2:
        if rank == 0:
            print("Uso: mpirun -np <nprocs> python primes_mpi.py D")
        sys.exit(1)

    D = int(sys.argv[1])
    start_num = 10**(D - 1)
    end_num = 10**D
    total_range = end_num - start_num
    chunk = total_range // size
    local_start = start_num + rank * chunk
    local_end = start_num + (rank + 1) * chunk if rank != size - 1 else end_num

    start = MPI.Wtime()
    local_count = sum(1 for i in range(local_start, local_end) if is_prime(i))
    total_count = comm.reduce(local_count, op=MPI.SUM, root=0)
    end = MPI.Wtime()

    if rank == 0:
        print(f"Cantidad de primos con {D} dígitos: {total_count}")
        print(f"Tiempo de ejecución MPI: {end - start:.4f} segundos")

if __name__ == "__main__":
    main()
