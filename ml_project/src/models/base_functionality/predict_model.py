import pandas as pd


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
    return model.predict(features)
