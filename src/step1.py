"""This script will connect to the OFX public API, download the data and convert it to .csv"""

import csv
import time

import requests

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


def download_data(pair):
    """Downloads the specified pair with a daily interval for the last 10 years."""

    url = "https://api.ofx.com/PublicSite.ApiService/SpotRateHistory/10year/{}/{}?DecimalPlaces=6&ReportingInterval=daily&format=json"

    with requests.get(url.format(pair[0], pair[1])) as response:

        with open("{}{}.csv".format(pair[0], pair[1]), "w", encoding="utf-8", newline="") as temp_file:

            writer = csv.writer(temp_file)

            for item in response.json()["HistoricalPoints"]:
                writer.writerow([item["PointInTime"], item["InverseInterbankRate"], item["InterbankRate"]])


if __name__ == "__main__":

    for pair in pairs:
        download_data(pair)
        print("Finished:", pair[0], pair[1])
        time.sleep(1)
