import sys
import time

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
        print("Uso: python primes_seq.py D")
        sys.exit(1)

    D = int(sys.argv[1])
    start_num = 10**(D - 1)
    end_num = 10**D

    start = time.time()
    count = sum(1 for i in range(start_num, end_num) if is_prime(i))
    end = time.time()

    print(f"Cantidad de primos con {D} dígitos: {count}")
    print(f"Tiempo de ejecución: {end - start:.4f} segundos")

if __name__ == "__main__":
    main()
