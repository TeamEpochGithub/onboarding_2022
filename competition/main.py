import numpy as np

from evaluate_public import *


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


def test_pipeline():
    df_train = pd.read_csv("../data/ford_train.csv")
    df_test = pd.read_csv("../data/ford_test.csv")

    mock_submission = pd.DataFrame.from_dict({'carId': df_test['carId'], 'price': [0] * len(df_test)})
    print(f"Your pipeline works, mock submission scored: \n {score_submission_df(mock_submission, mode='mse')} "
          f"MSE \n {score_submission_df(mock_submission, mode='mae')} MAE")


if __name__ == "__main__":
    test_pipeline()
