import unittest
from employee import Recruiter

class RecruiterTest(unittest.TestCase):
    def setUp(self):
        self.recruiter = Recruiter("Олексій Ковальов", 400)

    def tearDown(self):

        pass

    def test_work(self):
        self.assertEqual(self.recruiter.work(), "I come to the office and start hiring.")

    def test_str(self):
        self.assertEqual(str(self.recruiter), "Position: Recruiter, Name: Олексій Ковальов")


if __name__ == '__main__':
    unittest.main()


