import pandas as pd
from evaluate_public import *
import numpy as np

df_train = pd.read_csv("../data/ford_train.csv")
df_test = pd.read_csv("../data/ford_test.csv")


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


def make_predictions(predictor, X_test: np.array, df: pd.DataFrame) -> pd.DataFrame:
    """
    Finish method to actually use the predictor to make predictions. Watch the following things:
    - Make sure not to normalize the carId's
    - If you normalize the price, this should be converted back before submitting
    - Check all your columns, make sure it represents the information well

    :param predictor: Some model with a predict function
    :param df: Test dataframe
    :return: Submission dataframe
    """

    submission = pd.DataFrame.from_dict({'carId': [], 'price': []})
    return submission