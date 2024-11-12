# Parallel Computation Benchmark for Large Data Processing on HPC

## Project Overview

This repository is designed to benchmark parallel computing techniques for large-scale data processing on High-Performance Computing (HPC) environments. It includes implementations of various parallelization methods using Python libraries, such as:
- **Multiprocessing**: Python's `multiprocessing` library for parallel data processing.
- **Threading**: Python's `threading` library for concurrent tasks.
- **Dask**: A Python library for parallel computing with large datasets.
- **MPI**: Message Passing Interface (MPI) for distributed parallel computing using `mpi4py`.

Each parallelization approach is benchmarked to evaluate performance improvements when handling large datasets.

## Repository Structure

```plaintext
parallel-computation-benchmark/
├── README.md                  # Project overview and setup instructions
├── requirements.txt           # List of required packages
├── data/
│   └── large_dataset.csv      # Sample large dataset for testing
├── src/
│   ├── multiprocessing_example.py  # Multiprocessing implementation
│   ├── threading_example.py        # Threading implementation
│   ├── dask_example.py             # Dask implementation
│   ├── mpi_example.py              # MPI implementation
│   ├── benchmark.py                # Benchmarking script
│   └── utils/
│       └── data_loader.py          # Utility function to load data
├── benchmarks/
│   ├── results/                    # Stores benchmark results
│   └── logs/                       # Stores log files
└── scripts/
    └── submit_job.sh               # HPC job submission script
Setup Instructions
Prerequisites
Python 3.8 or higher
HPC environment with job scheduling (e.g., SLURM, PBS) to run on an HPC cluster.
MPI: Ensure MPI is installed on your system, as it is required for the mpi4py library.
Installation
Clone the Repository


git clone https://github.com/your-username/parallel-computation-benchmark.git
cd parallel-computation-benchmark
Create a Virtual Environment


python3 -m venv env
source env/bin/activate
Install Required Packages


pip install -r requirements.txt
Prepare Data

Place a large dataset (CSV format) in the data/ directory. You can name the file large_dataset.csv or adjust the data loading paths in the code.
Running the Benchmark
Run Locally: You can run individual scripts locally to test each parallelization method.

python src/multiprocessing_example.py
python src/threading_example.py
python src/dask_example.py
mpiexec -n 4 python src/mpi_example.py
Run Benchmark Script: To benchmark all parallelization methods and log the results, use:


python src/benchmark.py
Submit Job to HPC: Use the submit_job.sh script to run the benchmark on an HPC cluster.


sbatch scripts/submit_job.sh