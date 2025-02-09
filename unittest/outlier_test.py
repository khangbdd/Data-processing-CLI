import unittest
from outlier_handler import handleOutlier

class TestHandleOutlier(unittest.TestCase):
    def test_remove_outliers(self):
        header = ["feature1"]
        rows = [[1], [1000], [2], [3], [4], [5], [2], [3], [2], [1], [1], [1]]
        result = handleOutlier(header, rows, ("id", "rm_feature1"))
        expected = [[1], [2], [3], [4], [5], [2], [3], [2], [1], [1], [1]]
        self.assertEqual(list(result), expected)

    def test_replace_outliers(self):
        header = ["feature1"]
        rows = [[1], [1000], [2], [3], [4], [5], [2], [3], [2], [1], [1], [1]]
        result = handleOutlier(header, rows, ("id", "rp_feature1"))
        expected = [[1], [949.4824391000557], [2], [3], [4], [5], [2], [3], [2], [1], [1], [1]]
        self.assertEqual(result, expected)

    def test_invalid_service(self):
        header = ["feature1"]
        rows = [[1], [1000], [2], [3], [4], [5], [2], [3], [2], [1], [1], [1]]
        result = handleOutlier(header, rows, ("id", "invalid_feature1"))
        expected = [[1], [949.4824391000557] ,[2], [3], [4], [5], [2], [3], [2], [1], [1], [1]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()