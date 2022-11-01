from dataclasses import dataclass, field
from config_classes.data_params import DataParams
from config_classes.training_params import TrainingParams


@dataclass()
class PipelineParams:
    data_file_path: str
    model_save_path: str
    data_params: DataParams = field(default=DataParams())
    training_params: TrainingParams = field(default=TrainingParams())
