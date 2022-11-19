from src.models.console_functions import (
    train,
    predict,
    evaluate
)
from src.data_preporation import (
    read_config
)
from hydra import compose, initialize
import sys


def commands_runner():
    command = sys.argv[0].split("/")[-1]
    config_name = sys.argv[1]
    config_path = "../../../configs" if len(
        sys.argv) == 2 else "../../../" + sys.argv[2]

    initialize(
        config_path=config_path,
        version_base=None
    )
    cfg = compose(config_name=config_name)
    params = read_config(cfg)

    if command == "train":
        train.train(params)
    if command == "predict":
        predict.predict(params)
    if command == "evaluate":
        evaluate.evaluate(params)


def pipeline_command():
    config_name = sys.argv[1]
    config_path = "../../../configs" if len(
        sys.argv) == 2 else "../../../" + sys.argv[2]
    initialize(
        config_path=config_path,
        version_base=None
    )
    cfg = compose(config_name=config_name)
    params = read_config(cfg)

    train.train(params)
    predict.predict(params)
    evaluate.evaluate(params)
