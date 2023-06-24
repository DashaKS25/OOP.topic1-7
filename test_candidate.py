import unittest
from unittest.mock import patch
from decorators import CandidateGenerator, Candidate


class TestCandidateGenerator(unittest.TestCase):

    @patch('decorators.CandidateGenerator.generate_candidates')
    def test_generate_candidates(self, mock_method):
        # file_path = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'

        expected_candidates = [
            Candidate('Ivan', 'Chechov', 'ichech@example.com', ['Python', 'Django', 'Angular'], 'Python', 'Senior'),
            Candidate('Max', 'Payne', 'mpayne@example.com', ['PHP', 'Laravel', 'MySQL'], 'PHP', 'Middle'),
            Candidate('Tom', 'Hanks', 'thanks@example.com', ['Python', 'CSS'], 'Python', 'Junior')
        ]
        mock_method.return_value = expected_candidates
        candidates = CandidateGenerator.generate_candidates('')

        self.assertEqual(len(candidates), 3)

        for i in range(len(candidates)):
            self.assertEqual(candidates[i], expected_candidates[i])
            self.assertEqual(candidates[i].email, expected_candidates[i].email)
            self.assertEqual(candidates[i].tech_stack, expected_candidates[i].tech_stack)
            self.assertEqual(candidates[i].main_skill, expected_candidates[i].main_skill)
            self.assertEqual(candidates[i].main_skill_grade, expected_candidates[i].main_skill_grade)

if __name__ == '__main__':
    unittest.main()