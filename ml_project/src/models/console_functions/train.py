from src.models.base_functionality import (
    train_model,
    save_model
)
from src.data_preporation import (
    make_dataset,
    load_data,
    get_features_target
)
from src.config_classes import PipelineParams
import logging


def train(params: PipelineParams):

    if params.logging_params.level == "INFO":
        logging.basicConfig(level=logging.INFO)

    make_dataset(params.data_params)
    train_data = load_data(params.data_params.train_data_path)
    X, y = get_features_target(train_data, params.data_params)

    model = train_model(X, y, params.model_params)
    save_model(model, params.model_params)
