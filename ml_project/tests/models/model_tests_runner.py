from .test_train import TestModelTraining  # noqa
from .test_predict import TestModelPrediction  # noqa
from .test_evaluate import TestModelEvaluation  # noqa

import unittest


def run_model_tests():
    unittest.main()


if __name__ == "__main__":
    run_model_tests()
