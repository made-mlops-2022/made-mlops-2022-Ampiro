from models.base_functionality import (
    train_model,
    predict_model,
    evaluate_model
)
from data_preporation import (
    make_dataset,
    get_features_target
)
from config_classes import PipelineParams


def pipeline():
    params = PipelineParams(
        data_file_path="data/raw/heart_cleveland_upload.csv",
        model_save_path="."
    )
    data = make_dataset(params.data_file_path)
    X, y = get_features_target(data, params.data_params)
    model = train_model(X, y, params.training_params)
    predictions = predict_model(X, model)
    metrics = evaluate_model(y, predictions)
    print(metrics)


if __name__ == "__main__":
    pipeline()
