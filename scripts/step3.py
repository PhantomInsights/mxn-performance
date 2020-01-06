"""
In this step we generate charts from our data.
This file has similar code from step2.py
"""

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

plt.rcParams["figure.figsize"] = [12, 7]
plt.style.use("fivethirtyeight")

# We declare in our list the pairs we need for our figure.
# Each pair is a tuple.
# We split the list into two, to make the plots more readable.

top_pairs = [
    ("MXN", "CHF"),
    ("MXN", "EUR"),
    ("MXN", "GBP"),
    ("MXN", "JPY"),
    ("MXN", "USD")
]

popular_pairs = [
    ("MXN", "ARS"),
    ("MXN", "AUD"),
    ("MXN", "BRL"),
    ("MXN", "CAD"),
    ("MXN", "CNY")
]


def generate_fig(pairs, file_name):
    """Converts the .csv into a pandas Dataframe and plots the relevant data.
    In this project the data is resampled to 1 month intervals.

    Parameters
    ----------
    pair : tuple
        A tuple of 2 strings representing the currencies pair.

    file_name : str
        The file name of the generated figure.

    """

    for pair in pairs:

        df = pd.read_csv("{}{}.csv".format(pair[0], pair[1]), parse_dates=[
                         "datetime"], index_col="datetime")

        resampled_df = df.resample("M").mean()

        initial_value = resampled_df["inverse"].iloc[0]

        pct_changes = [(item - initial_value) / initial_value * -100 for item in resampled_df["inverse"]]

        plt.plot(resampled_df.index, pct_changes, label=pair[1], linewidth=1.5)

    plt.ylabel("Percent Change")
    plt.title("Mexican Peso Performance")
    plt.legend()
    plt.draw()
    plt.savefig(file_name)
    plt.close()


if __name__ == "__main__":

    # We call the same function 2 times with different parameters.
    generate_fig(top_pairs, "top5.png")
    generate_fig(popular_pairs, "popular.png")
