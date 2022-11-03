import pickle
import pandas as pd
from src.config_classes import ModelParams
from src.data_preporation import load_data


def save_model(model, model_params: ModelParams):
    path = model_params.save_path + model_params.type + ".pkl"
    with open(path, 'wb') as f:
        pickle.dump(model, f)


def load_model(model_params: ModelParams):
    path = model_params.save_path + model_params.type + ".pkl"
    with open(path, 'rb') as f:
        model = pickle.load(f)
        return model


def save_model_predictions(predictions: pd.Series, model_params: ModelParams):
    path = model_params.save_path + model_params.type + "_preds.csv"
    predictions.to_csv(path, index=False)


def load_model_predictions(
    model_params: ModelParams
) -> pd.Series:
    path = model_params.save_path + model_params.type + "_preds.csv"
    data = load_data(path)
    if len(data.columns) > 1:
        raise ValueError("predictions must have 1 column")
    predictions = data.squeeze().to_frame()
    return predictions
