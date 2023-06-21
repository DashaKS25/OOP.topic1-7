import urllib.request

class Candidate:
    FULL_NAME_FIELD = 'Full Name'
    EMAIL_FIELD = 'Email'
    TECH_STACK_FIELD = 'Technologies'
    MAIN_SKILL_FIELD = 'Main Skill'
    MAIN_SKILL_GRADE_FIELD = 'Main Skill Grade'

    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class CandidateParser:
    @staticmethod
    def parse_candidate_data(candidate_data, header):
        print(candidate_data)
        data_dict = {header[i]: candidate_data[i].strip() for i in range(len(header))}
        print(data_dict)
        first_name = data_dict.get(Candidate.FULL_NAME_FIELD, '')
        last_name = ''
        if len(first_name.split(' ')) > 1:
            last_name = first_name.split(' ')[-1].strip()
        email = data_dict.get(Candidate.EMAIL_FIELD, '')
        tech_stack = data_dict.get(Candidate.TECH_STACK_FIELD, '').split('|')
        main_skill = data_dict.get(Candidate.MAIN_SKILL_FIELD, '')
        main_skill_grade = data_dict.get(Candidate.MAIN_SKILL_GRADE_FIELD, '')

        candidate = Candidate(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
        return candidate


class CandidateGenerator:
    @staticmethod
    def generate_candidates(file_path):
        candidates = []

        with urllib.request.urlopen(file_path) as response:
            data = response.read().decode('utf-8')

        lines = data.strip().split('\n')
        header = lines[0].split(',')
        for line in lines[1:]:
            candidate_data = line.strip().split(',')
            if len(candidate_data) == len(header):
                candidate = CandidateParser.parse_candidate_data(candidate_data, header)
                candidates.append(candidate)

        return candidates



url = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
candidates = CandidateGenerator.generate_candidates(url)
url = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
candidates = CandidateGenerator.generate_candidates(url)
for candidate in candidates:
    print(candidate.first_name)
    print(candidate.last_name)
    print(candidate.email)
    print(candidate.tech_stack)
    print(candidate.main_skill)
    print(candidate.main_skill_grade)
    print(candidate.full_name)
    print()
