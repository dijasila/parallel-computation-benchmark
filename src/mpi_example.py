from mpi4py import MPI
import numpy as np
import pandas as pd
from utils.data_loader import load_data

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def process_data(data):
    # Perform distributed computation here
    return data.sum()

if __name__ == "__main__":
    data = None
    if rank == 0:
        data = load_data("data/large_dataset.csv")
        chunks = np.array_split(data, size)
    else:
        chunks = None

    # Scatter data to all processes
    data_chunk = comm.scatter(chunks, root=0)
    local_sum = process_data(data_chunk)

    # Gather results at root
    global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
    if rank == 0:
        print("Total sum using MPI:", global_sum)