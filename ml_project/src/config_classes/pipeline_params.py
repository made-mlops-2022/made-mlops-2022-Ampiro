from dataclasses import dataclass
from src.config_classes.data_params import DataParams
from src.config_classes.model_params import ModelParams
from src.config_classes.logging_params import LoggingParams


@dataclass()
class PipelineParams:
    data_params: DataParams
    logging_params: LoggingParams
    model_params: ModelParams
