import pandas as pd
from evaluate_public import *
import numpy as np


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    """Method to normalize an entire DataFrame"""
    return df.apply(lambda l: l / max(l), axis=0)


def convert_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Function to convert variables to one common type (float)"""
    # Preprocessing columns in one loop to floats
    for column_name, column_dtype in zip(df.columns, df.dtypes):

        # Categorical to int
        if column_dtype == "object":
            df[column_name] = pd.factorize(df[column_name])[0]

        # All columns to float
        df[column_name] = list(map(float, df[column_name]))

    return df


