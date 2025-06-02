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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python primes_seq.py D")
        sys.exit(1)

    D = int(sys.argv[1])
    inicio = 10**(D-1)
    fin = 10**D

    start_time = time.time()
    conteo = sum(1 for i in range(inicio, fin) if es_primo(i))
    end_time = time.time()

    print(f"Cantidad de primos con {D} dígitos: {conteo}")
    print(f"Tiempo secuencial: {end_time - start_time:.6f} segundos")
