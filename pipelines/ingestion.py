
import pandas as pd
import os

class AirbnbIngestion:

    def __init__(self, base_path):
        self.base_path = base_path

    def load_csv(self, filename):
        path = os.path.join(self.base_path, filename)
        if path.endswith(".gz"):
            return pd.read_csv(path, compression="gzip")
        return pd.read_csv(path)

    def ingest_city(self):
        data = {}

        files = [
            "listings.csv.gz",
            "calendar.csv.gz",
            "reviews.csv.gz",
            "neighbourhoods.csv"
        ]

        for file in files:
            key = file.split(".")[0]
            data[key] = self.load_csv(file)

        return data
