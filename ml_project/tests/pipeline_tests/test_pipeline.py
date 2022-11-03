from src.models.console_functions.pipeline import pipeline_command
from src.models.base_functionality.model_io import (
    load_model
)
from src.data_preporation import (
    read_config
)
from sklearn.svm import SVC

import sys
import yaml
from yaml.loader import SafeLoader
import unittest
from unittest.mock import patch


class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        patched_args = ["pipeline_command",
                        "test_config", "tests/pipeline_tests"]
        with patch.object(sys, 'argv', patched_args):
            pipeline_command()

        with open('tests/pipeline_tests/test_config.yaml') as f:
            cfg = yaml.load(f, Loader=SafeLoader)
        params = read_config(cfg)

        model = load_model(params.model_params)
        self.assertIsInstance(model, SVC)
        for param in params.model_params.params.keys():
            self.assertEqual(
                params.model_params.params[param], model.get_params()[param])


if __name__ == "__main__":
    unittest.main()
