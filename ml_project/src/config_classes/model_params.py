from dataclasses import dataclass


@dataclass()
class ModelParams:
    save_path: str
    type: str
    params: dict
