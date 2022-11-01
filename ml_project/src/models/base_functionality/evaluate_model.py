from sklearn.metrics import accuracy_score, f1_score
from typing import Dict
import pandas as pd


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
    results = {
        "accuracy": accuracy_score(real_traget, pred_target),
        "f1": f1_score(real_traget, pred_target)
    }
    return results
