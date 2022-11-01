import pandas as pd

# from sklearn.base import ClassifierMixin
from sklearn.ensemble import RandomForestClassifier
from config_classes import TrainingParams


def train_model(
    features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
):
    """Modal training function

    Args:
        features (pd.DataFrame)
        target (pd.Series)
        training_params (TrainingParams): dataclass with training parametrs

    Returns:
        Model: classification model described in traing params
    """
    if train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(**train_params.model_params)
    else:
        raise ValueError("wrong model type was provided")
    model.fit(features, target)
    return model
