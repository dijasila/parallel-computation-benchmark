#!/bin/bash
#SBATCH --job-name=parallel-benchmark
#SBATCH --output=benchmarks/logs/output_%j.log
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=4
#SBATCH --mem=16GB
#SBATCH --time=01:00:00

module load python/3.8  # Load relevant modules
source env/bin/activate  # Activate virtual environment if needed

srun python src/benchmark.py