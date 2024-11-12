import threading
import pandas as pd
from utils.data_loader import load_data

def process_data_chunk(chunk, results, index):
    # Perform some I/O bound task, e.g., network request
    results[index] = chunk.sum()

if __name__ == "__main__":
    data = load_data("data/large_dataset.csv")
    num_threads = 8
    chunks = np.array_split(data, num_threads)
    results = [None] * num_threads
    threads = []

    # Start threads
    for i in range(num_threads):
        thread = threading.Thread(target=process_data_chunk, args=(chunks[i], results, i))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Combine results
    print("Total sum:", sum(results))