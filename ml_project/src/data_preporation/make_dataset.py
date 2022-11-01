import pandas as pd
from typing import Tuple
from config_classes import DataParams


def make_dataset(file_path: str) -> pd.DataFrame:
    data = pd.read_csv(file_path)
    return data


def get_features_target(
    data: pd.DataFrame, params: DataParams
) -> Tuple[pd.DataFrame, pd.Series]:
    data.drop(params.cols_to_drop, inplace=True, axis=1)
    X = data.drop(params.target_col, axis=1)
    y = data[params.target_col]
    return (X, y)


def data_train_test_split(X: pd.DataFrame, y: pd.Series):
    pass
