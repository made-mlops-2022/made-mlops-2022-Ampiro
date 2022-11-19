from src.models.base_functionality import predict_model
from tests import generate_data
from sklearn.dummy import DummyClassifier

import unittest


class TestModelPrediction(unittest.TestCase):
    def test_predictions(self):
        X, y = generate_data()
        model = DummyClassifier(random_state=42)
        model.fit(X, y)

        sklearn_pred = model.predict(X)
        predictions = predict_model(X, model)

        self.assertTrue(all(sklearn_pred == predictions))


if __name__ == "__main__":
    unittest.main()
