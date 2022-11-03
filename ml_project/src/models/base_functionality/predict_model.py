import pandas as pd
import logging


def predict_model(
    features: pd.DataFrame, model  # : Model Type
) -> pd.Series:
    """Predicting result with given model on given data

    Args:
        features (pd.DataFrame):
        model (ModelType):

    Returns:
        pd.Series: prediction result
    """
    logger = logging.getLogger("PREDICT")
    logger.info("Making prediction...")
    predictions = pd.Series(model.predict(features))
    logger.info("Predictions are made.")
    return predictions
