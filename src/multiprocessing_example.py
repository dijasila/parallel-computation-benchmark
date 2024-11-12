import multiprocessing as mp
import pandas as pd
from utils.data_loader import load_data

def process_data_chunk(chunk):
    # Perform some CPU-intensive computation
    return chunk.sum()

if __name__ == "__main__":
    data = load_data("data/large_dataset.csv")
    num_processes = mp.cpu_count()

    # Split data into chunks
    chunks = np.array_split(data, num_processes)

    # Set up a pool of workers
    with mp.Pool(num_processes) as pool:
        results = pool.map(process_data_chunk, chunks)

    # Combine results
    print("Total sum:", sum(results))