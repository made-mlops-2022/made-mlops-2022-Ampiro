import pandas as pd
import numpy as np
from typing import Tuple


def generate_data() -> Tuple[pd.DataFrame, pd.Series]:
    np.random.seed(42)
    X = pd.DataFrame(np.random.randint(
        0, 100, size=(100, 4)), columns=list('ABCD'))
    y = pd.DataFrame(np.random.randint(
        0, 2, size=(100, 1)), columns=list('t'))
    y = pd.Series(y.squeeze())
    return (X, y)
