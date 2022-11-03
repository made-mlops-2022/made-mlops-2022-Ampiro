from data_preporation.test_custom_transformer import TestCustomTransformer
from models.test_train import TestModelTraining
from models.test_predict import TestModelPrediction
from models.test_evaluate import TestModelEvaluation
from pipeline_tests.test_pipeline import TestPipeline


import unittest


def run_tests():
    unittest.main()


if __name__ == "__main__":
    run_tests()
