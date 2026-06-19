import pandas as pd 

class AirbnbTransform:

    def compute_host_tenure(self, df):
        df["host_since"] = pd.to_datetime(df["host_since"])
        df["host_tenure_years"] = (
            (pd.Timestamp("today") - df["host_since"]).dt.days / 365
        )
        return df

    def price_per_bedroom(self, df):
        df["price_per_bedroom"] = df["price_clean"] / df["bedrooms"]
        return df

    def occupancy_rate(self, calendar):
        summary = calendar.groupby("listing_id")["available"].apply(
            lambda x: (x == "f").mean()
        )
        return summary.reset_index(name="occupancy_rate")
