import pandas as pd
import numpy as np
import os

def generate_large_dataset(filename="data/large_dataset.csv", num_rows=100, num_columns=10):
    """
    Generate a large CSV file with random data.

    Parameters:
    - filename (str): The file path for the generated CSV file.
    - num_rows (int): Number of rows in the dataset.
    - num_columns (int): Number of columns in the dataset.
    """
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Generate random data
    data = np.random.rand(num_rows, num_columns)
    
    # Create column names
    column_names = [f"col_{i+1}" for i in range(num_columns)]
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame(data, columns=column_names)
    df.to_csv(filename, index=False)
    
    print(f"Large dataset created with {num_rows} rows and {num_columns} columns at {filename}")

if __name__ == "__main__":
    generate_large_dataset()