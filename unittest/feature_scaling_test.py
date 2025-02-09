import unittest
from feature_scaling_handler import featureScale

class TestFeatureScale(unittest.TestCase):
    def test_normalization(self):
        header = ["feature1"]
        rows = [[10], [20], [30]]
        result = featureScale(header, rows, ("id", "nm_feature1"))
        expected = [[0.0], [0.5], [1.0]]
        self.assertEqual(result, expected)

    def test_standardization(self):
        header = ["feature1"]
        rows = [[10], [20], [30]]
        result = featureScale(header, rows, ("id", "sd_feature1"))
        expected = [[-1.0], [0.0], [1.0]]
        self.assertEqual(result, expected)

    def test_invalid_service(self):
        header = ["feature1"]
        rows = [[10], [20], [30]]
        result = featureScale(header, rows, ("id", "invalid_feature1"))
        expected = [[0.0], [0.5], [1.0]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()