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


def date_converter(value):
    """Converts the UNIX timestamp to a datetime object."""

    return datetime.utcfromtimestamp(float(int(value) / 1000))


def get_insights(pair):
    """
    Converts the .csv into a pandas Dataframe and gets the insights.
    In this project, the data was resampled to 1 month intervals.
    Then the values were formatted for Markdown.
    """

    df = pd.read_csv("{}{}.csv".format(pair[0], pair[1]), header=None, names=[
                     "timestamp", "rate", "inversed"], converters={"timestamp": date_converter})

    resampled_df = df.resample("M", on="timestamp").mean().reset_index()

    initial_value = resampled_df["rate"].iloc[0]
    latest_value = resampled_df["rate"].iloc[-1]
    percentage_change = (latest_value - initial_value) / initial_value * -1
    min_value = resampled_df["rate"].min()
    max_value = resampled_df["rate"].max()
    mean_value = resampled_df["rate"].mean()

    final_string = "| {} | {:.2f} | {:.2f} | {:.2f}% | {:.2f} | {:.2f} | {:.2f} |".format(
        pair[1], initial_value, latest_value, percentage_change, min_value, max_value, mean_value)

    print(final_string)


if __name__ == "__main__":

    for pair in pairs:
        get_insights(pair)
