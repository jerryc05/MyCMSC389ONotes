import unittest
from solution import findDuplicates

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual([3], findDuplicates([1,3,2,3]))

    def test2(self):
        self.assertEqual([1], findDuplicates([1,1]))

    def test3(self):
        self.assertEqual([2,4], findDuplicates([2,4,2,4]))

    def test4(self):
        self.assertEqual([1,2], findDuplicates([1,1,2,2]))

if __name__ == "__main__":
    unittest.main()
