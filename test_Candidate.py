import unittest
import urllib.request
from decorators import Candidate

class CandidateTest(unittest.TestCase):
    def setUp(self):
        url = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
        self.candidates = Candidate.generate_candidates(url)

    def tearDown(self):

        pass

    def test_full_name(self):
        candidate = self.candidates[0]
        self.assertEqual(candidate.full_name, "Dasha Kovl")

    def test_generate_candidates(self):
        self.assertEqual(len(self.candidates), 2)
        self.assertEqual(self.candidates[0].email, "dashyn@test.com")
        self.assertEqual(self.candidates[1].main_skill_grade, "B")

    def test_tech_stack(self):
        candidate = self.candidates[0]
        self.assertEqual(candidate.tech_stack, ["Python", "JavaScript"])


if __name__ == '__main__':
    unittest.main()

