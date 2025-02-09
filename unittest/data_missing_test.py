import unittest
from data_missing_handler import handleMissingValue

class TestHandleMissingValue(unittest.TestCase):
    def test_remove_missing(self):
        self.assertEqual(list(handleMissingValue([[1, 2], [None, 3], [4, 5]], ("mv", "rm"))), [[1, 2], [4, 5]])
    
    def test_fill_with_value(self):
        self.assertEqual(list(handleMissingValue([[1, None], [None, 3]], ("mv", "fl_0"))), [[1, 0], [0, 3]])
    
    def test_fill_with_invalid_value(self):
        self.assertEqual(list(handleMissingValue([[1, None], [None, 3]], ("mv", "fl_x"))), [[1, 0], [0, 3]])
    
    def test_invalid_service(self):
        self.assertEqual(list(handleMissingValue([[1, None], [None, 3]], ("mv", "invalid"))), [])

if __name__ == "__main__":
    unittest.main()