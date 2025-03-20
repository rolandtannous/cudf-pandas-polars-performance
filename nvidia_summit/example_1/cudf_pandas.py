import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# synthetize some time series data
rng = pd.date_range("2023-01-01", "2023-02-01", periods=1_000_000)
df = pd.DataFrame(
    {
        "id": np.random.randint(0, 100, len(rng)),
        "a": np.random.rand(len(rng)),
        "b": np.random.rand(len(rng)),
    },
    index=rng,
)

# filter for data between 9:30am and 4:00pm
df = df.iloc[rng.indexer_between_time("9:30", "16:00")]

# group and compute on the data
results = df.groupby("id").mean()

# plot the results
_ = sns.lineplot(results)
_ = plt.xticks(rotation=30)
plt.show()
