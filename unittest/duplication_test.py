import unittest
from duplication_handler import removeDuplication

class TestRemoveDuplication(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(removeDuplication([]), [])
    
    def test_no_duplicates(self):
        self.assertEqual(removeDuplication([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
    
    def test_with_duplicates(self):
        self.assertEqual(removeDuplication([[1, 2], [3, 4], [1, 2]]), [[1, 2], [3, 4]])
    
    def test_multiple_duplicates(self):
        self.assertEqual(removeDuplication([[1, 2], [3, 4], [1, 2], [3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]])
    
    def test_mixed_types(self):
        self.assertEqual(removeDuplication([[1, 2], "test", [1, 2], "test", (1, 2)]), [[1, 2], "test", (1, 2)])

if __name__ == "__main__":
    unittest.main()
