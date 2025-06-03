# Dockerfile

# Base image: Ubuntu
FROM ubuntu:22.04

# Evita interacción al instalar
ARG DEBIAN_FRONTEND=noninteractive

# Actualiza el sistema e instala Python, pip, OpenMPI y otras dependencias
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev openmpi-bin libopenmpi-dev \
    build-essential git && \
    apt-get clean

# Instala numpy y mpi4py
RUN python3 -m pip install numpy mpi4py

# Instala Numba y CuPy (para GPU)
RUN python3 -m pip install numba cupy-cuda11x

# Crea carpetas de trabajo
WORKDIR /workspace
RUN mkdir -p MultMatrices Primos

# Indicaciones de uso (documentación)
CMD ["/bin/bash"]
