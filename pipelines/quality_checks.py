import pandas as pd

class DataQuality:

    def missing_report(self, df):
        return (df.isnull().mean() * 100).sort_values(ascending=False)

    def duplicate_check(self, df, subset=None):
        if subset:
            return df.duplicated(subset=subset).sum()
        return df.duplicated().sum()

    def numeric_outliers(self, df, col):
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        return df[(df[col] < lower) | (df[col] > upper)]
