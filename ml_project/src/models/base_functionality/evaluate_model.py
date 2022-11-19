from sklearn.metrics import accuracy_score, f1_score
from typing import Dict
import pandas as pd
import logging


def evaluate_model(
    real_traget: pd.Series, pred_target: pd.Series
) -> Dict[str, float]:
    """Returs several calculated metrics of predictions

    Args:
        real_traget (List[int])
        pred_target (List[int])

    Returns:
        Dict[str, float]: dict of metrics
    """
    logger = logging.getLogger("EVALUATE")
    logger.info("Making evaluation...")
    results = {
        "accuracy": accuracy_score(real_traget, pred_target),
        "f1": f1_score(real_traget, pred_target)
    }
    acc = results["accuracy"]
    f1 = results["f1"]
    logger.info(f"Accuracy {acc}")
    logger.info(f"F1       {f1}")
    logger.info("Evaluation is finished")
    return results
