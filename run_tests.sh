#!/bin/bash

mkdir -p resultados

echo "N,Tiempo_Secuencial" > resultados/multmatrices_seq.csv
echo "N,Procesos,Tiempo_MPI" > resultados/multmatrices_mpi.csv

echo "D,Tiempo_Secuencial" > resultados/primos_seq.csv
echo "D,Procesos,Tiempo_MPI" > resultados/primos_mpi.csv

# Multiplicación de matrices
for N in 128 256 512 1024
do
    # Secuencial
    tiempo=$(python MultMatrices/matmul_seq.py $N | grep Tiempo | awk '{print $3}')
    echo "$N,$tiempo" >> resultados/multmatrices_seq.csv

    # MPI (por ejemplo, con 4 procesos)
    tiempo=$(mpiexec -n 4 python MultMatrices/matmul_mpi.py $N | grep Tiempo | awk '{print $5}')
    echo "$N,4,$tiempo" >> resultados/multmatrices_mpi.csv
done

# Conteo de primos
for D in 4 5 6
do
    # Secuencial
    tiempo=$(python Primos/primos_seq.py $D | grep Tiempo | awk '{print $3}')
    echo "$D,$tiempo" >> resultados/primos_seq.csv

    # MPI (con 4 procesos)
    tiempo=$(mpiexec -n 4 python Primos/primos_mpi.py $D | grep Tiempo | awk '{print $6}')
    echo "$D,4,$tiempo" >> resultados/primos_mpi.csv
done
