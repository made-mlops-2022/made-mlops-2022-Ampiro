from dataclasses import dataclass


@dataclass()
class DataParams:
    data_path: str
    train_data_path: str
    test_data_path: str
    params: dict
    """
    params dict:
        - target str: target column in data
        - make_preporations bool: wether preporations is to be done on
            input data or not
    """
