from src.models.base_functionality import (
    predict_model,
    load_model,
    save_model_predictions
)
from src.data_preporation import (
    load_data,
    get_features_target
)
from src.config_classes import PipelineParams
import logging


def predict(params: PipelineParams):
    if params.logging_params.level == "INFO":
        logging.basicConfig(level=logging.INFO)

    test_data = load_data(params.data_params.test_data_path)
    X, _ = get_features_target(test_data, params.data_params)

    model = load_model(params.model_params)
    predictions = predict_model(X, model)
    save_model_predictions(predictions, params.model_params)
