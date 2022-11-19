from src.models.base_functionality import train_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from src.config_classes import ModelParams
from tests import generate_data

import unittest


class TestModelTraining(unittest.TestCase):
    def test_random_forest(self):
        model_params = {
            'criterion': 'gini',
            'max_depth': 5,
            'n_estimators': 10,
            'random_state': 42
        }
        params = ModelParams(
            ".",
            "RandomForestClassifier",
            model_params
        )
        X, y = generate_data()
        model = train_model(X, y, params)

        self.assertIsInstance(model, RandomForestClassifier)
        for param in model_params.keys():
            self.assertEqual(model_params[param], model.get_params()[param])

    def test_svm(self):
        model_params = {
            "C": 10,
            "kernel": "rbf"
        }
        params = ModelParams(
            ".",
            "SVM",
            model_params
        )
        X, y = generate_data()
        model = train_model(X, y, params)

        self.assertIsInstance(model, SVC)
        for param in model_params.keys():
            self.assertEqual(model_params[param], model.get_params()[param])

    def test_incorrect_model_params(self):
        model_params = {}
        params = ModelParams(
            ".",
            "WRONG_MODEL_TYPE",
            model_params
        )
        X, y = generate_data()

        with self.assertRaises(ValueError):
            _ = train_model(X, y, params)


if __name__ == "__main__":
    unittest.main()
