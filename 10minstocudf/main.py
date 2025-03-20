"""
Pandas, cupy, RAPIDS cuDF and Dask-cuDF Demonstration

This script demonstrates basic usage of dataframe and distributed GPU dataframe Libraries. for distributed GPU DataFrame.

Key Features Demonstrated:
- Creating cuDF Series and DataFrames
- Converting between Pandas and cuDF DataFrames
- Using Dask-cuDF for distributed operations
- Basic DataFrame operations (querying, indexing)
- Handling missing values
- Random number generation with cuPy

Dependencies:
- cudf: GPU-accelerated DataFrame library
- cupy: GPU-accelerated NumPy-like library
- dask_cudf: Distributed GPU DataFrame operations
- pandas: CPU-based DataFrame library

Example Usage:
    python main.py

Note: Requires NVIDIA GPU with CUDA support and RAPIDS installed.
"""

import os

import cudf
import cupy as cp
import dask_cudf
import pandas as pd

# Set random seed for reproducibility
cp.random.seed(12)

# Create a cuDF Series with some missing data
s = cudf.Series([1, 2, 3, None, 4])
print("cuDF Series:")
print(s)

# Convert cuDF Series to Dask-cuDF with 2 partitions
ds = dask_cudf.from_cudf(s, npartitions=2)
print("\nDask-cuDF Series (first 3 elements):")
print(ds.head(3))

# Create a cuDF DataFrame with three columns
df = cudf.DataFrame(
    {
        "a": list(range(20)),  # Column with values 0-19
        "b": list(reversed(range(20))),  # Column with values 19-0
        "c": list(range(20)),  # Another column with values 0-19
    }
)
print("\ncuDF DataFrame:")
print(df)

# Convert cuDF DataFrame to Dask-cuDF with 2 partitions
ddf = dask_cudf.from_cudf(df, npartitions=2)
print("\nDask-cuDF DataFrame (first few rows):")
print(ddf.head())

# Create a Pandas DataFrame with missing values
pdf = pd.DataFrame({"a": [0, 1, 2, 3], "b": [0.1, 0.2, None, 0.3]})
# Convert Pandas DataFrame to cuDF
gdf = cudf.DataFrame.from_pandas(pdf)
print("\ncuDF DataFrame converted from Pandas:")
print(gdf)

# Convert cuDF DataFrame to Dask-cuDF with 2 partitions
dask_gdf = dask_cudf.from_cudf(gdf, npartitions=2)
print("\nDask-cuDF DataFrame from Pandas (first 2 rows):")
print(dask_gdf.head(n=2))

# Access a single column from the DataFrame
print("\nColumn 'a' from cuDF DataFrame:")
print(df["a"])

# Query the DataFrame using a condition
print("\nRows where column 'b' equals 3:")
print(df.query("b == 3"))

# Query the Dask-cuDF DataFrame and compute the result
print("\nDask-cuDF query results (b == 3):")
print(ddf.query("b == 3").compute())  # suitable if the number of results is small
