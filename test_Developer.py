import unittest
from unittest import TestCase
from Employee import Developer

class DeveloperTest(unittest.TestCase):
    def setUp(self):
        self.developer = Developer("Марина Власенко", 450)

    def tearDown(self):

        pass

    def test_work(self):
        self.assertEqual(self.developer.work(), "I come to the office and start coding.")

    def test_str(self):
        self.assertEqual(str(self.developer), "Position: Developer, Name: Марина Власенко")


if __name__ == '__main__':
    unittest.main()
