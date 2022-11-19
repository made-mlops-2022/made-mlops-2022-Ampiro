from src.config_classes import (
    PipelineParams,
    DataParams,
    LoggingParams,
    ModelParams
)
from dataclasses import fields
from omegaconf import DictConfig


def classFromArgs(className, argDict):
    fieldSet = {f.name for f in fields(className) if f.init}
    filteredArgDict = {k: v for k, v in argDict.items() if k in fieldSet}
    return className(**filteredArgDict)


def read_config(cfg: DictConfig):  # -> PipelineParams:
    data_params = classFromArgs(DataParams, cfg["data"])
    logging_params = classFromArgs(LoggingParams, cfg["logging"])
    model_params = classFromArgs(ModelParams, cfg["model"])
    params = PipelineParams(data_params, logging_params, model_params)
    return params
