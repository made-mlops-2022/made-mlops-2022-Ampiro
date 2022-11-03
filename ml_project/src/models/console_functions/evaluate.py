from src.models.base_functionality import (
    load_model_predictions,
    evaluate_model
)
from src.data_preporation import (
    load_data,
    get_features_target,
)
from src.config_classes import PipelineParams
import logging
import json


def evaluate(params: PipelineParams):
    if params.logging_params.level == "INFO":
        logging.basicConfig(level=logging.INFO)

    test_data = load_data(params.data_params.test_data_path)
    _, y = get_features_target(test_data, params.data_params)

    predictions = load_model_predictions(params.model_params)
    metrics = evaluate_model(y, predictions)
    path = params.model_params.save_path + \
        params.model_params.type + "_metrics.json"
    with open(path, 'w') as f:
        json.dump(metrics, f)
