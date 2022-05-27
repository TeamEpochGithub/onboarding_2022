import pandas as pd


def score_submission_path(path_to_csv: str, mode='mse') -> float:
    """
    Public method to score submission. The actual script that does the calculations is hidden to not reveal any answers.
    Use this method to score your submissions

    Your submission csv should at least contain two columns, one named carId and one named price.
    It should contain all carId's in the ford_test.csv file, combined with your price prediction

    :param path_to_csv: Path to your submission csv file
    :param mode: Scoring metric. Options are 'mse' and 'mae' for mean squared or mean absolute error
    :return: The MSE or MAE value as float
    """
    import evaluate
    return evaluate.score_submission(path_to_csv, mode=mode)


def score_submission_df(df: pd.DataFrame, mode='mse') -> float:
    df.to_csv("../data/temp_submission.csv", index=False)
    return score_submission_path("../data/temp_submission.csv", mode=mode)
