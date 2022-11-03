from src.data_preporation import CustomTransformer
from tests.data_generator import generate_data
import unittest


class TestCustomTransformer(unittest.TestCase):
    def test_transformation(self):
        transformer = CustomTransformer()
        X, _ = generate_data()

        transformer.fit(X)
        X_norm = transformer.transform(X)
        std = X_norm.std()
        mean = X_norm.mean()

        epsilon = 1e-3
        self.assertTrue(all(mean > 0-epsilon))
        self.assertTrue(all(mean < 0+epsilon))
        self.assertTrue(all(std > 1-epsilon))
        self.assertTrue(all(std < 1+epsilon))


if __name__ == "__main__":
    unittest.main()
