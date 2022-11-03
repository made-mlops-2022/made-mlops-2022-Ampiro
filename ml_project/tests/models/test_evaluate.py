from src.models.base_functionality import evaluate_model

import numpy as np
import pandas as pd
import unittest


class TestModelEvaluation(unittest.TestCase):
    def test_max_accuracy(self):
        real = pd.Series(np.random.randint(0, 2, size=(100, 1)).reshape(-1))
        pred = real.copy()
        metrics = evaluate_model(real, pred)
        self.assertEqual(metrics["accuracy"], 1)

    def test_random_accuracy(self):
        np.random.seed(42)
        real = pd.Series(np.random.randint(0, 2, size=(100, 1)).reshape(-1))
        pred = pd.Series(np.random.randint(0, 2, size=(100, 1)).reshape(-1))
        metrics = evaluate_model(real, pred)
        acc = metrics["accuracy"]
        self.assertTrue(acc < 0.55)
        self.assertTrue(acc > 0.45)

    def test_max_f1_score(self):
        real = pd.Series(np.random.randint(0, 2, size=(100, 1)).reshape(-1))
        pred = real.copy()
        metrics = evaluate_model(real, pred)
        self.assertEqual(metrics["f1"], 1)

    def test_random_f1_score(self):
        np.random.seed(42)
        real = pd.Series(np.random.randint(0, 2, size=(100, 1)).reshape(-1))
        pred = pd.Series(np.random.randint(0, 2, size=(100, 1)).reshape(-1))
        metrics = evaluate_model(real, pred)
        f1 = metrics["f1"]
        self.assertTrue(f1 < 0.55)
        self.assertTrue(f1 > 0.45)


if __name__ == "__main__":
    unittest.main()
