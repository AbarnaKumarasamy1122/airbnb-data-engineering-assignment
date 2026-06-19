import pandas as pd
import numpy as np

class AirbnbCleaning:

    def clean_price(self, df):
        df["price_clean"] = (
            df["price"]
            .replace("[$,]", "", regex=True)
            .astype(float)
        )
        return df

    def clean_dates(self, df, cols):
        for c in cols:
            if c in df.columns:
                df[c] = pd.to_datetime(df[c], errors="coerce")
        return df

    def clean_text(self, df, cols):
        for c in cols:
            if c in df.columns:
                df[c] = df[c].str.lower().str.strip()
        return df
