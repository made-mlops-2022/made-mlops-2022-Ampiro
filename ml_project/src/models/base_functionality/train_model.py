import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from src.config_classes import ModelParams


def train_model(
    features: pd.DataFrame, target: pd.Series, model_params: ModelParams
):
    """Modal training function

    Args:
        features (pd.DataFrame)
        target (pd.Series)
        model_params (TrainingParams): dataclass with training parametrs

    Returns:
        Model: classification model described in traing params
    """
    if model_params.type == "RandomForestClassifier":
        model = RandomForestClassifier(**model_params.params)
    elif model_params.type == "SVM":
        model = SVC(**model_params.params)
    else:
        raise ValueError("wrong model type is given")
    logger = logging.getLogger("TRAIN")
    logger.info(f"Model type   {model_params.type}")
    logger.info(f"Model params {model_params.params}")
    logger.info("Training model...")
    model.fit(features, target)
    logger.info("Training is finished.")
    return model
