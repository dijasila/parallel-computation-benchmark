import time
from multiprocessing_example import main as run_multiprocessing
from threading_example import main as run_threading
from dask_example import compute_sum as run_dask
from mpi_example import main as run_mpi

def benchmark(func):
    start_time = time.time()
    func()
    return time.time() - start_time

if __name__ == "__main__":
    times = {
        "Multiprocessing": benchmark(run_multiprocessing),
        "Threading": benchmark(run_threading),
        "Dask": benchmark(run_dask),
        "MPI": benchmark(run_mpi),
    }

    with open("benchmarks/results/benchmark_results.txt", "w") as f:
        for method, duration in times.items():
            f.write(f"{method}: {duration} seconds\n")