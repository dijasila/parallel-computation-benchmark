import dask.dataframe as dd

def compute_sum():
    # Load data with Dask
    data = dd.read_csv("data/large_dataset.csv")
    total_sum = data.sum().compute()
    print("Total sum using Dask:", total_sum)

if __name__ == "__main__":
    compute_sum()