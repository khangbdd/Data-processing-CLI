import sys
import os
# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from encoding_handler import handleEncoding
import unittest

class TestHandleEncoding(unittest.TestCase):
    def test_onehot_encoding(self):
        header = ["feature1"]
        rows = [["A"], ["B"], ["A"], ["C"]]
        result = handleEncoding(header, rows, ("id", "oh_feature1"))
        expected = [[[1, 0, 0]], [[0, 1, 0]], [[1, 0, 0]], [[0, 0, 1]]]
        self.assertEqual(result, expected)
    
    def test_ordinal_encoding(self):
        header = ["feature1"]
        rows = [["A"], ["B"], ["A"], ["C"]]
        result = handleEncoding(header, rows, ("id", "od_feature1"))
        expected = [[0], [1], [0], [2]]
        self.assertEqual(result, expected)
    
    def test_invalid_encoding_service(self):
        header = ["feature1"]
        rows = [["A"], ["B"], ["A"], ["C"]]
        result = handleEncoding(header, rows, ("id", "invalid_feature1"))
        expected = [[[1, 0, 0]], [[0, 1, 0]], [[1, 0, 0]], [[0, 0, 1]]]
        self.assertEqual(result, expected)
    
    def test_missing_feature(self):
        header = ["feature1"]
        rows = [["A"], ["B"], ["A"], ["C"]]
        with self.assertRaises(Exception):
            handleEncoding(header, rows, ("id", "oh"))

if __name__ == "__main__":
    unittest.main()