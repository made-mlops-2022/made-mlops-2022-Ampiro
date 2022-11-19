from sklearn.base import BaseEstimator, TransformerMixin
import logging
import pandas as pd


class CustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.logger = logging.getLogger("TRANSFORMER".upper())
        self.std = None
        self.mean = None

    def fit(self, X: pd.DataFrame):
        self.logger.info("Fitting data...")
        self.std = X.std()
        self.mean = X.mean()
        self.logger.info("Data is fitted")

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        if (self.std != 0).all():
            self.logger.info("Transforming data...")
            X_norm = (X - self.mean) / (self.std)
            self.logger.info("Data is transformed")
        else:
            raise ValueError("Division by zero in normalization")
        return X_norm
