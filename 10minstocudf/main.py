import os

import cudf
import cupy as cp
import dask_cudf
import pandas as pd

cp.random.seed(12)


s = cudf.Series([1, 2, 3, None, 4])
print(s)

ds = dask_cudf.from_cudf(s, npartitions=2)
print(ds.head(3))

df = cudf.DataFrame(
    {
        "a": list(range(20)),
        "b": list(reversed(range(20))),
        "c": list(range(20)),
    }
)
print(df)


ddf = dask_cudf.from_cudf(df, npartitions=2)
print(ddf.head())

pdf = pd.DataFrame({"a": [0, 1, 2, 3], "b": [0.1, 0.2, None, 0.3]})
gdf = cudf.DataFrame.from_pandas(pdf)
print(gdf)


dask_gdf = dask_cudf.from_cudf(gdf, npartitions=2)
print(dask_gdf.head(n=2))

print(df["a"])

print(df.query("b == 3"))

print(ddf.query("b == 3").compute())  # suitable if the number of results is small
