"""
This script gives us the max, min and average.
The pairs list is shared from the other files.
"""

from datetime import datetime

import pandas as pd

# We declare in our list the pairs we need.
# Each pair is a tuple.

pairs = [
    ("MXN", "ARS"),
    ("MXN", "AUD"),
    ("MXN", "BRL"),
    ("MXN", "CAD"),
    ("MXN", "CHF"),
    ("MXN", "CNY"),
    ("MXN", "EUR"),
    ("MXN", "GBP"),
    ("MXN", "JPY"),
    ("MXN", "USD")
]


def get_insights(pair):
    """Converts the .csv into a pandas Dataframe and gets the insights.
    In this project, the data was resampled to 1 month intervals.
    Then the values were formatted for Markdown.

    Parameters
    ----------
    pair : tuple
        A tuple of 2 strings representing the currencies pair.

    """

    df = pd.read_csv("{}{}.csv".format(
        pair[0], pair[1]), parse_dates=["datetime"], index_col="datetime")

    resampled_df = df.resample("M").mean()

    initial_value = resampled_df["inverse"].iloc[0]
    latest_value = resampled_df["inverse"].iloc[-1]
    percentage_change = (latest_value - initial_value) / initial_value * -100
    min_value = resampled_df["inverse"].min()
    max_value = resampled_df["inverse"].max()
    mean_value = resampled_df["inverse"].mean()

    final_string = "| {} | {:.2f} | {:.2f} | {:.2f}% | {:.2f} | {:.2f} | {:.2f} |".format(
        pair[1], initial_value, latest_value, percentage_change, min_value, max_value, mean_value)

    print(final_string)


if __name__ == "__main__":

    for pair in pairs:
        get_insights(pair)
