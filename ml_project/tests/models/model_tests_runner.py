from .test_train import TestModelTraining
from .test_predict import TestModelPrediction
from .test_evaluate import TestModelEvaluation

import unittest


def run_model_tests():
    unittest.main()


if __name__ == "__main__":
    run_model_tests()
