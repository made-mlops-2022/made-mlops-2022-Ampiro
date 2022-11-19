import pandas as pd
import logging
from typing import Tuple

from sklearn.model_selection import train_test_split
from src.config_classes import DataParams
from src.data_preporation import CustomTransformer


def load_data(data_path: str) -> pd.DataFrame:
    data = pd.read_csv(data_path)
    return data


def make_dataset(data_params: DataParams) -> None:
    logger = logging.getLogger("DATA_MAKER")
    logger.info("Data is preparing to use...")
    data = load_data(data_params.data_path)

    X, y = get_features_target(data, data_params)
    X_train, X_test, y_train, y_test = data_train_test_split(X, y)

    if data_params.params["make_preporations"]:
        logger.info("Applying custom transformer...")
        normer = CustomTransformer()
        normer.fit(X_train)
        X_train = normer.transform(X_train)
        X_test = normer.transform(X_test)
        logger.info("Data is transformed")

    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test, y_test], axis=1)

    train_data.to_csv(data_params.train_data_path, index=False)
    test_data.to_csv(data_params.test_data_path, index=False)
    logger.info("Data is preprocessed")


def get_features_target(
    data: pd.DataFrame, params: DataParams
) -> Tuple[pd.DataFrame, pd.Series]:
    X = data.drop(params.params["target"], axis=1)
    y = data[params.params["target"]]
    return (X, y)


def data_train_test_split(
    X: pd.DataFrame,
    y: pd.Series
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    return (X_train, X_test, y_train, y_test)  # type: ignore
