import unittest
from decorators import CandidateGenerator, Candidate

class TestCandidateGenerator(unittest.TestCase):
    def test_generate_candidates(self):
        file_path = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
        candidates = CandidateGenerator.generate_candidates(file_path)

        self.assertEqual(len(candidates), 3)

        expected_candidates = [
            Candidate('Ivan', 'Chechov', 'ichech@example.com', ['Python', 'Django', 'Angular'], 'Python', 'Senior'),
            Candidate('Max', 'Payne', 'mpayne@example.com', ['PHP', 'Laravel', 'MySQL'], 'PHP', 'Middle'),
            Candidate('Tom', 'Hanks', 'thanks@example.com', ['Python', 'CSS'], 'Python', 'Junior')
        ]

        for i in range(len(candidates)):
            self.assertEqual(candidates[i].first_name, expected_candidates[i].full_name)
            self.assertEqual(candidates[i].email, expected_candidates[i].email)
            self.assertEqual(candidates[i].tech_stack, expected_candidates[i].tech_stack)
            self.assertEqual(candidates[i].main_skill, expected_candidates[i].main_skill)
            self.assertEqual(candidates[i].main_skill_grade, expected_candidates[i].main_skill_grade)

if __name__ == '__main__':
    unittest.main()
