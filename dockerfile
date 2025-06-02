FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    mpich \
    build-essential \
    && pip install numpy mpi4py numba

WORKDIR /app
COPY . /app

CMD ["/bin/bash"]
